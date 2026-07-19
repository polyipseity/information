"""Wikipedia HTML-to-Markdown converter package.

Re-exports all public and private symbols so that ``from scripts import
convert_wiki as _mod`` and then ``_mod._symbol_name`` works as it did
when the module was monolithic.
"""

# isort: skip_file

# Re-export from bs4 (was module-level in the monolithic file)
from bs4 import BeautifulSoup  # noqa: F401

# Re-export from pyarchivist (was module-level in the monolithic file)
from pyarchivist import Args  # noqa: F401
from pyarchivist.Wikimedia_Commons import archive as pyarchivist_archive  # noqa: F401

# Config / constants
from .config import (  # noqa: F401
    AUTHORS,
    BASE_NAME,
    NAME,
    USER_AGENT,
    VERSION,
    __all__,
    _API_BACKOFF_MULTIPLIER,
    _API_INITIAL_BACKOFF,
    _API_MAX_BACKOFF,
    _API_MAX_RETRIES,
    _API_MAX_TITLES_PER_REQUEST,
    _ARCHIVE_REGEXES,
    _BAD_CHARACTERS,
    _BAD_TITLES,
    _build_names_map,
    _CACHE_TTL,
    _COMMONS_HOST_URL,
    _CONVERTED_WIKI_DIRECTORY,
    _CONVERTED_WIKI_LANGUAGE_DIRECTORY,
    _DATA_DIRECTORY,
    _IGNORED_NAME_PREFIXES,
    _LIST_INDENT,
    _MARKDOWN_ESCAPE_REGEX,
    _MARKDOWN_SEPARATOR_CHARACTERS,
    _MAX_CONCURRENT_REQUESTS_PER_HOST,
    _NAMES_MAP,
    _NAMES_MAP_NAME,
    _PAGE_DOES_NOT_EXIST_SUFFIX,
    _PRESERVED_PAGE_PREFIXES,
    _REDIRECT_CACHE_PATH,
    _SCRIPT_DIRECTORY,
    _WIKI_HOST_URL,
    _with_cwd,
)

# Types
from .types import _RedirectInfo  # noqa: F401

# Utilities
from .utils import (  # noqa: F401
    _balance_brackets,
    _bs4_new_element,
    _create_redirect_symlinks,
    _fix_filename,
    _fix_name_maybe,
    _get_image_filename,
    _markdown_fragment,
    _markdown_link_target,
    _pad_table_blocks,
    _tag_affixes,
)

# API / network helpers
from .api import (  # noqa: F401
    _api_request,
    _collect_image_filenames,
    _collect_link_titles,
    _load_redirect_cache,
    _resolve_redirects,
    _save_redirect_cache,
)

# Converter
from .converter import (  # noqa: F401
    WikiHtmlConverter,
    _HEADER_REGEX,
    _MARKDOWN_SEPARATOR,
)

# Pipeline
from .pipeline import (  # noqa: F401
    run_pipeline,
    wiki_html_to_plaintext,
)
