# context_utils.py

import os
import sys
from pathlib import Path

def append_context_if_exists(context_filename):
   
    if not context_filename:
        return ""

    expected_filename = ''.join(context_filename)
    path = Path.cwd()

    for con in os.listdir(path):
        file_path = path / con
        if file_path.is_file() and con == expected_filename:
            with open(file_path, "r") as file:
                file_content = file.read()
                return f"""context:\n{file_content} \n"""

    print("The file does not exist inside the current directory")
    sys.exit(0)
