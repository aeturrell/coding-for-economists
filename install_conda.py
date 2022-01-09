import yaml
import json
from subprocess import run
from rich import print
import subprocess
import sys
import argparse
import numpy as np


def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def conda_list(environment):
    proc = run(
        ["conda", "list", "--json", "--name", environment],
        text=True,
        capture_output=True,
    )
    return json.loads(proc.stdout)


def conda_install(environment, package, channel):
    proc = run(
        ["conda", "install", "--quiet", "-c", channel, "--name", environment, package],
        text=True,
        capture_output=True,
    )
    print(proc)


with open("environment.yml", "r") as stream:
    try:
        pkgs = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


pip_pkgs = pkgs["dependencies"][-1]["pip"]
cond_pkgs = pkgs["dependencies"][:-1]
cond_pkgs = [x for x in cond_pkgs if x.split("=")[0] != "python"]
channels = ["conda-forge" if x != "fastcore" else "fastai" for x in cond_pkgs]

num_pkg_map = dict(zip(range(len(cond_pkgs)), zip(cond_pkgs, channels)))
num_pkg_map.update(
    dict(
        zip(
            range(len(num_pkg_map), len(num_pkg_map) + len(pip_pkgs)),
            zip(pip_pkgs, ["pip"] * len(pip_pkgs)),
        )
    )
)

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("group", metavar="N", type=int, nargs="+", help="Group to run")

tot_num_groups = 10
nums_in_group = np.array_split(list(num_pkg_map.keys()), tot_num_groups)

if __name__ == "__main__":
    args = parser.parse_args()
    dict_entry_nums = nums_in_group[args.group[0]]
    for key, value in num_pkg_map.items():
        if key in dict_entry_nums:
            print(value)
            if value[1] == "pip":
                print("[red]pip installing  [/red]")
                pip_install(value[0])
            else:
                print("[blue]conda install[/blue]")
                conda_install("codeforecon", value[0], value[1])
