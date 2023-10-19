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
    # The newline at the start and the tab on each line is on purpose
    HELP_STRING: Final[str] = """
    -> a [Foldername]   Add a folder to the list
    -> h                Display this help screen
    -> p                Print the list of folders
    -> q                Continue with the next step of the initialisation
    -> r [Foldername]   Remove a folder from the list
"""[1:]  # Remove the newline at the start
    foldersToIgnore: list[str] = []
    print("Idk what to put here. Have to think about it in the future")
    while True:
        foldersToShow = [f for f in glob(*) if f not in foldersToIgnore]
        for folder in foldersToShow:
            print(folder)

        command, args = input("-> ").split(" ")
        # This is the annoying part when it comes to user input
        if (len(command) > 1):
            ...

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

