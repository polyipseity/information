import abc as _abc
import ast as _ast
import builtins as _builtins
import pathlib as _pathlib
import types as _types
import typing as _typing

from .. import globals as _globals
from . import environment as _environment
from . import venv as _venv
from . import write as _write


class Reader(metaclass=_abc.ABCMeta):
    registry: _typing.MutableMapping[str, type] = {}
    __slots__ = ()

    @_abc.abstractmethod
    def __init__(self: _typing.Self, *,
                 path: _pathlib.PurePath,
                 comment: bool = True) -> None: ...

    @property
    @_abc.abstractmethod
    def path(self: _typing.Self) -> _pathlib.PurePath: ...

    @property
    @_abc.abstractmethod
    def comment(self: _typing.Self) -> bool: ...

    @_abc.abstractmethod
    def read(self: _typing.Self, text: str, /) -> None: ...

    @_abc.abstractmethod
    def pipe(self: _typing.Self) -> _typing.Collection[_write.Writer]: ...

    @classmethod
    def __subclasshook__(cls: type[_typing.Self], subclass: type) -> bool | _types.NotImplementedType:
        if cls is Reader:
            if any(all(p not in c.__dict__ or c.__dict__[p] is None
                       for c in subclass.__mro__)
                   for p in ('path', 'comment', cls.read.__name__, cls.pipe.__name__)):
                return False
        return NotImplemented


def _Python_env(reader: Reader) -> _typing.Mapping[str, _typing.Any]:
    def cwf_section(section: str) -> _environment.util.Location:
        return _typing.cast(_environment.util.Location,
                            _environment.util.FileSection(
                                path=reader.path, section=section)
                            )
    return _types.MappingProxyType({
        'cwf': reader.path,
        'cwd': reader.path.parent,
        'cwf_section': cwf_section,
    })


class MarkdownReader:
    __slots__ = ('__path', '__codes', '__comment')
    builtins_exclude: _typing.AbstractSet[str] = frozenset(
        # constants: https://docs.python.org/library/constants.html
        # functions: https://docs.python.org/library/functions.html
    )
    start: str = f'```Python\n# {_globals.uuid} generate data'
    stop: str = '```'

    @property
    def path(self: _typing.Self) -> _pathlib.PurePath: return self.__path

    @property
    def comment(self: _typing.Self) -> bool: return self.__comment

    def __init__(self: _typing.Self, *,
                 path: _pathlib.PurePath,
                 comment: bool = True) -> None:
        self.__path: _pathlib.PurePath = path
        self.__codes: _typing.MutableSequence[_typing.Any] = []
        self.__comment: bool = comment

    def read(self: _typing.Self, text: str, /) -> None:
        start: int = text.find(self.start)
        while start != -1:
            stop: int = text.find(self.stop, start + len(self.stop))
            if stop == -1:
                raise ValueError(f'Unenclosure at char {start}')
            self.__codes.append(
                compile('\n' * text.count('\n', 0, start + len(self.start))
                        + text[start + len(self.start):stop],
                        filename=self.__path,
                        mode='exec',
                        flags=_ast.PyCF_ALLOW_TOP_LEVEL_AWAIT,
                        dont_inherit=True,
                        optimize=0)
            )
            start = text.find(self.start, stop + len(self.stop))

    def pipe(self: _typing.Self) -> _typing.Collection[_write.Writer]:
        vars: _typing.MutableMapping[str,
                                     _typing.Any] = _environment.__dict__.copy()
        vars['__builtins__'] = {
            k: v for k, v in _builtins.__dict__.items() if k not in self.builtins_exclude}
        env: _venv.Environment = _venv.Environment(
            env=_Python_env(_typing.cast(Reader, self)), globals=vars, locals=vars)

        def ret_gen() -> _typing.Iterator[_write.Writer]:
            code: _typing.Any
            for code in self.__codes:
                ret: _write.PythonWriter = _write.PythonWriter(
                    code, env=env, comment=self.__comment)
                assert isinstance(ret, _write.Writer)
                yield ret
        return tuple(ret_gen())


Reader.register(MarkdownReader)
assert issubclass(MarkdownReader, Reader)
Reader.registry['.md'] = MarkdownReader
