
import os
from config import file_directory

def edit_existing_budget_file(budget: dict[str, dict[str, float]], filename):
    path = f'{os.path.abspath(file_directory)}/{filename}'
    with open(path, "a") as f:
        f.write(f'{budget}')

    with open(path, "r") as f:
        file_content = f.read()
    print(file_content)
