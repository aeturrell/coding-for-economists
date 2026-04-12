import glob

import nbformat

# Find all notebooks
notebooks = glob.glob("**/*.ipynb", recursive=True)

for nb_path in notebooks:
    if ".ipynb_checkpoints" in nb_path:
        continue

    with open(nb_path, "r", encoding="utf-8") as f:
        try:
            nb = nbformat.read(f, as_version=4)
            print(f"Fixing {nb_path}...")

            # Wipe and replace kernelspec
            nb.metadata["kernelspec"] = {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3",
            }

            # Wipe language_info version (this prevents the 3.10.17 mismatch)
            if "language_info" in nb.metadata:
                nb.metadata["language_info"]["version"] = "3"

            with open(nb_path, "w", encoding="utf-8") as f_out:
                nbformat.write(nb, f_out)
        except Exception as e:
            print(f"Could not process {nb_path}: {e}")

print("Successfully standardized all notebooks.")
