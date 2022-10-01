import\
    abc as _abc,\
    collections as _collections,\
    contextlib as _contextlib,\
    logging as _logging,\
    re as _re,\
    sys as _sys,\
    types as _types,\
    typing as _typing,\
    unicodedata as _unicodedata
from .. import utils as _utils
import collections.abc as _
del _

_default_delimiters = tuple(chr(char) for char in range(_sys.maxunicode)
                            if _unicodedata.category(chr(char)).startswith('P'))
_flashcard_regex = '<!--SR:.*?-->'


class Writer(_abc.ABC):
    @_abc.abstractmethod
    def __init__(self, data, *, bindings, **kwargs): ...

    @_abc.abstractmethod
    def write(self): ...

    @property
    @_abc.abstractmethod
    def location(self): ...

    @property
    @_abc.abstractmethod
    def data(self): ...


class AffixableWriter:
    def __init__(self, data, *, bindings, **kwargs):
        self.__pretext = data.get('pretext', '')
        self.__posttext = data.get('posttext', '')

    @_contextlib.contextmanager
    def affix(self, file):
        file.write(self.__pretext)
        yield
        file.write(self.__posttext)


class TextWriter(AffixableWriter):
    def __init__(self, data, *, bindings, **kwargs):
        super().__init__(data, bindings=bindings, **kwargs)
        self.__location: _utils.FileTextLocation = data['location']
        self.__text = data['text']
        self.__prefix = data.get('prefix', '')
        self.__suffix = data.get('suffix', '')

    def write(self):
        with self.__location.open() as file:
            with self.affix(file):
                file.writelines(''.join(('' if index == 0 else '\n', self.__prefix, line, self.__suffix))
                                for index, line in enumerate(self.__text.splitlines()))
            file.truncate()

    @property
    def location(self): return self.__location

    @property
    def data(self): return self.__text


class TextChunkWriter(AffixableWriter):
    format = '{number}. {pretext}→{next_hint}:::{prev_hint}←{posttext} {comment}'

    def __init__(self, data, *, bindings, **kwargs):
        super().__init__(data, bindings=bindings, **kwargs)
        self.__location: _utils.FileTextLocation = data['location']

        writer = bindings[data['writer']]
        delimiters = data.get('delimiters', _default_delimiters)
        scheme: _typing.Iterable[int | str | None] = data['scheme']

        all_delimiters = '|'.join(map(_re.escape, delimiters))
        raw_chunks = tuple(chunk for chunk in _re.split(
            f'(?<={all_delimiters})(?!{all_delimiters})', writer.data) if chunk)
        _logging.info(f'Separated into {len(raw_chunks)} chunks')

        def parse_scheme():
            start = 0
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
            remain = raw_chunks[start:]
            if remain:
                yield remain
        self.__chunks = tuple(parse_scheme())

    def write(self):
        with self.__location.open() as file:
            text = file.read()
            comments: list[str] = _re.findall(_flashcard_regex, text)
            file.seek(0)
            with self.affix(file):
                for index, chunk in enumerate(self.__chunks[:-1]):
                    next_chunk = self.__chunks[index + 1]
                    if isinstance(chunk, str):
                        pretext = chunk
                        prev_hint = ''
                    else:
                        pretext = ''.join(chunk)
                        prev_hint = len(chunk)
                    if isinstance(next_chunk, str):
                        posttext = next_chunk
                        next_hint = ''
                    else:
                        posttext = ''.join(next_chunk)
                        next_hint = len(next_chunk)
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
    def location(self): return self.__location

    @property
    def data(self): return self.__chunks


class SemanticsWriter(AffixableWriter):
    format = '{number}. {pretext}::{posttext} {comment}'

    def __init__(self, data, *, bindings, **kwargs):
        super().__init__(data, bindings=bindings, **kwargs)
        self.__location: _utils.FileTextLocation = data['location']

        writers = tuple(bindings[writer] for writer in data['writers'])

        self.__semantics = tuple(filter(lambda sem: sem[0] and sem[1], ((
            left if isinstance(
                left, str) else ''.join(left),
            right if isinstance(
                right, str) else ''.join(right)
        ) for left, right in zip(writers[0].data, writers[1].data, strict=True))))

    def write(self):
        with self.__location.open() as file:
            text = file.read()
            comments: list[str] = _re.findall(_flashcard_regex, text)
            file.seek(0)
            with self.affix(file):
                file.writelines(('' if index == 0 else '\n') + self.format.format(
                    number=index + 1,
                    pretext=sem[0],
                    posttext=sem[1],
                    comment=comments[index] if index < len(comments) else ''
                ) for index, sem in enumerate(self.__semantics))
                file.truncate()

    @property
    def location(self): return self.__location

    @property
    def data(self): return self.__semantics


class Writers:
    types = _types.MappingProxyType({
        'text': TextWriter,
        'text_chunk': TextChunkWriter,
        'semantics': SemanticsWriter
    })

    def __init__(self):
        self.__content = []

    def add_from(self, data):
        if not isinstance(data, _collections.abc.Iterable):
            data = (data,)
        bindings = dict()
        for datum in data:
            writer = self.types[datum['type']](
                datum, bindings=_types.MappingProxyType(bindings))
            try:
                bindings[datum['name']] = writer
            except KeyError:
                pass
            self.__content.append(writer)

    def write(self):
        for writer in tuple(self.__content):
            writer.write()

    @property
    def content(self): return tuple(self.__content)

    def __iter__(self): return tuple(self.__content).__iter__()
