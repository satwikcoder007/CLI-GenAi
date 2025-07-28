import os
import sys
from pathlib import Path

def append_context_if_exists(context_filename):
    if not context_filename:
        return {}

    expected_filename = ''.join(context_filename)
    path = Path.cwd()

    for con in os.listdir(path):
        file_path = path / con
        if file_path.is_file() and con == expected_filename:
            file_extension = file_path.suffix  # Includes the dot, e.g., '.txt'
            with open(file_path, "r") as file:
                file_content = file.read()
                return {
                    "type": file_extension.lstrip('.'),  # removes the dot, e.g., 'txt'
                    "content": file_content
                }

    print("The file does not exist inside the current directory")
    sys.exit(0)
