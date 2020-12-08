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

# Best practice in coding

In this chapter, you'll learn about best practice for coding. As you code, you'll be tempted to ignore these (we all are). But the truth is that they will *all* save you time in the long run, and future you will thank past you for sticking to them.


## Background

The validity of your research depends, to a frightening degree, on the quality of your code. There are many ways to write code and, over the years, software developers have worked out best practices that help to make writing, using, debugging, and reading code more fun, and to make the end product higher quality. (There's nothing worse than wading through someone's terrible code.)

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

Most programming languages have a style guide or at least some conventions.

![Code quality](https://imgs.xkcd.com/comics/code_quality.png)

## Do not repeat yourself (DRY)

The DRY principle is 'Every piece of knowledge or logic must have a single, unambiguous representation within a system.' Divide your code into re-usable pieces that you can call when and where you want. Don't write lengthy methods, but divide logic up into clearly differentiated chunks.

This saves having to repeat code, having no idea whether it's this or that version of the same function doing the work, and will help your debugging efforts no end.

Some practical ways to apply DRY in practice are to use functions, to put functions or code that needs to be executed multiple times by multiple different scripts into another script (eg called `utilities.py`) and then import it, and to think carefully if another way of writing your code would be more concise (yet still readable).

## Naming conventions

In Python, the naming convention for almost all objects is lower case separated by underscores, e.g. ‘this_is_a_script.py’. This style of naming is also known as snake case. There are different naming conventions though--[Allison Horst](https://twitter.com/allison_horst) made this fantastic cartoon of the different conventions that are in use.

![Different naming conventions](http://aeturrell.github.io/home/images/in_that_case.jpeg)

But good naming isn't just about following the conventions, it's also about giving objects names that are clear and useful. Instead of calling a variable that measures incomes `variable_one`, call it `income_measure`. Instead of calling a function that inverts a matrix `matrix_stuff`, call it `matrix_invert`. The better named your variables, the clearer your code will be--and the fewer comments you will need to write!

## Code comments

Code comments, extra information that is not executed when the code is run, can be added by a preceding hash character `# This is a comment`. Use code comments to provide extra contextual information that *isn't* conveyed by function and variable names.

## Code review

Perform code reviews. Give what you’ve done to a colleague and ask them to go through it line-by-line checking it works as intended. If they do this properly and don’t find any mistakes or issues then I’d be very surprised. Return the favour to magically become a better coder yourself.

## The Zen of Python

For a more poetic take on how to code, `import this` in your Python session.

```{code-cell} ipython3
import this
```

Finally, it's always good to start by choosing clarity over optimisation. Computation is cheap, brain time is not. If you really need to optimise, do it later when you’ve figured out where it will count.

## Review
...