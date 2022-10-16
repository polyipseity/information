import enum as _enum
import io as _io
import types as _types
import typing as _typing


@_typing.final
class TextCode:
    __slots__ = ('__blocks', '__by_tag')

    @_typing.final
    class Block:
        __slots__ = ('__tag', '__text')

        def __init__(self: _typing.Self, text: str, *, tag: str = '') -> None:
            self.__tag: str = tag
            self.__text: str = text

        def __repr__(self: _typing.Self) -> str:
            return f'{TextCode.Block.__qualname__}(text={self.__text!r}, tag={self.__tag!r})'

        @property
        def tag(self: _typing.Self) -> str: return self.__tag

        @property
        def text(self: _typing.Self) -> str: return self.__text

        @property
        def special(self: _typing.Self) -> bool: return bool(self.__tag)

        @property
        def common(self: _typing.Self) -> bool: return not self.special

    @_typing.final
    class ByTagValue(_typing.NamedTuple):
        idx: int
        block: 'TextCode.Block'

    def __init__(self: _typing.Self, blocks: _typing.Iterable[Block]) -> None:
        self.__blocks: _typing.Sequence[TextCode.Block] = tuple(blocks)
        by_tag: dict[str, _typing.MutableSequence[TextCode.ByTagValue]] = {}
        for idx, block in enumerate(self.__blocks):
            by_tag.setdefault(block.tag, []).append(
                TextCode.ByTagValue(idx=idx, block=block))
        self.__by_tag: dict[str, _typing.Sequence[TextCode.ByTagValue]] = {
            k: tuple(v) for k, v in by_tag.items()}

    def __repr__(self: _typing.Self) -> str:
        return f'{TextCode.Block.__qualname__}(blocks={self.__blocks!r})'

    @property
    def blocks(
        self: _typing.Self) -> _typing.Sequence[Block]: return self.__blocks

    @property
    def by_tag(self: _typing.Self) -> _types.MappingProxyType[str, _typing.Sequence[ByTagValue]]:
        return _types.MappingProxyType(self.__by_tag)

    @staticmethod
    def compiler(code: str) -> _typing.Iterator[Block]:
        @_enum.unique
        class State(_enum.Enum):
            NORMAL = _enum.auto()
            ESCAPE = _enum.auto()
            TAG = _enum.auto()
            BLOCK = _enum.auto()
        state: State = State.NORMAL
        stack: _typing.MutableSequence[_io.StringIO | State] = []
        stack.append(_io.StringIO())
        for index, char in enumerate(code + '{}' if not code.endswith('}') or code.endswith('{}') else code):
            if state == State.NORMAL:
                if char == '\\':
                    stack.append(state)
                    state = State.ESCAPE
                elif char == '{':
                    text: _io.StringIO = _typing.cast(_io.StringIO, stack[-1])
                    text0: str = text.getvalue()
                    if text0:
                        yield TextCode.Block(text0)
                        text.seek(0)
                        text.truncate()
                    stack.append(_io.StringIO())
                    state = State.TAG
                elif char == '}':
                    raise ValueError(f'Unexpected char at {index}: {code}')
                else:
                    _typing.cast(_io.StringIO, stack[-1]).write(char)
            elif state == State.ESCAPE:
                prev_state: State = _typing.cast(State, stack.pop())
                _typing.cast(_io.StringIO, stack[-1]).write(char)
                state = prev_state
            elif state == State.TAG:
                if char == '\\':
                    stack.append(state)
                    state = State.ESCAPE
                elif char == '{':
                    raise ValueError(f'Unexpected char at {index}: {code}')
                elif char == ':':
                    stack.append(_io.StringIO())
                    state = State.BLOCK
                elif char == '}':
                    text: _io.StringIO = _typing.cast(
                        _io.StringIO, stack.pop())
                    if text.getvalue():
                        raise ValueError(f'Unexpected char at {index}: {code}')
                    state = State.NORMAL
                else:
                    _typing.cast(_io.StringIO, stack[-1]).write(char)
            elif state == State.BLOCK:
                if char == '\\':
                    stack.append(state)
                    state = State.ESCAPE
                elif char == '{' or char == ':':
                    raise ValueError(f'Unexpected char at {index}: {code}')
                elif char == '}':
                    text: _io.StringIO = _typing.cast(
                        _io.StringIO, stack.pop())
                    tag: _io.StringIO = _typing.cast(_io.StringIO, stack.pop())
                    yield TextCode.Block(text.getvalue(), tag=tag.getvalue())
                    state = State.NORMAL
                else:
                    _typing.cast(_io.StringIO, stack[-1]).write(char)
            else:
                raise ValueError(f'Unexpected state "{state}": {code}')

    @classmethod
    def compile(cls: type[_typing.Self], text: str) -> _typing.Self:
        return cls(cls.compiler(text))
