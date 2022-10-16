import abc as _abc
import ast as _ast
import builtins as _builtins
import pathlib as _pathlib
import types as _types
import typing as _typing

from .. import globals as _globals
from .. import util as _util
from . import environment as _environment
from . import venv as _venv
from . import write as _write


class Reader(metaclass=_abc.ABCMeta):
    registry: dict[str, type] = {}
    __slots__ = ()

    @_abc.abstractmethod
    def __init__(self: _typing.Self, *,
                 path: _pathlib.PurePath) -> None: ...

    @_abc.abstractmethod
    def read(self: _typing.Self, text: str, /) -> None: ...

    @_abc.abstractmethod
    def pipe(self: _typing.Self) -> _typing.Collection[_write.Writer]: ...

    @classmethod
    def __subclasshook__(cls: type[_typing.Self], subclass: type) -> bool | _types.NotImplementedType:
        if cls is Reader:
            if any(all(p not in c.__dict__ or c.__dict__[p] is None
                       for c in subclass.__mro__)
                   for p in (cls.read.__name__, cls.pipe.__name__)):
                return False
        return NotImplemented


class MarkdownReader:
    __slots__ = ('__path', '__codes')
    builtins_exclude: frozenset[str] = frozenset(
        # constants: https://docs.python.org/library/constants.html
        # functions: https://docs.python.org/library/functions.html
    )
    start: str = f'```Python\n# {_globals.uuid} generate data'
    stop: str = '```'

    def _env(self: _typing.Self) -> dict[str, _typing.Any]:
        def relative_path(path: _util.StrPath) -> _pathlib.PurePath:
            return self.__path / path
        return {
            'relative_path': relative_path,
        }

    def __init__(self: _typing.Self, *,
                 path: _pathlib.PurePath) -> None:
        self.__path: _pathlib.PurePath = path
        self.__codes: _typing.MutableSequence[_typing.Any] = []

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
        vars: dict[str, _typing.Any] = _environment.__dict__.copy()
        vars['__builtins__'] = {
            k: v for k, v in _builtins.__dict__.items() if k not in self.builtins_exclude}
        env: _venv.Environment = _venv.Environment(
            env=self._env(), globals=vars, locals=vars)

        def ret_gen() -> _typing.Iterator[_write.Writer]:
            code: _typing.Any
            for code in self.__codes:
                ret: _write.PythonWriter = _write.PythonWriter(code, env=env)
                assert isinstance(ret, _write.Writer)
                yield ret
        return tuple(ret_gen())


Reader.register(MarkdownReader)
assert issubclass(MarkdownReader, Reader)
Reader.registry['.md'] = MarkdownReader
