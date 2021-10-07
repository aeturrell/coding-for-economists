# coding-for-economists

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aeturrell/coding-for-economists/HEAD)

This readme is intended to help those contributing to or editing the book, not those trying to follow it. To read or use the book, head to the [coding for economists website](https://aeturrell.github.io/coding-for-economists/intro.html). You can use the book interactively via the following options, all available via the link above:

- download pages to your computer as jupyter notebooks
- run pages in Google Colab through your browser
- run pages in Binder through your browser

## Dev

These instructions are only for developers working on the book.

### Setting up the Environment

In principle, the environment can be installed using

```bash
conda env create -f environment.yml
```

on the command line. **This takes a really, really long time to install**. Coding for Economists depends on a LOT of packages, which in turn have a lot of dependencies. 

Some extra assets associated with packages are required. You will need to run `python -m spacy download en_core_web_sm` to download the spacy model. There are also several models needed for nltk.

### Building the Book

To build the book using Jupyter books use

```bash
jupyter-book build .
```

Once this command is run, you should be able to look at the HTML files for the book locally on your computer.

Note that, due to package conflicts, several pages may not compile when taking this approach. One work around is to manually run troublesome notebooks and, when jupyter-book encounters a problem when executing them to build the book, it will pick up the notebook at the last point it was successfully manually executed. If you do have this problem, it may be that jupyter-book is not picking up the right jupyter kernel. You can look at installed kernels using `jupyter kernelspec list`.

### Uploading Built Files

See [here](https://jupyterbook.org/publish/gh-pages.html) for how to upload revised HTML files, but the key command is

```bash
ghp-import -n -p -f _build/html
```

To perform the pre-commit checks, use

```bash
pre-commit run --all-files
```

### Pre-commit

Pre-commit is currently configured to:

- check for large added files
- strip outputs from notebooks
- apply the [black](https://black.readthedocs.io/en/stable/) code formatter to .py and .ipnb scripts

If **black-nb** finds a pre-commit error that is difficult to diagnose, a tip is to convert it to a regular script to find the problem, using, for example,

```bash
jupytext --to py data-intro.ipynb
```

## Good to Know

If you get a

```bash
File "python3.8/site-packages/myst_nb/parser.py", line 139, in nb_to_tokens
    start_line = source_map[cell_index] if source_map else (cell_index + 1) * 10000
IndexError: list index out of range
```

error then it may be that the notebook metadata has gone awry. If you can isolate the notebook, you can refresh the metadata by running:

```bash
jupytext --to py bad_notebook.ipynb
jupytext --to notebook bad_notebook.py
```

This will overwrite the existing notebook!
