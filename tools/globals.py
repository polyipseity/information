import datetime as _datetime
import re as _re
import types as _types
import typing as _typing

uuid: str = '08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e'
open_options: _typing.Mapping[str, _typing.Any] = _types.MappingProxyType({
    'encoding': 'UTF-8', 'errors': 'strict', 'newline': None
})
flashcard_regex: _re.Pattern[str] = _re.compile(r'<!--SR:.*?-->', flags=0)
generate_comment: str = '<!-- Following content is generated at {now}. Any edits will be overridden! -->'
generate_comment_regex: _re.Pattern[str] = _re.compile(
    r'^<!-- Following content is generated at (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}). Any edits will be overridden! -->',
    flags=0
)
assert generate_comment_regex.search(
    generate_comment.format(
        now=_datetime.datetime.now().astimezone().isoformat())
)
