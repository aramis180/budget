import json
import os

from tabulate import tabulate

from config import file_directory
from functions.sort_dates import sort_dates
from functions.sum_up_categories import sum_up_categories


def view_contents(filename: str):
    path = f"{os.path.abspath(file_directory)}/{filename}"
    with open(path, "r") as f:
        file_content = json.load(f)



    budget = sum_up_categories(sort_dates(filename))
    categories = ["Dates"]
    for category in budget[list(budget.keys())[0]]:
        categories.append(category)

    list_of_columns = [categories]
    for date in budget.keys():
        list_other_columns = []
        list_other_columns.append(date)
        for category in budget[date]:
            list_other_columns.append(budget[date][category])
        list_of_columns.append(list_other_columns)

    print(tabulate(list_of_columns,headers="firstrow", tablefmt="grid"))
