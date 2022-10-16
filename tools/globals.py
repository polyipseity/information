import types as _types
import typing as _typing

uuid: str = '08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e'
open_options: _typing.Mapping[str, _typing.Any] = _types.MappingProxyType({
    'encoding': 'UTF-8', 'errors': 'strict', 'newline': None
})
flashcard_regex: str = r'<!--SR:.*?-->'
generate_comment: str = '<!-- Following content is generated at {now}. Any edits will be overridden! -->'
