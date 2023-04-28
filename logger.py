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
log_file: str = str()
log_file_name: str = str()
new_line: str = "\r\n"

# Methods
# Method [do log]
def log(level, message):
    global log_file
    try:
        log_file = open(f"logs/{level.lower()}.log", "a")
    except FileNotFoundError:
        print(log_levels["info"], "Directory [logs] not found! Try to create.")
        logger_mkdir()
        log_file = open(f"logs/{level.lower()}.log", "w")

    log_file.write(f"{datetime.datetime.now()} - {message}{new_line}")
    log_file.close()

    del log_file


# Method [make directory for logs]
def logger_mkdir():
        try:
            mkdir("logs")
            print(log_levels["info"], "Directory [logs] created successfully.")
        except FileExistsError:
            print(log_levels["info"], "Directory [logs] found.")

if __name__ == "__main__":
    print(log_levels["warning"], "This python script is intended to be used as external module.")