---
aliases:
  - Excel object
  - Excel objects
tags:
  - flashcard/special/academia/HKUST/COMP_1029V/Excel_object
  - language/in/English
---

# Excel object

## common objects

### `Range`

The `Range` object can refer to {{a cell or a range}}. We can pass {{a cell reference, a range reference, or even a user-defined name: `Range(reference)`, such as `Range("C3")`, `Range("A2:B5")`, `Range("UserDefinedName")`}}. By default, the worksheet the range is on is {{the currently active worksheet}}. <!--SR:!2024-12-18,246,330!2024-05-05,73,310!2024-04-26,65,310-->

### `Cells`

The `Cells` object can refer to {{a cell}}. We pass {{the 1-based row and the 1-based column in order: `Cells(row, column)`, such as `Cells(2, 1)`}}. By default, the worksheet the cell is on is {{the currently active worksheet}}. <!--SR:!2024-04-18,58,310!2024-08-07,124,290!2024-10-05,173,310-->

### `Worksheets`

The `Worksheets` object can refer to {{a worksheet}}. We get a worksheet {{by name: `Worksheets(name)`, such as `Worksheets("Sheet1")`}}. We can also access `Range` and `Cells` in a specific worksheet by accessing them under the `Worksheets` object, like {{`Worksheets("Sheet1").Range("A1")`}}. <!--SR:!2024-04-25,64,310!2024-10-09,175,310!2024-09-09,154,310-->

One can make a worksheet active using {{the `Activate` method, like `Worksheets("My Potential").Activate`}}. <!--SR:!2024-05-05,48,270-->

## selection

You can get the currently selected cell or range using {{`Selection`}}. You can change the currently selected cell or range by doing {{`CellOrRange.Select`. Note that the worksheet the cell or range is on must be active, otherwise you get an error}}. <!--SR:!2024-05-02,23,290!2024-09-21,163,310-->
