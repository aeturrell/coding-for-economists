# coding-for-economists

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aeturrell/coding-for-economists/HEAD)

This readme is intended to help those contributing to or editing the book, not those trying to follow it. To read or use the book, head to the [coding for economists website](https://aeturrell.github.io/coding-for-economists/intro.html). You can use the book interactively via the following options:
- download pages to your computer as jupyter notebooks
- run pages in Google Colab through your browser
- run pages in Binder through your browser

## Setting up the environment

After installing env, activate, and use

```bash
python3.8 -m ipykernel install --user --name=codeforecon
```

to install a new ipykernel.

From a fresh install, it's recommended that you use **nbstripout** to avoid committing notebook outputs to github. Once pip installing the package, run `nbstripout --install --global` for installation within a given Python environment or `nbstripout --install --attributes .gitattributes` within the folder.

To build the book using Jupyter books use

```bash
jupyter-book build .
```

To ensure that Jupyter notebooks are running the correct kernel, open them in Jupyter notebook server and change the kernel there to 'codeforecon' and save it.

See [here](https://jupyterbook.org/publish/gh-pages.html) for how to upload revised HTML files.

The command is

```bash
ghp-import -n -p -f _build/html
```
