import os
import subprocess


file_directory = "bank_statements/to_be_processed"
file_args_for_func = ["ls", file_directory]

def list_files_from_directory():
    file_listing_process = subprocess.run(file_args_for_func, text=True, capture_output=True)
    list_of_files = file_listing_process.stdout.replace("\n", ",").split(",")[:-1:2]

    list_of_files_with_path = []
    for i in list_of_files:
        list_of_files_with_path.append(f'{file_directory}/{i}')

    '''
    list_of_files_to_display = "\n"
    for i in list_of_files:
        list_of_files_to_display += f'{file_directory}/{i}\n'
        '''

    return list_of_files_with_path

print(list_files_from_directory())
