"""
[File Inspector]
[Mohammad Javad Rakhshani]
[Dec, 2022]
[Mr. Dadgar]

This class is intended for handling file I/O operations.
"""

# Project configs
from config import *
# Project modules
from logger import *

# Class definition
class File():
    _file = None
    _file_name: str = str()
    _file_name_buffer: str = str()

    # Methods
    # Methods [constructor]
    def __init__(self):
        pass

    # Methods [set file]
    def set_file(self):
        """
        Create file based on the user-input filename.
        """
        log(log_levels["info"], f"Reading file {self._file_name}.")
        try:
            self._file = open(f"{self.get_file_name()}")
        except FileNotFoundError:
            log(log_levels["warning"], "File does not exist.")
            # Try creating the file
            self._file = open(f"{self.get_file_name()}", mode="w")

            self._file.write(f"This is an auto generated message from {APP_NAME}!")
            self._file.close()
            
            # Try reading the auto-generated file
            self._file = open(f"{self.get_file_name()}", mode="r")

            log(log_levels["info"], "File has been created automatically.")
        except:    
            print(log_levels["error"], f"Something went wrong reading the file {self._file_name}")


    # Methods [get file]
    def get_file(self):
        """
        Return user's file.
        """
        return self._file

    # Methods [get file name from user]
    def user_get_file_name(self):
            """
            Get file name from the user;
            If file not found, it will be created.
            """
            while True:
                self._file_name_buffer = input("File name: ").strip()
                if self._file_name_buffer != "":
                    if self._file_name_buffer.find(".") == -1:
                        self._file_name_buffer += ".txt"
                        self._file_name = self._file_name_buffer
                        break
                    else:
                        self._file_name = self._file_name_buffer
                        break
                else:
                    log(log_levels["error"], "Empty file name is not allowed.")


    # Methods [get file name]
    def get_file_name(self):
        """
        Return user's filename.
        """
        return self._file_name
