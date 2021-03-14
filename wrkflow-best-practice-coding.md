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

# Tips for Better Coding

In this chapter, you'll learn about some best practices for coding. **These will save you *so much time*!**. Trust me.

As you code, you'll be tempted to ignore these (that's normal; we all are). But the truth is that they will *save* time in the long run, and future you will thank past you for sticking to them.

The validity of your research depends, to a frightening degree, on the quality of your code. There are many ways to write code and, over the years, software developers have worked out best practices that help to make writing, using, debugging, and reading code more fun, and to make the end product higher quality. (There's nothing worse than wading through someone else's terrible code.)

![Code quality 2](https://imgs.xkcd.com/comics/code_quality_2.png)

Most of the time, you are going to be writing code for your co-authors or for future you. Following best practice will save you hours, and hours, and *hours* of time. You may think that by cutting out some of these practices that you'll save time. Well, it depends how heavily you discount your future time. Regardless of your discount rate, it's almost always worth it to follow best practices.

Fortunately there's lot of great advice, and even tools, to help you do this.

(Reproducibility is also an important part of coding best practice, but we'll talk about that in a later chapter. Likewise, I won't talk about a more advanced best practice, testing, here.)

## Code in style

The first thing to think about is code style, ie how you write equivalent valid code. Python has a whole set of conventions about good style called ['PEP8'](https://www.python.org/dev/peps/pep-0008/), which it's worth taking a quick look at. It includes advice like indentation should always be 4 spaces per level and to surround top-level function and class definitions with two blank lines.

Learning all of these would be tedious beyond belief. The good news is that a combination of packages and Visual Studio Code will do almost all of them for you!

Visual Studio Code can use a so-called 'linter' package to highlight any lines of your code that don't comply with PEP8. I use [**pycodestyle**](https://pypi.org/project/pycodestyle/). Once you've installed it and set it up in Visual Studio Code (Command Palette -> Python: Set Linter) you select some of your code in a script and hit Command+K, Command+F on Mac (Ctrl+K, Ctrl+F otherwise) and pycodestyle will automatically fix what it can.

You can go even further than just linting and allow all of your code to be restyled more dramatically using a 'code formatter'. I sometimes use [**black**](https://black.readthedocs.io/en/stable/) (you can have any code style you like, as long as it's black), which is very opinionated but great it you just want to forget about formatting your own code nicely.

To use **black**, install it according to the documentation. Then it runs from the command line, eg `black yourscript.py`. Here's an example of the kind of reformatting it does:

```python
# in:

def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        ...

# out:

def very_important_function(
    template: str,
    *variables,
    file: os.PathLike,
    engine: str,
    header: bool = True,
    debug: bool = False,
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        ...
```

To see more about black and how to use it, check out these [short video tutorials](https://calmcode.io/black/introduction.html).

Most programming languages have a style guide or at least some conventions.

![Code quality](https://imgs.xkcd.com/comics/code_quality.png)

## Do not repeat yourself (DRY)

The DRY principle is 'Every piece of knowledge or logic must have a single, unambiguous representation within a system.' Divide your code into re-usable pieces that you can call when and where you want. Don't write lengthy methods, but divide logic up into clearly differentiated chunks.

This saves having to repeat code, having no idea whether it's this or that version of the same function doing the work, and will help your debugging efforts no end.

Some practical ways to apply DRY in practice are to use functions, to put functions or code that needs to be executed multiple times by multiple different scripts into another script (eg called `utilities.py`) and then import it, and to think carefully if another way of writing your code would be more concise (yet still readable).

```{admonition} Tip
:class: tip
If you're using Visual Studio Code, you can [automatically send code into a function](https://code.visualstudio.com/docs/editor/refactoring) by right-clicking on code and using the 'Extract to method' option.
```

## Naming conventions

In Python, the naming convention for almost all objects is lower case separated by underscores, e.g. ‘this_is_a_script.py’. This style of naming is also known as snake case. There are different naming conventions though--[Allison Horst](https://twitter.com/allison_horst) made this fantastic cartoon of the different conventions that are in use.

![Different naming conventions](http://aeturrell.github.io/home/images/in_that_case.jpeg)
Artwork by @allison_horst.

But good naming isn't just about following the conventions, it's also about giving objects names that are clear and useful. Instead of calling a variable that measures incomes `variable_one`, call it `income_measure`. Instead of calling a function that inverts a matrix `matrix_stuff`, call it `matrix_invert`. The better named your variables, the clearer your code will be--and the fewer comments you will need to write!

For some quick shortcuts to re-naming columns in **pandas** dataframes or other string variables, try the unicode-friendly [**slugify**](https://github.com/un33k/python-slugify) library or the `clean_headers` function from the [**dataprep**](https://docs.dataprep.ai/index.html) library.

## Make it modular

Do not have a single file that does everything. If you split your code into separate, independent modules it will be easier to read, debug, test, and use. You can check the basics of coding chapter to see how to create and import functions from other scripts. But even within a script, you can still make your code modular by defining functions that have clear inputs and outputs.

A good rule of thumb is that if a code that achieves one end goes longer than about 30 lines, it should probably go into a function. Scripts longer than about 500 lines are ripe for splitting up too.

## Code comments

Code comments, extra information that is not executed when the code is run, can be added by a preceding hash character `# This is a comment`. Use code comments to provide extra contextual information that *isn't* conveyed by function and variable names.

Actually, well-written code needs *fewer* comments because it's more evidence what's going on. And it's tempting not to update comments even when code changes. So do comment, but see if you can make the code tell its own story first.

## Code review

Perform code reviews: give what you’ve done to a colleague and ask them to go through it line-by-line to check it works as intended. If they do this properly and don’t find any mistakes or issues then I’d be very surprised. Return the favour to magically become a better coder yourself.

## Use interoperable file formats

We'll talk much more about data in an upcoming chapter. For now, some basic pointers for the most common form of data: tabular data that's arranged in columns and rows.

First: **do not** store your data in Excel file formats. Ever. First, it's not an open format, it's proprietary, even if you can open it with many open source tools. Second, more importantly, Excel can do bad things like [changing the underlying values in your dataset](http://www.win-vector.com/blog/2014/11/excel-spreadsheets-are-hard-to-get-right/) (dates and booleans), and it tempts other users to start slotting Excel code around the data. This is bad - best practice is to **separate** code and data. Code hidden in Excel cells is not very transparent or auditable.

![jpg](https://pbs.twimg.com/media/D8z-M_dVUAA6NOh?format=jpg&name=medium)

If you want examples of what can go wrong using Excel, look no further than the famous [Reinhart and Rogoff Excel error](https://theconversation.com/the-reinhart-rogoff-error-or-how-not-to-excel-at-economics-13646_), where they didn't select all cells (it's harder to make this kind of mistake with real programming languages, though of course not impossible), the time when a first-year law associate [added an extra 179 contracts](https://www.abajournal.com/news/article/excel_error_by_a_cleary_gottlieb_associate_alters_lehman_asset_deal1) to an agreement to buy Lehman Brothers assets, or when the UK [under-counted the number](https://www.bbc.co.uk/news/technology-54423988) of coronavirus cases by *16,000* because their Excel spreedsheet wasn't big enough. In programming, the dataset limitation is the size of your computer's hard drive (and even then, you can jump onto the cloud).

In the majority of cases, the best data file format for your project is CSV--certainly for outputting final results. Everyone can open a CSV file, no matter what analytical tool or operating system they are using. As a storage format, it’s unlikely to change. Without going into the mire of [different encodings](http://kunststube.net/encoding/), save it with the UTF-8 encoding (note that this is not the default encoding in Windows).

Do not use Stata's .dta format for storing data, especially long term. For one thing, the format changes with the version of Stata. You do not want your data to depend on what version of software you're using! Second, it isn't very interoperable across tools (although you can use `pd.read_stata()` in Python). Third, it is not very efficient in the way that it uses disk space.

Although open source and compressed, I also don't recommend the statistical language R's RDS format or Python's pickle format, because neither are easily accessible from other tools. These are okay for intermediate data within a project that won't persist, but you could also use parquet for that, which is cross-platform.

And if you're working with big data, I *strongly* recommend the parquet file format. In most programming languages, it's [blazing fast](https://ursalabs.org/blog/2019-10-columnar-perf/) for input/output and packs down to a very efficient size. For example, a file saved in parquet might be 10 times smaller than the same .dta file; in tests, a 114 Mb parquet file was a whopping 4.68 GB in R's RDS format. If you're using cloud or have a small laptop, these space-savings add up. Better yet, parquet is available across a wide range of tools and languages including Python, R, Ruby, C++, Java, and Go. (Worth saying that parquet won't always be the right choice, but it's a great default for big data.)

## Use relative filepaths

A path, or filepath, is a slash-separated list of directory names followed by either a directory name or a file name. You'll use them to read data into code, for example using `df = pd.read_csv('path/to/data.csv')`. A directory is the same as a folder. On Unix based systems (Mac and Linux), these paths use forward slashes:

```shell
/Users/yourname/Documents/projects/file.csv
```

On Windows, which insists on being different, the slashes go the other way:

```shell
C:\Documents\projects\file.csv
```

These are *absolute paths*, that is they give the full information to go from a disk to the file. These are okay on your computer, but they are useless for replicability or for working with co-authors. It's much better in that case to use *relative paths*, where the path to a file is defined relative to a project folder. For example,

```shell
project_folder/data/raw/file.csv
```

Then, we use the convention that code executed for a project should have the project folder as its root directory, and any paths are relative to it. So to open `file.csv` using **pandas**, you would use

```python
import pandas as pd
df = pd.read_csv('data/raw/file.csv')
```

This works great on Mac and Linux, but it's not going to work on Windows. For that we need to use operating system independent paths. One way of doing this in Python is to use the `os` package that tells the operating system (whatever it may be) to combine folder names into a path:

```python
import pandas as pd
import os

path_to_data = os.path.join('data', 'raw', 'file.csv')
df = pd.read_csv(path_to_data)
```

## Don't prematurely optimise for speed

Make code correct and readable first, and fast second. You can waste a lot of time optimising only to find that either the bottleneck is not where you thought it was, or that you change your mind about what process needs to be done.

## Rubber duck your problems

Rubber duck debugging is a method of fixing code that isn't working as intended by, err, talking to a rubber duck. Something about describing your problem out loud and in detail can suddenly illuminate the issue to you and your plastic waterfowl friend.

![jpg](https://gitduck.com/blog/content/images/2019/10/IMG_7540.jpeg)

## The Zen of Python

For a more poetic take on how to code, `import this` in your Python session.

```{code-cell} ipython3
import this
```

Finally, it's always good to start by choosing clarity over optimisation. Computation is cheap, brain time is not. If you really need to optimise, do it later when you’ve figured out where it will count.

## Review

From this chapter, you should remember to

- ✅ follow a code style and use a linter;
- ✅ not repeat yourself;
- ✅ be consistent with your naming convention;
- ✅ write modular, well-documented code;
- ✅ use interoperable file formats;
- ✅ use relative file paths; and
- ✅ stay zen!
