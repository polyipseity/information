"""Type stubs for jaraco.clipboard.

Platform-agnostic interface for clipboard operations:
- Text copy/paste (cross-platform)
- HTML copy/paste (Windows/Darwin)
- Image copy/paste (where supported)
"""

def copy_text(text: str) -> None:
    """Copy text to system clipboard."""
    ...

def paste_text() -> str:
    """Paste text from system clipboard."""
    ...

def copy_html(content: str) -> None:
    """Copy HTML to system clipboard."""
    ...

def paste_html() -> str:
    """Paste HTML from system clipboard.

    Returns the HTML fragment as a string.
    On Windows, returns wclip.get_html().fragment.
    On Darwin, returns richxerox.paste(format='html').
    """
    ...

def copy_image(image) -> None:
    """Copy image to system clipboard."""
    ...

def paste_image():
    """Paste image from system clipboard."""
    ...

# Aliases for backwards compatibility
copy = copy_text
paste = paste_text

__all__: list[str]
