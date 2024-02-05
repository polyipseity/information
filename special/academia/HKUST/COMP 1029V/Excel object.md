---
aliases:
  - Excel object
  - Excel objects
tags:
  - flashcards/special/academia/HKUST/COMP_1029V/Excel_object
  - languages/in/English
---

# Excel object

## common objects

### `Range`

The `Range` object can refer to {{a cell or a range}}. We can pass {{a cell reference, a range reference, or even a user-defined name: `Range(reference)`, such as `Range("C3")`, `Range("A2:B5")`, `Range("UserDefinedName")`}}. By default, the worksheet the range is on is {{the currently active worksheet}}. <!--SR:!2024-02-19,14,290!2024-02-22,17,290!2024-02-21,16,290-->

### `Cells`

The `Cells` object can refer to {{a cell}}. We pass {{the row and the column in order: `Cells(row, column)`, such as `Cells(2, 1)`}}. By default, the worksheet the cell is on is {{the currently active worksheet}}. <!--SR:!2024-02-20,15,290!2024-02-16,11,270!2024-02-19,14,290-->

### `Worksheets`

The `Worksheets` object can refer to {{a worksheet}}. We get a worksheet {{by name: `Worksheets(name)`, such as `Worksheets("Sheet1")`}}. We can also access `Range` and `Cells` in a specific worksheet by accessing them under the `Worksheets` object, like {{`Worksheets("Sheet1").Range("A1")`}}. <!--SR:!2024-02-21,16,290!2024-02-20,15,290!2024-02-18,13,290-->

One can make a worksheet active using {{the `Activate` method, like `Worksheets("My Potential").Activate`}}. <!--SR:!2024-02-22,17,290-->

## selection

You can get the currently selected cell or range using {{`Selection`}}. You can change the currently selected cell or range by doing {{`CellOrRange.Select`. Note that the worksheet the cell or range is on must be active, otherwise you get an error}}. <!--SR:!2024-02-18,13,290!2024-02-19,14,290-->
