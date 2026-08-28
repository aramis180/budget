
import os
import json
from config import file_directory

def edit_existing_budget_file(budget: dict[str, dict[str, float]], filename):
    path = f'{os.path.abspath(file_directory)}/{filename}'
    with open(path, "r") as f:
        file_content = json.load(f)

    for date in budget:
        file_content[date] = budget[date]

    with open(path, "w") as f:
        json.dump(file_content, f)

    with open(path, "r") as f:
        file_content = json.load(f)
    print(file_content)
