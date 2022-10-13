import\
    abc as _abc,\
    contextlib as _contextlib,\
    re as _re,\
    sys as _sys,\
    types as _types,\
    typing as _typing,\
    unicodedata as _unicodedata
from .. import globals as _globals
from .. import utils as _utils
from . import types as _types_0

_default_delimiters: _typing.Collection[str] = tuple(chr(char) for char in range(
    _sys.maxunicode) if _unicodedata.category(chr(char)).startswith('P'))


class Writer(metaclass=_abc.ABCMeta):
    @_abc.abstractmethod
    def __init__(self,
                 data: _types_0.ParsedData,
                 *,
                 bindings: _typing.Dict[str, 'Writer'],
                 **_: _typing.Any) -> None: ...

    @_abc.abstractmethod
    def write(self) -> None: ...

    @property
    @_abc.abstractmethod
    def location(self) -> _utils.FileTextLocation: ...

    @property
    @_abc.abstractmethod
    def data(self) -> _typing.Any: ...


class AffixableWriter:
    def __init__(self,
                 data: _types_0.ParsedData,
                 *,
                 bindings: _typing.Dict[str, Writer],
                 **_: _typing.Any) -> None:
        self.__pretext: str = data.get('pretext', '')
        self.__posttext: str = data.get('posttext', '')

    @_contextlib.contextmanager
    def _affix(self, file: _typing.TextIO) -> _typing.Iterator[None]:
        file.write(self.__pretext)
        yield
        file.write(self.__posttext)


class TextWriter(AffixableWriter):
    def __init__(self,
                 data: _types_0.ParsedData,
                 *,
                 bindings: _typing.Dict[str, Writer],
                 **_: _typing.Any) -> None:
        super().__init__(data, bindings=bindings, **_)
        self.__location: _utils.FileTextLocation = data['location']
        self.__text: str = data['text']
        self.__prefix: str = data.get('prefix', '')
        self.__suffix: str = data.get('suffix', '')

    def write(self) -> None:
        file: _typing.TextIO
        with self.__location.open() as file:
            with self._affix(file):
                file.writelines(''.join(('' if index == 0 else '\n', self.__prefix, line, self.__suffix))
                                for index, line in enumerate(self.__text.splitlines()))
            file.truncate()

    @property
    def location(self) -> _utils.FileTextLocation: return self.__location

    @property
    def data(self) -> str: return self.__text


class TextChunkWriter(AffixableWriter):
    format: str = '{number}. {pretext}→{next_hint}:::{prev_hint}←{posttext} {comment}'

    def __init__(self,
                 data: _types_0.ParsedData,
                 *,
                 bindings: _typing.Dict[str, Writer],
                 **_: _typing.Any) -> None:
        super().__init__(data, bindings=bindings, **_)
        self.__location: _utils.FileTextLocation = data['location']

        writer: Writer = bindings[data['writer']]
        delimiters: _typing.Collection[str] = data.get(
            'delimiters', _default_delimiters)
        scheme: _typing.Iterable[int | str | _typing.Any] = data['scheme']

        all_delimiters: str = '|'.join(map(_re.escape, delimiters))
        raw_chunks: _typing.Sequence[str] = tuple(chunk for chunk in _re.split(
            f'(?<={all_delimiters})(?!{all_delimiters})', writer.data) if chunk)

        def parse_scheme() -> _typing.Iterator[_typing.Sequence[str] | str]:
            start: int = 0
            chunk_scheme: int | str | _typing.Any
            for chunk_scheme in scheme:
                if isinstance(chunk_scheme, int):
                    if chunk_scheme >= 0:
                        yield raw_chunks[start:start + chunk_scheme]
                        start += chunk_scheme
                    else:
                        start -= chunk_scheme
                elif isinstance(chunk_scheme, str):
                    yield chunk_scheme
                else:
                    raise TypeError(chunk_scheme)
            remain: _typing.Sequence[str] = raw_chunks[start:]
            if remain:
                yield remain
        self.__chunks: _typing.Sequence[_typing.Sequence[str] | str] = tuple(
            parse_scheme())

    def write(self) -> None:
        file: _typing.TextIO
        with self.__location.open() as file:
            text: str = file.read()
            comments: _typing.Sequence[str] = _re.findall(
                _globals.flashcard_regex, text)
            file.seek(0)
            with self._affix(file):
                index: int
                chunk: _typing.Sequence[str] | str
                for index, chunk in enumerate(self.__chunks[:-1]):
                    next_chunk: _typing.Sequence[str] | str = self.__chunks[index + 1]
                    pretext: str
                    prev_hint: str
                    next_hint: str
                    posttext: str
                    if isinstance(chunk, str):
                        pretext = chunk
                        prev_hint = ''
                    else:
                        pretext = ''.join(chunk)
                        prev_hint = str(len(chunk))
                    if isinstance(next_chunk, str):
                        posttext = next_chunk
                        next_hint = ''
                    else:
                        posttext = ''.join(next_chunk)
                        next_hint = str(len(next_chunk))
                    if index != 0:
                        file.write('\n')
                    file.write(self.format.format(
                        number=index + 1,
                        pretext=pretext,
                        next_hint=next_hint,
                        prev_hint=prev_hint,
                        posttext=posttext,
                        comment=comments[index] if index < len(
                            comments) else ''
                    ))
            file.truncate()

    @property
    def location(self) -> _utils.FileTextLocation: return self.__location

    @property
    def data(
        self) -> _typing.Sequence[_typing.Sequence[str] | str]: return self.__chunks


