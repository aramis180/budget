import datetime as dt
import os
import json

from config import file_directory

def sort_dates(filename: str):
    path = f"{os.path.abspath(file_directory)}/{filename}"
    with open(path, "r") as f:
        file_content = json.load(f)

    list_of_keys = []
    dict_for_comparison = {}
    date_for_comparison_first = dt.date(1,1,1)
    for month in file_content.keys():
        holder_str = month.split("-")
        holder_int = []
        for string in holder_str:
            holder_int.append(int(string))
        date = dt.date(holder_int[1], holder_int[0], 1).strftime("%m-%Y")
        date_for_comparison_second = dt.date(holder_int[1], holder_int[0], 1)
        difference = date_for_comparison_second - date_for_comparison_first
        dict_for_comparison[difference.days] = date
    for key in sorted(dict_for_comparison.keys()):
        list_of_keys.append(dict_for_comparison[key])

    budget = {}
    for key in list_of_keys:
        budget[key] = file_content[key]

    return budget
