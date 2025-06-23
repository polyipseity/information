---
aliases:
  - Java I/O
  - Java IO
  - Java input output
  - Java input/output
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/IO
  - language/in/English
---

# Java input/output

## output

One can print to stdout using {@{`System.out.print` and `System.out.println`}@}. The first one prints {@{the provided string as is while the second one also prints an additional newline}@}.

```Java
System.out.println("println");
System.out.print("print");
System.out.println("ing");
/* stdout
println
printing
*/
```

One can also print {@{numerical types, `char`s, `boolean`s, and even objects using `print` and `println`}@}. `println` can also be called {@{without arguments, in which case it simply prints a newline}@}.

To align output, a primitive way is {@{using the tab character `\t`, which usually aligns text in 8-character intervals}@}.

## input

While we can use {@{`System.in` directly}@}, it is easier to use {@{`java.util.Scanner` to read the input: `Scanner scanner = new Scanner(System.in);`}@}.

To ask the user for input, use {@{`String input = scanner.nextLine();`}@}. Since our constructed `Scanner` uses `System.in`, the code {@{blocks until the user has entered the input and pressed the enter key, and the input excluding the newline is returned and assigned to `input`}@}. if `next()` is used instead, the difference is {@{the returned string only contains the text just before the next delimiter \(by default spaces\)}@}. Any further `nextLine()` or `next()` {@{do not block and process the rest of the string after the delimiter as if the remaining string is inputted by the user}@}. This is true {@{until the rest of the string is all processed}@}.
