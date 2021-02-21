# coding-for-economists

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

## Other dependencies

(Not currently active due to latter bullet)

- Camelot on Ghostscript: `brew install ghostscript` (MacOS), or download the windows installer.
- Camelot on outdate sqlalchemy, can cause problems.
