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

# Private Objects
_user_file = None

# Global Objects
file = file.File()
inspector = inspector.Inspector()
OP_MESSAGE = """
Choose what to do:
\t1. Head [DEFAULT]
\t2. Tail
\t3. Show random line
\t4. Show all lines

\t Write [e]/[exit] to terminate the program.
>>> """
op_code = "1"

# Methods
# Methods [main]
def main():
    global _user_file
    global op_code

    print("[",WELCOME_MESSAGE,"]")
    print("[",APP_NAME,"]")

    # Get file name from user
    file.user_get_file_name()

    # Initialization of the file name from user
    file.set_file()

    # Find file content
    _user_file = file.get_file()

    # Initialize file inspector
    inspector.set_buffer(_user_file.readlines())

    if _user_file != None:
        while True:
            input_buffer = input(OP_MESSAGE)
            op_code = input_buffer.strip().lower()
            if op_code == "" or op_code == "1":
                lines = input("Lines to read [Default: 5]: ").strip()
                if lines != "":
                    try:
                        lines = int(lines)
                        inspector.head(inspector.get_buffer() ,line_count=lines)
                    except:
                        log(log_levels["error"], "Line count should be a number.")
                        continue
                else:
                    inspector.head(inspector.get_buffer())
            elif op_code == "2":
                lines = input("Lines to read [Default: 5]: ").strip()
                if lines != "":
                    try:
                        lines = int(lines)
                        inspector.tail(inspector.get_buffer(), line_count=lines)
                    except:
                        log(log_levels["error"], "Line count should be a number.")
                        continue
                else:
                        inspector.tail(inspector.get_buffer())
            elif op_code == "3":
                inspector.show_r(inspector.get_buffer())
            elif op_code == "4":
                inspector.show_all(inspector.get_buffer())
            elif op_code == "exit" or op_code == "0":
                log(log_levels["info"], f" {op_code} was terminated the program.")
                n = input("Press any key to exit...")
                exit(0)
            
    else:
        log("error", "There was a problem reading the file.")


if __name__ == "__main__":
    main() 