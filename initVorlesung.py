# TODO:
# - Online auf Github stellen


from glob import glob
from os.path import isdir
from os import mkdir
from typing import Final
from pathlib import Path
import json


JSONFILENAME: Final[str] = "vorlesung_counter.json"


def createVorlesung(parentDirectory: str) -> None:
    #  1. Get count in vorlesung_counter.json
    counters: dict[str, int] = json.load(open(JSONFILENAME, ))
    if parentDirectory not in counters.keys():
        raise KeyError("The given directory doesn't exist")
    if len(counters.keys()) == 0:
        raise IOError(f"The {JSONFILENAME} file is empty. Write it manually")
    counters[parentDirectory] += 1
    mkdir(rf"{parentDirectory}\Vorlesung {counters[parentDirectory]}")

    # 2. Overwrite because of raised counter
    print(f"{counters=}")
    json.dump(counters, open(JSONFILENAME, "w"))


def main():
    try:#to read the ignore file
        IGNOREFILE: Final[str] = open(".vorlesung.ignore", "r").read()
    except FileNotFoundError:
        pass # All of the directories will be selectable

    DirectoriesToIgnore: list[str] = [path for path in IGNOREFILE.split("\n")]
    AllDirectories: list[str] = []
    for directory in glob("*"):
        if isdir(directory) and directory not in DirectoriesToIgnore:
            AllDirectories.append(directory)

    print("Select the number of the directory to create the new Vorlesung in:")
    for index, dire in enumerate(AllDirectories):
        print(f"{index+1}. {dire}")
    while True:
        try:
            indexInput = int(input("-> ")) - 1
            if indexInput > len(AllDirectories) or indexInput < 0:
                continue#because the index is out of range
            global SelectedDirectory
            SelectedDirectory = AllDirectories[indexInput]
            break

        except ValueError:
            continue#if the user entered a non-numeric-value

    try:
        createVorlesung(SelectedDirectory)
    except KeyError:
        print("There was an error while creating the directory. "
              + "No changes were done")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

