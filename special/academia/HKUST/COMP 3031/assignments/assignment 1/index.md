---
aliases:
  - COMP3031 assignment 1
  - COMP 3031 assignment 1
  - HKUST COMP3031 assignment 1
  - HKUST COMP 3031 assignment 1
tags:
  - date/2025/10/02
  - flashcard/active/special/academia/HKUST/COMP_3031/assignments/assignment_1
  - language/in/English
---

# assignment 1

- HKUST COMP 3031

---

- title: Assignment 1: Trees
- due: 2025-10-02T23:59:59+08:00
- points: 10
- submitting: file upload
- file types: scala

---

- [`ass1.zip`](attachments/ass1.zip)

---

The goal of this assignment is to implement a minimal data structure for trees. The motivating example for such trees is a file system, which is represented as a tree of directories and files. Although we would be implementing a generic tree, it would still be instructive to think of the file system example.

Download the skeleton project at [ass1.zip](attachments/ass1.zip).

## Representation

The `Tree` type is parametrized by `K` and `V`, which stand for "key" and "value". Each node of a tree carries a key of type `K`.

We classify nodes of the tree into two disjoint kinds:

- _Internal nodes_ have a number \(possibly zero\) of children, which are themselves trees, with distinct keys among siblings. They are represented as the type `Tree.Node`. Their children are represented as a list of trees.
- _Leaves_ have a payload of type `V` attached. They are represented as the type `Tree.Leaf`.

Nodes are identified by their paths, i.e. the lists of ancestors from the root to them. Paths are represented as a `List` of `K`, wrapped inside the type `Tree.Path[K]`. Note that `Path[K]` represents a relative path from the current node.

- An empty `Path` represents the current node.
- Each segment in the `Path` represents a step down the tree hierarchy.

## Methods

For illustrative purpose, consider the following tree `t`:

```text
Node(, ...)
├── Node(foo, ...)
│   ├── Leaf(a, 1)
│   └── Leaf(b, 2)
└── Node(bar, ...)
    ├── Leaf(a, 11)
    └── Leaf(b, 12)
```

### `Tree.contains`

```Scala
def contains(path: Path[K]): Boolean
```

Returns `true` if the tree contains the path `path`, regardless of whether the path refers to an internal node or a leaf, and `false` otherwise.

### `Tree.get`

```Scala
def get(path: Path[K]): Option[Either[List[K], V]]
```

Optionally returns the content at the path `path`, wrapped in an `Either`. In other words:

- Returns a `None` if the tree does not contain `path`.
- Returns a `Some(Left(ls))` if `path` refers to an internal node with `children` as its children, where `ls` is a list containing the keys of the elements in `children`.
- Returns a `Some(Right(payload))` if `path` refers to a leaf with `payload` as its payload.

### `Tree.flatten`

```Scala
def flatten: List[(Path[K], V)]
```

Returns a list of pairs of paths and values of all leaves in the tree.

For example, `t.flatten` would return the following list:

```text
List(
    (Path(List(, foo, a)),1),
    (Path(List(, foo, b)),2),
    (Path(List(, bar, a)),11),
    (Path(List(, bar, b)),12)
)
```

<span style="color: #ba372a;">Note that the method produces _absolute paths_, which includes the key of the root node.</span>

### `Tree.updated`

The `Tree` class should implement two `updated` methods with the following signatures:

```Scala
def updated(path: Path[K]): Tree[K, V]
def updated(path: Path[K], payload: V): Tree[K, V]
```

These methods create a new tree with modifications based on the given relative path:

