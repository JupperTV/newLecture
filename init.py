from pathlib import Path  # Maybe use pathlib.Path instead of strings?
from os.path import isdir
from typing import Final

BATCH_FILE_CONTENT: Final[str] = f"@echo off\npython {__file__}"

HELP_STRING: Final[str] = """
\ta [folder]    Add a folder to the list
\th             Display this help screen
\tp             Print the list of folders
\tq             Continue with the next step of the initialisation
\tr [folder]    Remove a folder from the list
"""[1:]  # Remove the newline at the start


class BreakFromFunction(Exception):
    def __init__(*args):
        super("")


# 1. Select the Path that contains all the folders/directories
#    with lectures
def ChooseDirectory() -> str:
    print("> Enter the Path to the directory with all of your lectures:")
    while True:
        coursePath = input("-> ").strip("\"")
        if isdir(coursePath):
            return coursePath


# 2. Choose all Folders (or Directories) that should contain lectures
# 3. Create .lectures.ignore
    # .lectures.ignore contains all of the folders
    # that do not contain lectures
def SelectFoldersForLectures(selectedPath: str) -> list[str]:
    foldersToIgnore: list[str] = []
    def addFolderToList(folder):  # TODO
        raise NotImplementedError()
    def removeFolderFromList(folder):  # TODO
        raise NotImplementedError()
    print("> Enter the name of a folder that should contain lectures")
    while True:
        foldersToShow = [f for f in glob("*") if f not in foldersToIgnore]
        for folder in foldersToShow:
            print(folder)
        command, args = input("-> ").split(" ")
        commands: dict[str, callable] = {
                "a": addFolderToList,
                "h": lambda _: print(HELP_STRING),
                "p": removeFolderFromList,
                "q": BreakFromFunction
        }

        # This is the annoying part of user input
        if len(command) != 1 or command not in commands.keys():
            continue
        if not isdir(args):
            print(f"> '{args}' is not a folder")
            continue

        try:
            commands[command](args)  # Execute the command
        except BreakFromFunction:
            break

    # And write .vorlesungen.ignore
    ignoreFolders: list[str] = [f for f in glob("*") if f not in foldersToShow]
    open(".lectures.ignore", "w").write("\n".join(ignoreFolders).strip("\n"))
    return foldersToShow


# 4. Enter the number of lectures in each folder, if they already existed
# 5. Create lectures_counter.json
def InputNumOfLectures(foldersForLectures: list[str]) -> None:
    print("> Did any Vorlesungen exist previously? (y/n)")
    userAnswerDidLecturesExist = None
    while userAnswer not in ["y", "n", "yes", "no"]:
        userAnswerDidLecturesExist = input("-> ")
    if userAnswerDidLecturesExist in ["n", "no"]:
        return

    lectures = {}
    while True:
        for folder in foldersForLectures:
            print(f"> {folder}")
        userSelectedFolder = input("\n> Select a Folder:\n-> ")
        if userSelectedFolder not in foldersForLectures:
            continue
        lectureCount = None
        while type(lectureCount) is not
        lectureCountInput = input("> Input the Number of Vorlesungen for"
                                      + "that already exist:")
        try:
            vorlesungenCount = int(lectureCountInput)
        except ValueError:
            continue
        raise NotImplementedError

try:
    if __name__ == "__main__":
        path: str = ChooseDirectory()
        dirsForLectures: list[str] = SelectFoldersForLectures(path)
        InputNumOfLectures(dirsForLectures)
        # 6. Create Batch File for `newLectures.py`
        open("new.bat", "w").write(BATCH_FILE_CONTENT)
except KeyboardInterrupt:
    exit(0)

