"""
[File Inspector]
[Mohammad Javad Rakhshani]
[Dec, 2022]
[Mr. Dadgar]

This class is intended for inspection of files.
"""

# Project configs
from config import *
# Project modules
from logger import *
# Pyhton built-in libraries
import random

# Class definition
class Inspector():
    _buffer: str = str()

    # Methods
    # Methods [constructor]
    def __init__(self):
        pass

    # Methods [set file content to buffer]
    def set_buffer(self, content: str):
        self._buffer = content

    # Methods [get file content from buffer]
    def get_buffer(self) -> str:
        if self._buffer != None:
            return self._buffer
        else:
            return ""

    # Methods [head]
    def head(self, file_contents=_buffer, line_count=5):
        """
        Get head content of the file.
        If [line_count] was bigger than length of file lines, program will print all contents.
        """
        log("info", "Start reading file {line_count} line(s) head.")
        print(NEW_LINE + log_levels["start"])

        if line_count > len(file_contents):
            for line in range(len(file_contents)):
                print(file_contents[line],end="")
        else:
            for line in range(line_count):
                print(file_contents[line],end="")

        print(NEW_LINE + log_levels["end"])

    # Methods [tail]
    def tail(self, file_contents=_buffer, line_count=5):
        """
        Get the tail content of file.
        If [line_count] was bigger than length of file lines, program will print all contents.
        """
        log("info", "Start reading file {line_count} line(s) tail.")
        print(NEW_LINE + log_levels["start"])

        if line_count > len(file_contents):
            for line in range(len(file_contents)):
                print(file_contents[line],end="")
        else:
            cursor = line_count
            for line in range(line_count):
                print(file_contents[-cursor],end="")
                cursor -= 1

        print(NEW_LINE + log_levels["end"])

    # Methods [show random]
    def show_r(self, file_contents=_buffer):
        """
        Show a random line of file.
        """
        log("info", "Start reading random file line.")
        print(NEW_LINE + log_levels["start"])

        random_number = random.randint(0, len(file_contents) - 1)
        print(file_contents[random_number].strip("\n"),end="")

        print(NEW_LINE + log_levels["end"])

    # Methods [show random]
    def show_all(self, file_contents=_buffer):
        """
        Show all lines inside the file.
        """
        log("info", "Start reading file.")
        print(NEW_LINE + log_levels["start"])

        for line in range(len(file_contents)):
            print(file_contents[line],end="")

        print(NEW_LINE + log_levels["end"])
