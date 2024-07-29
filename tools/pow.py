def _pow(a: int, b: int, c: int, d: int = 0) -> int:
    return pow(a, b, c) + d


def a() -> None:
    a = int(input("a? ").strip())
    b = int(input("b? ").strip())
    print(_pow(a, b, 100000000))


def b() -> None:
    a = int(input("a? ").strip())
    b = int(input("b? ").strip())
    print(_pow(a, b, 9999999, 20000000))


def default() -> None:
    a = int(input("a? ").strip())
    b = int(input("b? ").strip())
    c = int(input("c? ").strip())
    d = int(input("d? ").strip() or "0")
    print(_pow(a, b, c, d))


def main() -> None:
    m = input("m? ").strip()
    {
        a.__name__: a,
        b.__name__: b,
    }.get(m, default)()
    print(":)")


if __name__ == "__main__":
    main()
