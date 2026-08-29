import datetime as dt
import json


with open("/home/alek/workspace/alek/budget/budget_files/test.json", "r") as f:
    file_content = json.load(f)

print(file_content)
