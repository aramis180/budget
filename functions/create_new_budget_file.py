from operator import lshift
import subprocess

from config import file_directory, file_format


file_listing_args = ["ls", file_directory]
file_creation_args =["touch"]

def create_new_budget_file():
    filename = f'{input("Provide name for the new budget file, extension is added by the program: ")}{file_format}'
    file_listing_process = subprocess.run(file_listing_args, text=True, capture_output=True)

    result_to_return = ""

    if file_listing_process.stderr:
        result_to_return = file_listing_process.stderr
    if file_listing_process.stdout:
        list_of_files = file_listing_process.stdout.replace("\n", ",").split(",")[:-1]
        if filename in list_of_files:
            while True:
                print(f'File: {filename} already exists, please provide different filename')
                filename = input("Provide name for the new budget file, extension is added by the program: ")
                if filename not in list_of_files:
                    break

        file_creation_args.append(f'{filename}{file_format}')
        file_creation_process = subprocess.run(file_creation_args, text=True, capture_output=True)

        if file_creation_process.stderr:
            result_to_return = file_creation_process.stderr
        result_to_return = f'Created file: {filename}{file_format}'

    return print(result_to_return)
