import re
import sys
from typing import Literal


def bump_version(
    part: Literal["major", "minor", "patch"] = "patch",
    dev_suffix: str | None = None,
) -> None:
    file_path = "pyproject.toml"

    with open(file_path, "r") as f:
        content = f.read()

    match = re.search(r'^version = "([^"]+)"', content, re.MULTILINE)
    if not match:
        raise RuntimeError("Could not find version in pyproject.toml")

    base = re.match(r"(\d+)\.(\d+)\.(\d+)", match.group(1))
    if not base:
        raise RuntimeError(f"Unexpected version format: {match.group(1)}")

    major, minor, patch_v = map(int, base.groups())

    if part == "major":
        major += 1
        minor = 0
        patch_v = 0
    elif part == "minor":
        minor += 1
        patch_v = 0
    elif part == "patch":
        patch_v += 1
    else:
        raise ValueError("Invalid part value. Choose 'major', 'minor', or 'patch'.")

    new_version = f"{major}.{minor}.{patch_v}"
    if dev_suffix:
        new_version = f"{new_version}.dev.{dev_suffix}"

    new_content = re.sub(
        r'^version = "[^"]+"',
        f'version = "{new_version}"',
        content,
        count=1,
        flags=re.MULTILINE,
    )
    with open(file_path, "w") as f:
        f.write(new_content)

    print(f"Version bumped to {new_version}")


if __name__ == "__main__":
    dev_suffix = sys.argv[1] if len(sys.argv) > 1 else None
    bump_version("patch", dev_suffix)
