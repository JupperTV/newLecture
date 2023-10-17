from glob import glob
from os.path import isdir
from os import mkdir
from typing import Final
from pathlib import Path
import json


JSONFILENAME: Final[str] = "vorlesung_counter.json"


def CreateVorlesung(parentDirectory: str) -> None:
    #  1. Get count in vorlesung_counter.json
    counters: dict[str, int] = json.load(open(JSONFILENAME, ))
    if parentDirectory not in counters.keys():
        raise KeyError("The given directory doesn't exist")
    if len(counters.keys()) == 0:
        raise IOError(f"The {JSONFILENAME} file is empty. Write it manually")
    counters[parentDirectory] += 1
    mkdir(rf"{parentDirectory}\Vorlesung {counters[parentDirectory]}")

    # 2. Overwrite because of raised counter
    json.dump(counters, open(JSONFILENAME, "w"))


def FilterDirectories(filecontent: Final[str]) -> list[str]:
    directoriesToIgnore: list[str] = [path for path in filecontent.split("\n")]
    allDirectories: list[str] = []
    for directory in glob("*"):
        if isdir(directory) and directory not in directoriesToIgnore:
            allDirectories.append(directory)
    return allDirectories


def UserDirectorySelect(allDirectories: list[str]) -> str:
    while True:
        try:
            indexInput = int(input("-> ")) - 1
            if indexInput > len(allDirectories) or indexInput < 0:
                continue#because the index is out of range
            userSelectedDirectory = allDirectories[indexInput]
            break
        except ValueError:
            continue#if the user entered a non-numeric-value
    return userSelectedDirectory


def main():
    try:#to read the ignore file
        IgnoreFile_Content: Final[str] = open(".vorlesung.ignore", "r").read()
    except FileNotFoundError:
        pass # All of the directories will be selectable

    allDirectories = FilterDirectories(IgnoreFile_Content)


    print("Select the number of the directory to create the new Vorlesung in:")
    for index, dire in enumerate(allDirectories):
        print(f"{index+1}. {dire}")

    userSelectedDirectory = UserDirectorySelect(allDirectories)

    try:
        CreateVorlesung(userSelectedDirectory)
    except KeyError:
        print("There was an error while creating the directory. "
              + "No changes were done")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

