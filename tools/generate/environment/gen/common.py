import re as _re
import typing as _typing

from .. import util as _util
from . import flashcard as _flashcard
from . import misc as _misc
from . import text_code as _text_code


class _MarkdownRegex(_typing.NamedTuple):
    regex: _re.Pattern[str]
    desugared: str


_markdown_regexes: _typing.Sequence[_MarkdownRegex] = (
    _MarkdownRegex(regex=_re.compile(r'\b__\B', flags=0),
                   desugared='<b u>'),
    _MarkdownRegex(regex=_re.compile(r'\B__(?:\b|$)', flags=0),
                   desugared='</b u>'),
    _MarkdownRegex(regex=_re.compile(r'\*\*\B', flags=0),
                   desugared='<b s>'),
    _MarkdownRegex(regex=_re.compile(r'\B\*\*', flags=0),
                   desugared='</b s>'),
    _MarkdownRegex(regex=_re.compile(r'\b_\B', flags=0),
                   desugared='<i u>'),
    _MarkdownRegex(regex=_re.compile(r'\B_(?:\b|$)', flags=0),
                   desugared='</i u>'),
    _MarkdownRegex(regex=_re.compile(r'\*\B', flags=0),
                   desugared='<i s>'),
    _MarkdownRegex(regex=_re.compile(r'\B\*', flags=0),
                   desugared='</i s>'),
)
_html_tag_regex: _re.Pattern[str] = _re.compile(r'<([^>]+)>', flags=0)


def quote_text(code: _text_code.TextCode, /, *,
               tag: _misc.TagStr = _misc.Tag.TEXT) -> str:
    return _util.Unit(code)\
        .map(lambda code: _misc.code_to_str(code, tag=tag))\
        .map(lambda text: _misc.affix_lines(text, prefix='> '))\
        .map(_misc.strip_lines)\
        .map('\n'.__add__)\
        .counit()


def memorize_linked_seq(code: _text_code.TextCode, /, *,
                        hinted: _typing.Sequence[bool],
                        states: _typing.Iterable[str],
                        sanitizer: _typing.Callable[[
                            str], str] = lambda str_: str_,
                        reversible: bool = True,) -> str:
    return _util.Unit(code)\
        .map(lambda code: _misc.code_to_strs(code, tag=_misc.Tag.MEMORIZE))\
        .map(lambda strs: _flashcard.memorize_linked_seq(strs,
                                                         reversible=reversible,
                                                         hinter=_flashcard.punctuation_hinter(
                                                             hinted.__getitem__, sanitizer=sanitizer)
                                                         ))\
        .map(_flashcard.listify_flashcards)\
        .map(lambda text: _flashcard.attach_flashcard_states(text, states=states))\
        .map(_misc.strip_lines)\
        .map('\n'.__add__)\
        .counit()


def semantics_seq_map(text: _text_code.TextCode, sem: _text_code.TextCode, *,
                      states: _typing.Iterable[str],
                      reversible: bool = False,) -> str:
    return _util.Unit((text, sem))\
        .map(lambda codes: (
            _misc.code_to_strs(codes[0], tag=_misc.Tag.SEMANTICS),
            _misc.code_to_strs(codes[1], tag=_misc.Tag.SEMANTICS)
        ))\
        .map(lambda strss: zip(*strss, strict=True))\
        .map(lambda map: _flashcard.semantics_seq_map(map, reversible=reversible))\
        .map(_flashcard.listify_flashcards)\
        .map(lambda text: _flashcard.attach_flashcard_states(text, states=states))\
        .map(_misc.strip_lines)\
        .map('\n'.__add__)\
        .counit()


def markdown_sanitizer(text: str) -> str:
    def get_and_remove_html_tags(text: str) -> tuple[str, _typing.AbstractSet[str]]:
        tags: _typing.MutableSet[str] = set()
        matches: _typing.MutableSequence[_re.Match[str]] = []

        stack: _typing.MutableSequence[_re.Match[str]] = []
        match: _re.Match[str]
        for match in _html_tag_regex.finditer(text):
            tag: str = match[1]
            if tag.startswith('/'):
                tag0: str = tag[1:]
                tags.add(tag0)
                if stack and stack[-1][1] == tag0:
                    matches.extend((stack.pop(), match))
            elif tag.endswith('/'):
                tag0: str = tag[:-1]
                tags.add(tag0)
                matches.append(match)
            else:
                tags.add(tag)
                stack.append(match)

        matches.sort(key=lambda match: match.start())

        def ret_gen() -> _typing.Iterator[str]:
            prev: int = 0
            match: _re.Match[str]
            for match in matches:
                yield text[prev:match.start()]
                prev = match.end()
            yield text[prev:]
        return (''.join(ret_gen()), frozenset(tags))

    tags: _typing.AbstractSet[str]
    text, tags = get_and_remove_html_tags(text)
    distingusher: str = '\0' * \
        (len(max(tags, key=lambda tag: len(tag), default='')) + 1)
    md_regex: _MarkdownRegex
    for md_regex in _markdown_regexes:
        suffix: str = '/>' if md_regex.desugared.endswith('/>') else\
            '>' if md_regex.desugared.endswith('>') else ''
        text = md_regex.regex.sub(f'{md_regex.desugared[:-len(suffix)]}{distingusher}{suffix}',
                                  text)
    text, _ = get_and_remove_html_tags(text)
    return text
