"""Interactive helper for modular exponentiation experiments.

Exposes three modes (``a``, ``b``, and a generic default) that prompt
for base, exponent, modulus, and optional addend, then print the result.
"""

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()


def _pow(a: int, b: int, c: int, d: int = 0) -> int:
    """Return pow(a, b, c) + d."""
    return pow(a, b, c) + d


def a() -> None:
    """Prompt for base and exponent and compute pow(a, b, 100000000)."""
    a = int(input("a? ").strip())
    b = int(input("b? ").strip())
    print(_pow(a, b, 100000000))


def b() -> None:
    """Prompt for base and exponent and compute pow(a, b, 9999999) + 20000000."""
    a = int(input("a? ").strip())
    b = int(input("b? ").strip())
    print(_pow(a, b, 9999999, 20000000))


def default() -> None:
    """Prompt for all four parameters and compute pow(a, b, c) + d."""
    a = int(input("a? ").strip())
    b = int(input("b? ").strip())
    c = int(input("c? ").strip())
    d = int(input("d? ").strip() or "0")
    print(_pow(a, b, c, d))


def main() -> None:
    """Dispatch to mode a, b, or default based on user input."""
    m = input("m? ").strip()
    {
        a.__name__: a,
        b.__name__: b,
    }.get(m, default)()
    print(":)")


def __main__():
    """Thin wrapper calling main."""
    main()


if __name__ == "__main__":
    __main__()
