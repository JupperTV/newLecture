# Dieses Skript soll zuallererst ausgeführt werden

from pathlib import Path  # Maybe use pathlib.Path instead of strings?
from os.path import isdir
from typing import Final


BATCH_FILE_CONTENT: Final[str] = f"@echo off\npython {__file__}"

# 1. Wähle Pfad aus
def ChooseDirectory() -> str:
    print("Enter the Path to the directory with all of your courses:")
    while True:
        coursePath = input("-> ").strip("\"")
        if isdir(coursePath):
            return coursePath

# 2. Wähle Ordner zum Ignorieren aus
# 3. Erstelle .vorlesung.ignore
def SelectFoldersForVorlesugen(selectedPath: str) -> list[str]:
    # The tab on each line is on purpose
    HELP_STRING: Final[str] = """
    -> a [Foldername]   Add a folder to the list
    -> h                Display this help screen
    -> p                Print the list of folders
    -> q                Continue with the next step of the initialisation
    -> r [Foldername]   Remove a folder from the list
"""[1:]  # Remove the newline at the start
    foldersToIgnore: list[str] = []
    print("Enter the name of a folder that should contain Vorlesungen")
    while True:
        foldersToShow = [f for f in glob(*) if f not in foldersToIgnore]
        for folder in foldersToShow:
            print(folder)
        "\t"
        command, args = input("-> ").split(" ")

        commands: dict[str, callable] = {
                "a": lambda: raise NotImplementedError,
                "h": lambda: print(HELP_STRING)
                "p": lambda: raise NotImplementedError,
                "q": lambda: break

                }
        # This is the annoying part of user input
        if len(command) == 1 and command in commands.keys():
                continue
        if not isdir(args):
            print(f"'{args}' is not a folder"
            continue

    # And write .vorlesungen.ignore
    open(".vorlesungen.ignore", "w").write()


# 4. Gebe Anzahl an Vorlesungen ein, die es bereits gab
# 5. Erstelle vorlesung_counter.json
def InputNumOfVorlesungen(directoriesForVorlesungen: list[str]):
    pass
    # And create vorlesungen_counter.json


if __name__ == "__main__":
    vorlesungenPath: str = ChooseDirectory()
    dirsForVorlesungen: list[str] = SelectFoldersForVorlesugen(vorlesungenPath)
    InputNumOfVorlesungen(dirsForVorlesungen)
    # 6. Erstelle Batch Datei
    open("new.bat", "w").write(BATCH_FILE_CONTENT)

