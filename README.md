# coding-for-economists

After installing env, activate, and use

```bash
python -m ipykernel install --user --name=codeforecon
```

to install new ipykernel.

To ensure that Jupyter notebooks are running the correct kernel, open them in Jupyter notebook server and change the kernel there to 'codeforecon' and save it.

See [here](https://jupyterbook.org/publish/gh-pages.html) for how to upload revised HTML files.

The command is

```bash
ghp-import -n -p -f _build/html
```

## Other dependencies

- Camelot on Ghostscript: `brew install ghostscript` (MacOS), or download the windows installer.
