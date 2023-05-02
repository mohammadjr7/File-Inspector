"""
[File Inspector]
[Mohammad Javad Rakhshani]
[Dec, 2022]
[Mr. Dadgar]

File inspector is a python script to inspect and traverse file contents easily.
"""
# Project modules
from logger import *
from config import *
import file
import inspector

# Pyhton built-in libraries
import random

operation_code = "1"
operation_message = """
Choose what to do:
\t1. Head [DEFAULT]
\t2. Tail
\t3. Show random line
\t4. Show all lines
"""

file = file.File()

# Methods
# Methods [main]
def main():
    print("[",WELCOME_MESSAGE,"]")
    print("[",APP_NAME,"]")

    # Program Main Code [get file name]
    file.user_get_file_name()
    file.set_file()
    print(f"File is in ", file.get_file())


if __name__ == "__main__":
    main() 