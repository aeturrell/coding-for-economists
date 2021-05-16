---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: 'Python 3.8.6 64-bit (''codeforecon'': conda)'
  language: python
  name: codeforecon
---

# Coming from Excel

Like it or loathe it, Microsoft's Excel spreadsheet programme is ubiquitous in our offices and homes. If you're looking to get off Excel, look no further because code can do everything Excel can-and a whole lot more!

The biggest difference between a fully-fledged programming language, such as Python, and a graphical tool for spreadsheet analysis is that you write out all of your instructions in code in the former, but only some instructions are written in code in the latter (such as cell formulae). Another big difference is that Python (and related tools like Visual Studio Code and git) are free!

The three main packages (extensions of the basic Python programming language) that cover Excel's functionality are **pandas**, which is for panel data analysis (such as spreadsheets). For some Excel functions, **numpy**, which provides tools for working with numbers, and **matplotlib**, which creates charts, will be necessary.

In this chapter, we'll focus on how to go from Excel to Python by *replacing* Excel. The situation where you want to work with Excel from Python (eg by populating a spreadsheet with data, formulae, and charts) will be covered in another chapter on automation.

## Excel <==> Python

To get started with Excel, you open the application and create a new empty file. To get started with Python, follow the instructions in the preliminaries chapter of this book and create a new script (a file ending in `.py`) in Visual Studio Code. You will also need to have the Python package **pandas** installed. The translations of common Excel tasks in the table below assume you have already run `import pandas as pd`, and that you have your data in a pandas dataframe called `df` (see the parts of this book on data analysis for more on using pandas). Although the table only covers a small fraction of what Excel does, and is certainly not comprehensive, it should give an idea of the ease and flexibility of **pandas** in replacing common Excel functions.

| Action | Excel      | Python (pandas) |
|-----| ----------- | ----------- |
|View data | Open the file using Excel  | `df.head(n)` to see the first n rows; use `df` to see all       |
|Count rows | Select a column with the mouse and look at the count indicator  | `df.count()`   |
| Find Sum, Average, Max, or Min of the 1st column | eg, `=SUM(A:A)`   | eg, `df.iloc[:, 0].sum()`. Other commands are `.mean()`, `.max()`, and `.min()`      |
| Perform an operation on, eg sum, on the first row | `=SUM(1:1)` | `df.iloc[0, :].sum()` |
| Count occurrences of distinct items within a column | See [here](https://superuser.com/questions/442653/ms-excel-how-to-count-occurrences-of-items-in-a-list) (complicated!) | `df['column_name'].value_counts()` |
| Return true or false given values in another column based on a condition | `=IF(A1<100, TRUE, FALSE)` etc, with 1 changing according to row | `df['new_column'] = df['column_name'] < 100` |
| Adding two columns | `= A1 + B1` etc, with 1 changing according to row | `df['new_column'] = df['column_A'] + df['column_B']` |
| Create a date column | Click on the column; select "Date" from list of number-format categories. | `df['column'] = pd.to_datetime(df['column'])` |
| Count days between two dates | `=DAYS(A1, B1)` with 1 changing according to row | `df['new_column'] = df['column_A'] - df['column_B']`, where both existing columns are datetimes |
| Create a cumulative sum on a column | `=SUM(A$1:A10)` where 10 is the maximum row index number | `df['new_columns'] = df['column'].cumsum()` |
| Concatenate string columns | `=CONCATENATE(A1,B1)` where 1 changes by row | `df['new_column'] = df['string_column_a'] + df['string_column_b']` |
| Find out which cells in a column have invalid entries | `=ISERROR(A1)` where 1 changes by row | `df['column'].notna()` |
| Remove excess whitespace | `=TRIM(A1)` where 1 changes by row | `df['new_column'] = df['column'].replace("\s+", " ", regex=True)` |
| Transpose data | `=TRANSPOSE(A1:C100)`, assuming a 3 by 100 input data set between columns A and C, and rows 1 to 100 | `df.T` |
| Create a pivot table | Manually select data and use the various menus (example [here](https://www.excel-easy.com/data-analysis/pivot-tables.html)) | `pd.pivot_table(df, values='D', index=['A'], columns=['C'], aggfunc=np.sum)` by summing over a column named 'D' with rows 'A', creating columns 'C' |

For more on how to replace Excel with Python and **pandas**, see the [Data Analysis Quickstart](data-quickstart) and [Data Analysis](data-analysis) sections.
