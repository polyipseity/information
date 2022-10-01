import\
    contextlib as _contextlib,\
    datetime as _datetime,\
    io as _io,\
    os as _os,\
    typing as _typing
from .. import globals as _globals


class FileTextLocation:
    __slots__ = '__file', '__id', '__start', '__end'

    def __init__(self, *, file: str = _os.devnull, id: str = '', **kwargs):
        self.__file = file
        self.__id = id
        self.__start = f'<!--{_globals.uuid},generate,id,{id}-->'
        self.__end = f'<!--{_globals.uuid},generate,end-->'

    def __repr__(self) -> str:
        return f'{type(self).__name__}(file={self.__file!r}, id={self.__id!r})'

    @property
    def file(self): return self.__file

    @property
    def id(self): return self.__id

    class FileTextIO(_io.StringIO):
        comment = '<!-- Following content is generated at {}. Any edits will be overridden! -->'

        def __init__(self, file: _typing.TextIO, slice: slice, **kwargs) -> None:
            assert file.readable(), file.readable()
            assert file.writable(), file.writable()
            assert slice.step is None, slice.step

            self.__file = file
            self.__slice = slice

            file.seek(0)
            file.read(slice.start)
            super().__init__(file.read(slice.stop - slice.start), **kwargs)

        def close(self) -> None:
            try:
                self.seek(0)
                text = self.read()
                with self.__file:
                    self.__file.seek(0)
                    all_text = self.__file.read()
                    self.__file.seek(0)
                    self.__file.write(
                        ''.join((
                            all_text[:self.__slice.start],
                            self.comment.format(
                                _datetime.datetime.now().astimezone().isoformat()),
                            text,
                            all_text[self.__slice.stop:]
                        )))
                    self.__file.truncate()
            finally:
                super().close()

    @_contextlib.contextmanager
    def open(self) -> _typing.Iterator[_io.TextIOBase]:
        file = open(self.__file, mode='r+t', **_globals.open_default_options)
        if not self.__id:
            with file:
                yield file
            return
        try:
            text = file.read()
            start = text.find(self.__start)
            if start == -1:
                raise ValueError(f'File text location not found: {self}')
            start += len(self.__start)
            end = text.find(self.__end, start)
            if end == -1:
                raise ValueError(
                    f'Unenclosed file text location at char {start}: {self}')
            ret = self.FileTextIO(file, slice(start, end))
        except BaseException as exc:
            file.close()
            raise exc
        with ret:
            yield ret
