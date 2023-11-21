from glob import glob
from os.path import isdir
from os import mkdir
from typing import Final
from pathlib import Path
import json


JSONFILENAME: Final[str] = "lecture_counter.json"


def CreateLecture(parentDirectory: str) -> None:
    #  1. Get count in lecture_counter.json
    counters: dict[str, int] = json.load(open(JSONFILENAME, ))
    if parentDirectory not in counters.keys():
        raise KeyError("The given directory doesn't exist")
    if len(counters.keys()) == 0:
        raise IOError(f"The {JSONFILENAME} file is empty. Write it manually")
    counters[parentDirectory] += 1
    mkdir(rf"{parentDirectory}\Lecture {counters[parentDirectory]}")

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
    try:
        IgnoreFileContent: Final[str] = open(JSONFILENAME, "r").read()
    except FileNotFoundError:
        # All of the directories will be selectable
        IgnoreFileContent = ""

    allDirectories = FilterDirectories(IgnoreFileContent)

    print("Select the number of the directory to create the new lecture in:")
    for index, dire in enumerate(allDirectories):
        print(f"{index+1}. {dire}")

    userSelectedDirectory = UserDirectorySelect(allDirectories)

    try:
        CreateLecture(userSelectedDirectory)
    except KeyError:
        print("There was an error while creating the directory. "
              + "No changes were done")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

