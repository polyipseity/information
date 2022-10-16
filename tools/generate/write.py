import abc as _abc
import datetime as _datetime
import types as _types
import typing as _typing

from .. import globals as _globals
from . import environment as _environment
from . import venv as _venv


class Writer(metaclass=_abc.ABCMeta):
    __slots__ = ()

    @_abc.abstractmethod
    def write(self: _typing.Self) -> None: ...

    @classmethod
    def __subclasshook__(cls: type[_typing.Self], subclass: type) -> bool | _types.NotImplementedType:
        if cls is Writer:
            if any(all(p not in c.__dict__ or c.__dict__[p] is None
                       for c in subclass.__mro__)
                   for p in (cls.write.__name__,)):
                return False
        return NotImplemented


class PythonWriter:
    __slots__ = ('__code', '__env')

    def __init__(self: _typing.Self,
                 code: _typing.Any, /, *,
                 env: _venv.Environment) -> None:
        self.__code: _typing.Any = code
        self.__env: _venv.Environment = env

    def __repr__(self: _typing.Self) -> str:
        return f'{PythonWriter.__qualname__}({self.__code!r}, env={self.__env!r})'

    def write(self: _typing.Self) -> None:
        result0: _typing.Any = self.__env.exec(self.__code)
        if not isinstance(result0, _typing.Iterable):
            raise TypeError(result0)
        result1: _typing.Iterable[_typing.Any] = result0
        del result0
        result2: _typing.Collection[_typing.Any] = tuple(result1)
        del result1
        if any(not isinstance(ret, _environment.result.Result) for ret in result2):
            raise TypeError(result2)
        results: _typing.Collection[_environment.result.Result] = result2
        del result2

        result: _environment.result.Result
        for result in results:
            io: _typing.TextIO
            with result.location.open() as io:
                io.write(_globals.generate_comment.format(
                    now=_datetime.datetime.now().astimezone().isoformat()))
                io.write(result.text)
                io.truncate()


Writer.register(PythonWriter)
assert issubclass(PythonWriter, Writer)
