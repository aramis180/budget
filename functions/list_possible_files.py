import os
import subprocess
from config import file_directory

file_listing_args = ["ls", file_directory]

def list_possible_files():
    file_listing_process = subprocess.run(file_listing_args, text=True, capture_output=True)
    list_of_files = file_listing_process.stdout.replace("\n", ",").split(",")[:-1]
    list_of_files_to_display = "\n"
    counter = 0
    for i in list_of_files:
        list_of_files_to_display += f'{counter} -> {i}\n'
        counter += 1


    files_to_be_edited = int(input((f"""
        Files that can be eddited
        {list_of_files_to_display}
        """)))

    filename = list_of_files[files_to_be_edited]
    path = f'{os.path.abspath(file_directory)}/{filename}'

    with open(path, "r") as f:
        file_content = f.read()
    print(f"""
        Budget in {filename} contains:

{file_content}
        """)

    return filename
