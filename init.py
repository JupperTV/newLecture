# Dieses Skript soll zuallererst ausgeführt werden

from pathlib import Path  # Maybe use pathlib.Path instead of strings?
from os.path import isdir
from typing import Final


BATCH_FILE_CONTENT: Final[str] = f"@echo off\npython {__file__}"

# 1. Wähle Pfad aus
def ChoosePath() -> str:
    print("Enter the Path to the directory with all of your courses:")
    while True:
        coursePath = input("-> ").strip("\"")
        if isdir(coursePath):
            return coursePath

# 2. Wähle Ordner zum Ignorieren aus
# 3. Erstelle .vorlesung.ignore
def SelectDirsForVorlesungen(selectedPath: str) -> list[str]:
    HELP_STRING: Final[str] = """
"""[1:]  # Strip the newline at the beginning

    # Funktionsweise:
    # -> [Command als einzelner Buchstabe] [Ordner als Parameter]
    # a: Ordner zu der Liste hinzufügen
    # d: Ordner aus der Liste löschen
    # h: Hile auswählen
    # q: Ordner Auswahl schließen. Alle Ordner, die Vorlesungen
    #    enthalten, wurden schon ausgewählt
    while True:
        pass
    # And write .vorlesungen.ignore


# 4. Gebe Anzahl an Vorlesungen ein, die es bereits gab
# 5. Erstelle vorlesung_counter.json
def InputNumOfVorlesungen(directoriesForVorlesungen: list[str]):
    pass
    # And create vorlesungen_counter.json


if __name__ == "__main__":
    vorlesungenPath: str = ChoosePath()
    dirsForVorlesungen: list[str] = SelectDirsForVorlesungen(vorlesungenPath)
    InputNumOfVorlesungen(dirsForVorlesungen)
    # 6. Erstelle Batch Datei
    open("new.bat", "w").write(BATCH_FILE_CONTENT)

