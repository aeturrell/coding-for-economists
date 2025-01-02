import subprocess
from typing import Literal

import toml


def bump_version(part: Literal["major", "minor", "patch"] = "patch") -> None:
    file_path = "pyproject.toml"

    with open(file_path, "r") as f:
        pyproject = toml.load(f)

    version = pyproject["project"]["version"]
    major, minor, patch = map(int, version.split("."))

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid part value. Choose 'major', 'minor', or 'patch'.")

    new_version = f"{major}.{minor}.{patch}"
    subprocess.run(
        [
            "uvx",
            "--from=toml-cli",
            "toml",
            "set",
            "--toml-path=pyproject.toml",
            "project.version",
            new_version,
        ]
    )

    print(f"Version bumped to {major}.{minor}.{patch}")


if __name__ == "__main__":
    bump_version()
