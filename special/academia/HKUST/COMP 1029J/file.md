---
aliases:
  - Java file
  - Java files
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/file
  - language/in/English
---

# Java file

## path

To interact with a file, we need to first {{get a path to the file}}. This can be done {{using `java.nio.file.Path` and `java.nio.file.Paths`}}: <!--SR:!2024-12-12,240,330!2024-12-20,249,330-->

```Java
import java.nio.file.Path;
import java.nio.file.Paths;

Path path = Paths.get("aFileInTheProjectDirectory.txt");
Path path2 = Paths.get("C:\\Documents", "aFileNotInTheProjectDirectory.txt");
```

## file metadata

One can check whether {{an __existing__ file}} is readable or writeable using {{`java.nio.file.Files.isReadable(path)` or `java.nio.file.Files.isWritable(path)` respectively}}. <!--SR:!2024-12-05,237,330!2024-04-20,61,310-->

## text files

One can read from or write to a text file using {{`java.io.BufferedReader` or `java.io.BufferedWriter` respectively}}. <!--SR:!2024-12-01,234,330-->

### reading text files

Use {{`java.nio.file.Files.newBufferedReader(path[, charset])` to read a text file}}. For `charset`, if you leave it blank, {{UTF-8 is used. You can use the system charset by passing `java.nio.charset.Charset.defaultCharset()`}}. If needed, handle {{exceptions reported by the above methods using methods in [error § catching exceptions](error.md#catching%20exceptions)}}. <!--SR:!2024-08-25,144,310!2024-04-21,62,310!2024-04-24,64,310-->

To read a line, use {{`reader.readLine()`, which returns `null` when the end of file has reached}}. An example: <!--SR:!2024-07-20,108,310-->

```Java
String line;
while ((line = reader.readLine()) != null) {
  // do something with `line`
}
```

When done with reading, {{close the reader to avoid locking the file by calling `reader.close()`}}. A better method is {{using `try...catch...finally`, and the best is using `try-with-resources`}}, but they will not be mentioned here. <!--SR:!2024-05-02,71,310!2024-04-22,62,310-->

### writing text files

Use {{`java.nio.file.Files.newBufferedWriter(path[, charset[, options]])` to read a text file}}. For `charset`, if you leave it blank, {{UTF-8 is used. You can use the system charset by calling `java.nio.charset.Charset.defaultCharset()`}}. For `options`, if you leave it blank, {{`StandardOpenOption.WRITE` is used. It creates the file if not exist and empties the content. If appending to an existing file, use `StandardOpenOption.APPEND` instead}}. If needed, handle {{exceptions reported by the above methods using methods in [error § catching exceptions](error.md#catching%20exceptions)}}. <!--SR:!2024-10-04,172,310!2024-09-18,168,310!2024-07-30,118,290!2024-04-23,62,310-->

To write something, use {{`writer.write(string)`}}. To write a newline, use {{`writer.newLine()`}}. An example: <!--SR:!2024-10-18,184,310!2024-04-27,67,310-->

```Java
writer.write("Hello, world!");
writer.newLine();
```

When done with writing, {{close the writer to save the file by calling `writer.close()`}}. A better method is {{using `try...catch...finally`, and the best is using `try-with-resources`}}, but they will not be mentioned here. <!--SR:!2024-10-30,205,330!2024-04-22,63,310-->
