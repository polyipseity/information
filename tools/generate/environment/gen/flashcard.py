import itertools as _itertools
import typing as _typing
from . import misc as _misc


@_typing.final
class Flashcard:
    __slots__ = ('__left', '__right', '__reversible')

    @_typing.final
    class SeparatorKey(_typing.NamedTuple):
        reversible: bool
        multiline: bool
    separators: dict[SeparatorKey, str] = {
        SeparatorKey(reversible=False, multiline=False): '::',
        SeparatorKey(reversible=True, multiline=False): ':::',
        SeparatorKey(reversible=False, multiline=True): '\n??\n',
        SeparatorKey(reversible=True, multiline=True): '\n???\n',
    }

    def __init__(self: _typing.Self, left: str, right: str, *, reversible: bool = False) -> None:
        self.__left: str = left
        self.__right: str = right
        self.__reversible: bool = reversible

    def __repr__(self: _typing.Self) -> str:
        return f'{Flashcard.__qualname__}(left={self.__left!r}, right={self.__right!r}, reversible={self.__reversible!r})'

    def __str__(self: _typing.Self) -> str:
        return self.separators[self.SeparatorKey(
            reversible=self.__reversible,
            multiline='\n' in self.__left or '\n' in self.__right
        )].join((self.__left, self.__right))

    @property
    def left(self: _typing.Self) -> str: return self.__left

    @property
    def right(self: _typing.Self) -> str: return self.__right

    @property
    def reversible(self: _typing.Self) -> bool: return self.__reversible


def listify_flashcards(flashcards: _typing.Iterable[Flashcard])\
        -> str:
    def ret_gen() -> _typing.Iterator[str]:
        newline: str = ''
        for index, flashcard in enumerate(flashcards):
            yield newline
            yield str(index + 1)
            yield '. '
            yield str(flashcard)
            newline = '\n'
    return ''.join(ret_gen())


def attach_flashcard_states(text: str, /, *, states: _typing.Iterable[str]) -> str:
    def ret_gen() -> _typing.Iterator[str]:
        newline: str = ''
        for line, state in zip(text.splitlines(), _itertools.chain(states, _itertools.repeat(''))):
            yield newline
            yield line
            if state:
                yield ' '
                yield state
            newline = '\n'
    return ''.join(ret_gen())


def memorize_linked_seq(strs: _typing.Iterable[str], /, *,
                        reversible: bool = True,
                        hinter: _typing.Callable[[int, str], tuple[str, str]] = lambda idx, str_: ('→', '←'))\
        -> _typing.Iterator[Flashcard]:
    class HintedStr(_typing.NamedTuple):
        str_: str
        left: str
        right: str
    prev: HintedStr | None = None
    index: int
    str_: str
    for index, str_ in enumerate(strs):
        cur: HintedStr = HintedStr(str_, *hinter(index, str_))
        if prev is not None:
            yield Flashcard(prev.str_ + cur.left, prev.right + cur.str_, reversible=reversible)
        prev = cur


def semantics_seq_map(map: _typing.Iterable[tuple[str, str]], /, *,
                      reversible: bool = False)\
        -> _typing.Iterator[Flashcard]:
    for text, sem in map:
        yield Flashcard(text, sem, reversible=reversible)


def punctuation_hinter(hinted: _typing.Callable[[int], bool] = lambda _: True)\
        -> _typing.Callable[[int, str], tuple[str, str]]:
    def ret(index: int, str_: str) -> tuple[str, str]:
        if hinted(index):
            count: int = len(_misc.split_by_punctuations(str_))
            return (f'→{count}', f'{count}←')
        return ('→', '←')
    return ret
