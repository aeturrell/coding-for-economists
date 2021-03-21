# coding-for-economists

This readme is intended to help those contributing to or editing the book, not those trying to follow it. To follow the book, head to the [coding for economists website](https://aeturrell.github.io/coding-for-economists/intro.html) and download the jupyter notebooks directly from the relevant page.

## Setting up the environment

After installing env, activate, and use

```bash
python3.8 -m ipykernel install --user --name=codeforecon
```

to install a new ipykernel.

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
