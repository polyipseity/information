---
aliases:
  - Java file
  - Java files
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/file
  - language/in/English
---

# Java file

## path

To interact with a file, we need to first {@{get a path to the file}@}. This can be done {@{using `java.nio.file.Path` and `java.nio.file.Paths`}@}: <!--SR:!2027-12-10,1092,350!2028-01-29,1134,350-->

```Java
import java.nio.file.Path;
import java.nio.file.Paths;

Path path = Paths.get("aFileInTheProjectDirectory.txt");
Path path2 = Paths.get("C:\\Documents", "aFileNotInTheProjectDirectory.txt");
```

## file metadata

One can check whether {@{an __existing__ file}@} is readable or writeable using {@{`java.nio.file.Files.isReadable(path)` or `java.nio.file.Files.isWritable(path)` respectively}@}. <!--SR:!2027-11-17,1077,350!2027-01-11,808,330-->

## text files

One can read from or write to a text file using {@{`java.io.BufferedReader` or `java.io.BufferedWriter` respectively}@}. <!--SR:!2027-11-02,1066,350-->

### reading text files

Use {@{`java.nio.file.Files.newBufferedReader(path[, charset])` to read a text file}@}. For `charset`, if you leave it blank, {@{UTF-8 is used. You can use the system charset by passing `java.nio.charset.Charset.defaultCharset()`}@}. If needed, handle {@{exceptions reported by the above methods using methods in [error § catching exceptions](error.md#catching%20exceptions)}@}. <!--SR:!2026-05-06,617,330!2027-03-18,860,330!2027-03-28,865,330-->

To read a line, use {@{`reader.readLine()`, which returns `null` when the end of file has reached}@}. An example: <!--SR:!2025-10-26,462,330-->

```Java
String line;
while ((line = reader.readLine()) != null) {
  // do something with `line`
}
```

When done with reading, {@{close the reader to avoid locking the file by calling `reader.close()`}@}. A better method is {@{using `try...catch...finally`, and the best is using `try-with-resources`}@}, but they will not be mentioned here. <!--SR:!2025-03-06,308,330!2028-06-18,1245,350-->

### writing text files

Use {@{`java.nio.file.Files.newBufferedWriter(path[, charset[, options]])` to read a text file}@}. For `charset`, if you leave it blank, {@{UTF-8 is used. You can use the system charset by calling `java.nio.charset.Charset.defaultCharset()`}@}. For `options`, if you leave it blank, {@{`StandardOpenOption.WRITE` is used. It creates the file if not exist and empties the content. If appending to an existing file, use `StandardOpenOption.APPEND` instead}@}. If needed, handle {@{exceptions reported by the above methods using methods in [error § catching exceptions](error.md#catching%20exceptions)}@}. <!--SR:!2026-10-15,737,330!2026-02-20,520,310!2025-07-06,341,290!2026-12-18,786,330-->

To write something, use {@{`writer.write(string)`}@}. To write a newline, use {@{`writer.newLine()`}@}. An example: <!--SR:!2027-01-15,819,330!2028-08-31,1301,350-->

```Java
writer.write("Hello, world!");
writer.newLine();
```

When done with writing, {@{close the writer to save the file by calling `writer.close()`}@}. A better method is {@{using `try...catch...finally`, and the best is using `try-with-resources`}@}, but they will not be mentioned here. <!--SR:!2027-05-22,934,350!2028-08-08,1286,350-->
