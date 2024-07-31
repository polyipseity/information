_PREFIX, _SUFFIX = "<!--SR:!", "-->"


def main():
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


if __name__ == "__main__":
    main()
