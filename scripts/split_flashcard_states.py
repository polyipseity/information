"""Split a combined flashcard state annotation string into individual per-card annotations."""

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

_PREFIX, _SUFFIX = "<!--SR:!", "-->"


def main():
    """Read a flashcard state string from stdin and print each state on its own line."""
    flashcard_states_string = (
        input("? ").strip().removeprefix(_PREFIX).removesuffix(_SUFFIX)
    )
    print(
        "\n".join(
            f"{_PREFIX}{fc_state}{_SUFFIX}"
            for fc_state in filter(
                None, map(str.strip, flashcard_states_string.split("!"))
            )
        )
    )
    print(":)")


def __main__():
    """Entry point for running the script directly."""
    main()


if __name__ == "__main__":
    __main__()