1. If the path is empty, replace the current node with
    - a new empty internal node \(for the first signature\);
    - a new leaf node with the given payload \(for the second signature\);
    - or throw `Tree.IllegalPathException` if the current node is root and payload is provided \(because root can only be a `Node` and can't be replaced with Leaf\).
2. For non-empty paths:
    - Traverse existing nodes along the path.
    - Create new internal nodes for missing segments.
    - Replace leaf nodes encountered before the end of the path with internal nodes.
3. At the end of the path:
    - Create a new empty internal node \(for the first signature\).
    - Create a new leaf node with the given payload \(for the second signature\).

#### Examples

The following are a few examples for the reference.

- `t.updated(Path(List("foo", "b", "c", "d")))` would return the following tree:

    ```text
    Node(, ...)
    ├── Node(foo, ...)
    │   ├── Leaf(a, 1)
    │   └── Node(b, ...)
    │       └── Node(c, ...)
    │           └── Node(d, ...)
    └── Node(bar, ...)
        ├── Leaf(a, 11)
        └── Leaf(b, 12)
    ```

- While `t.updated(Path(List("bar")))` would return:

    ```text
    Node(, ...)
    ├── Node(foo, ...)
    │   ├── Leaf(a, 1)
    │   └── Leaf(b, 2)
    └── Node(bar, ...)
    ```

- `t.updated(Path(List()))` would return:

    ```text
    Node(, ...)
    ```

- `t.updated(Path(List("foo", "b", "c", "d")), 42)` would return the following tree:

    ```text
    Node(, ...)
    ├── Node(foo, ...)
    │   ├── Leaf(a, 1)
    │   └── Node(b, ...)
    │       └── Node(c, ...)
    │           └── Leaf(d, 42)
    └── Node(bar, ...)
        ├── Leaf(a, 11)
        └── Leaf(b, 12)
    ```

- While `t.updated(Path(List("bar")), 0)` would return:

    ```text
    Node(, ...)
    ├── Node(foo, ...)
    │   ├── Leaf(a, 1)
    │   └── Leaf(b, 2)
    └── Leaf(bar, 0)
    ```

- `t.updated(Path(List()), 0)` would throw `Tree.IllegalPathException`.

### `Tree.display`

```Scala
def display: String
```

This method will serialize the tree structure into a string representation for easy visualization. The string representation shows the structure of the tree, including:

- distinction between internal nodes \(`Node`\) and leaves \(`Leaf`\),
- the key of each node \(`Node(key)`\),
- the value of each leaf \(`Leaf(key, value)`\), and
- the hierarchical relationship between nodes \(using [box drawing characters](https://en.wikipedia.org/wiki/Box-drawing_characters)\).

For example, `t.display` would produce the following output.

```text
Node()
├── Node(foo)
│   ├── Leaf(a, 1)
│   └── Leaf(b, 2)
└── Node(bar)
    ├── Leaf(a, 11)
    └── Leaf(b, 12)
```

#### Notes

1. The order of subtrees does not matter.
2. Serialize values by calling `.toString`.
3. Keys do not need to be quoted.
4. Trailing newlines are not necessary.
5. If you're using PowerShell on Windows and noticed that the box drawing characters become garbled text like `ΓöúΓöÇΓöÇ`. This is because the display encoding of PowerShell sessions is set to ASCII by default. The following solution might be helpful. Run the following command _BEFORE_ the sbt shell starts.

    ```PowerShell
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    ```

    Note that this is a display issue. In the test, the output is checked using string comparison. One can use the following Unicode escape to make the exact characters: "\\u251c" for "├"; "\\u2502" for "│"; "\\u2514" for "└"; "\\u2500" for "─".

## Companion object methods

The companion object provides a few constructors for `Tree`.

```Scala
def apply[K, V](key: K): Tree[K, V]
```

Constructs a tree with an empty internal node with key `key` as its root.

```Scala
def apply[K, V](path: Path[K]): Tree[K, V]
```

Constructs a tree with an empty internal node at path `path`. Throws `Tree.IllegalPathException` if called with an empty path.

```Scala
def apply[K, V](path: Path[K], payload: V): Tree[K, V]
```

Constructs a tree with a single leaf with payload `payload` at path `path`. Throws `Tree.IllegalPathException` if called with an empty path.

## A note on the order of lists

The order of children in the internal representation of `Node` does not matter, as seen by the `private` modifier in the cases of `Tree`, which forbids anyone outside the class from accessing underlying representations.

For functions returning lists, their orders also do not matter. We will only grade the contents of the lists.

## Tests

A few simple tests are provided in the test suite, but they are far from covering every cases. So you are encouraged to write your own tests to test your code!

## Submission

Submit `Tree.scala` only to the canvas assignment by __<span style="color: #ba372a;">2 Oct</span>__.

## Hint

For `Tree.updated`, one possible implementation would be to peek at the next segment in the path to determine which child to recurse on, which is quite easy to perform by pattern matching. Alternatively, you can also try to catch an exception, but this may not be the cleanest solution.

## FAQ

- __Writing tests to intercept an exception__
    To write a test in MUnit to intercept an exception, the type of the exception must be supplied as a type argument. Using `Tree.IllegalPathException` would not work, since it refers to the class `Tree.IllegalPathException`, which is not declared. To refer to the type of the object `Tree.IllegalPathException`, use `Tree.IllegalPathException.type` instead.

## submission

- file: [`submission.scala`](submission.scala)
  - filename: `Tree.scala`
  - source
    - [`submission/`](submission/)
    - [`submission/src/main/scala/ass1/Tree.scala`](submission/src/main/scala/ass1/Tree.scala)
