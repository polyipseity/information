
import types as _types
import typing as _typing


@_typing.final
class Environment:
    __slots__ = ('__env', '__globals', '__locals')

    def __init__(self: _typing.Self, *,
                 env: _typing.Mapping[str, _typing.Any] = {},
                 globals: _typing.Mapping[str, _typing.Any] = globals(),
                 locals: _typing.Mapping[str, _typing.Any] = locals()) -> None:
        self.__env: _typing.Mapping[str, _typing.Any] = _types.MappingProxyType(
            dict(env))
        self.__globals: _typing.Mapping[str, _typing.Any] = _types.MappingProxyType(
            dict(globals))
        self.__locals: _typing.Mapping[str, _typing.Any] = _types.MappingProxyType(
            dict(locals))
        assert '__env__' not in self.__locals

    def __repr__(self: _typing.Self) -> str:
        return f'{Environment.__qualname__}(env={self.__env!r}, globals={self.__globals!r}, locals={self.__locals!r})'

    @property
    def env(self: _typing.Self) -> _typing.Mapping[str, _typing.Any]:
        return self.__env

    @property
    def globals(self: _typing.Self) -> _typing.Mapping[str, _typing.Any]:
        return self.__globals

    @property
    def locals(self: _typing.Self) -> _typing.Mapping[str, _typing.Any]:
        return self.__locals

    def exec(self: _typing.Self, code: _typing.Any) -> _typing.Any:
        env = _types.SimpleNamespace()
        env.result = None
        env.__dict__.update(self.__env)
        locals: _typing.MutableMapping[str, _typing.Any] = dict(self.__locals)
        locals['__env__'] = env
        exec(code, dict(self.__globals), locals)
        return locals['__env__'].result
