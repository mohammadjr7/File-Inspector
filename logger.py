"""
[File Inspector]
[Mohammad Javad Rakhshani]
[Dec, 2022]
[Mr. Dadgar]

This module provides logging functionality.
"""

# Pyhton built-in libraries
import datetime
from os import mkdir

# Global variables
log_levels: dict = {"info": "[INFO]"
            ,"warning": "[WARNING]"
            ,"error": "[ERROR]"
            ,"start": "[START]"
            ,"end": "[END]"}
_log_file: str = str()
NEW_LINE: str = "\r\n"

# Methods
# Method [do log]
def log(level, message):
    global _log_file
    try:
        _log_file = open(f"logs/{level.lower()}.log", "a")
    except FileNotFoundError:
        print(log_levels["info"], "Directory [logs] not found! Try to create.")
        logger_mkdir()
        _log_file = open(f"logs/{level.lower()}.log", "w")

    _log_file.write(f"{datetime.datetime.now()} - {message}{NEW_LINE}")
    _log_file.close()

    del _log_file


# Method [make directory for logs]
def logger_mkdir():
        try:
            mkdir("logs")
            print(log_levels["info"], "Directory [logs] created successfully.")
        except FileExistsError:
            print(log_levels["info"], "Directory [logs] found.")

if __name__ == "__main__":
    print(log_levels["warning"], "This python script is intended to be used as external module.")