import typing as _typing

from .. import util as _util
from . import flashcard as _flashcard
from . import misc as _misc
from . import text_code as _text_code


def quote_text(code: _text_code.TextCode, /, *,
               tag: _misc.TagStr = _misc.Tag.COMMON) -> str:
    return _util.Unit(code)\
        .map(lambda code: _misc.code_to_str(code, tag=tag))\
        .map(lambda text: _misc.affix_lines(text, prefix='> '))\
        .map('\n'.__add__)\
        .counit()


def memorize_linked_seq(code: _text_code.TextCode, /, *,
                        hinted: _typing.Sequence[bool],
                        states: _typing.Iterable[str]) -> str:
    return _util.Unit(code)\
        .map(lambda code: _misc.code_to_strs(code, tag=_misc.Tag.MEMORIZE))\
        .map(lambda strs: _flashcard.memorize_linked_seq(strs, hinter=_flashcard.punctuation_hinter(hinted.__getitem__)))\
        .map(_flashcard.listify_flashcards)\
        .map(lambda text: _flashcard.attach_flashcard_states(text, states=states))\
        .map('\n'.__add__)\
        .counit()


def semantics_seq_map(text: _text_code.TextCode, sem: _text_code.TextCode, *,
                      states: _typing.Iterable[str]) -> str:
    return _util.Unit((text, sem))\
        .map(lambda codes: (
            _misc.code_to_strs(codes[0], tag=_misc.Tag.SEMANTICS),
            _misc.code_to_strs(codes[1], tag=_misc.Tag.SEMANTICS)
        ))\
        .map(lambda strss: zip(*strss, strict=True))\
        .map(_flashcard.semantics_seq_map)\
        .map(_flashcard.listify_flashcards)\
        .map(lambda text: _flashcard.attach_flashcard_states(text, states=states))\
        .map('\n'.__add__)\
        .counit()
