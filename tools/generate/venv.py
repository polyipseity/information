
import types as _types
import typing as _typing


@_typing.final
class Environment:
    __slots__ = ('__env', '__globals', '__locals')

    def __init__(self: _typing.Self, *,
                 env: dict[str, _typing.Any] = {},
                 globals: dict[str, _typing.Any] = globals(),
                 locals: dict[str, _typing.Any] = locals()) -> None:
        assert '__env__' not in locals
        self.__env: dict[str, _typing.Any] = env.copy()
        self.__globals: dict[str, _typing.Any] = globals.copy()
        self.__locals: dict[str, _typing.Any] = locals.copy()

    def __repr__(self: _typing.Self) -> str:
        return f'{Environment.__qualname__}(env={self.__env!r}, globals={self.__globals!r}, locals={self.__locals!r})'

    @property
    def env(self: _typing.Self) -> dict[str, _typing.Any]:
        return self.__env.copy()

    @property
    def globals(self: _typing.Self) -> dict[str, _typing.Any]:
        return self.__globals.copy()

    @property
    def locals(self: _typing.Self) -> dict[str, _typing.Any]:
        return self.__locals.copy()

    def exec(self: _typing.Self, code: _typing.Any) -> _typing.Any:
        env = _types.SimpleNamespace()
        env.result = None
        env.__dict__.update(self.__env)
        locals: dict[str, _typing.Any] = self.__locals.copy()
        locals['__env__'] = env
        exec(code, self.__globals, locals)
        return locals['__env__'].result
