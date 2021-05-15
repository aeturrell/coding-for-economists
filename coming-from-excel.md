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

The three main packages (extensions of the basic Python programming language) that cover Excel's functionality are **pandas**, which is for panel data analysis (such as spreadsheets), **numpy**, which provides tools for working with numbers, and **matplotlib**, which creates charts.

In this chapter, we'll focus on how to go from Excel to Python by *replacing* Excel. The situation where you want to work with Excel from Python (eg by populating a spreadsheet with data, formulae, and charts) will be covered in another chapter on automation.

## Excel <==> Python

To get started with Excel, you open the application and create a new empty file. To get started with Python, follow the instructions in the preliminaries chapter of this book and create a new script (a file ending in `.py`) in Visual Studio Code.
