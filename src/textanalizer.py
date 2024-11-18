"""Text analizer logic"""

from pathlib import Path
import re

DIR_PATH = Path(__file__).parent.parent.parent.parent
INPUT_DIR = DIR_PATH / "InputFiles"
OUTPUT_DIR = DIR_PATH / "OutputFiles"
INPUT_FILE_NAME = fr"{INPUT_DIR}\data"


def read_file_by_ext(ext: str) -> list:
    with open(f"{INPUT_FILE_NAME}.{ext}", "r") as fr:
        return [item.strip() for item in fr.readlines()]


def split_file_data(text: list[str]):
    chars = 0
    words = 0
    phrases = 0
    signs = [".", "?", "!"]

    for item in text:
        if not item:
            continue
        chars += len(item.replace(" ", ""))
        words += len(item.split(" "))
        if item[-1] in signs:
            phrases += 1

    return chars, words, phrases