class SemanticsWriter(AffixableWriter):
    format = '{number}. {pretext}::{posttext} {comment}'

    def __init__(self,
                 data: _types_0.ParsedData,
                 *,
                 bindings: _typing.Dict[str, Writer],
                 **_: _typing.Any) -> None:
        super().__init__(data, bindings=bindings, **_)
        self.__location: _utils.FileTextLocation = data['location']

        writers: _typing.Tuple[Writer, Writer] = tuple(
            bindings[writer] for writer in data['writers'])
        if len(writers) != 2:
            raise ValueError(writers)

        self.__semantics: _typing.Sequence[_typing.Tuple[str, str]] = tuple(
            filter(lambda sem: sem[0] and sem[1],
                   map(lambda pair: tuple(ele if isinstance(ele, str) else ''.join(ele) for ele in pair),
                       zip(writers[0].data, writers[1].data, strict=True))))

    def write(self):
        file: _typing.TextIO
        with self.__location.open() as file:
            text: str = file.read()
            comments: _typing.Sequence[str] = _re.findall(
                _globals.flashcard_regex, text)
            file.seek(0)
            with self._affix(file):
                file.writelines(('' if index == 0 else '\n') + self.format.format(
                    number=index + 1,
                    pretext=sem[0],
                    posttext=sem[1],
                    comment=comments[index] if index < len(comments) else ''
                ) for index, sem in enumerate(self.__semantics))
                file.truncate()

    @property
    def location(self) -> _utils.FileTextLocation: return self.__location

    @property
    def data(
        self) -> _typing.Sequence[_typing.Tuple[str, str]]: return self.__semantics


class Writers:
    types: _typing.Dict[str, type] = {
        'text': TextWriter,
        'text_chunk': TextChunkWriter,
        'semantics': SemanticsWriter
    }

    def __init__(self) -> None:
        self.__content: _typing.MutableSequence[Writer] = []

    def add_from(self, data: _types_0.ParsedData) -> None:
        if not isinstance(data, _typing.Collection):
            data = (data,)
        bindings: _typing.Dict[str, Writer] = dict()
        datum: _types_0.ParsedData
        for datum in data:
            writer: Writer = self.types[datum['type']](
                datum, bindings=_types.MappingProxyType(bindings))
            try:
                bindings[datum['name']] = writer
            except KeyError:
                pass
            self.__content.append(writer)

    def write(self) -> None:
        writer: Writer
        for writer in tuple(self.__content):
            writer.write()

    @property
    def content(self) -> _typing.Sequence[Writer]: return tuple(self.__content)

    def __iter__(
        self) -> _typing.Iterator[Writer]: return tuple(self.__content).__iter__()
