"""Helper methods for dealing with files"""
from typing import List


def import_file(file_name: str) -> List[str]:
    """Imports a file as an array of strings, stripping the newline off each line"""
    data = []
    with open(file_name, encoding="utf-8") as file:
        data = [line.rstrip("\n") for line in file.readlines()]
    return data
