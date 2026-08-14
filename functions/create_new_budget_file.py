import subprocess

def create_new_budget_file():
    filename = input("Provide name for the new budget file, extension is added by the program: ")
    create_file_command = f'touch budget_files/{filename}.txt'
