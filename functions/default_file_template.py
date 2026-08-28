import os
import json
import copy

from default_template import default_template
from functions.add_new_month_func.provide_month import provide_month
from functions.add_new_month_func.add_data_to_provided_date import add_data_to_provided_date
from config import file_directory
from functions.add_new_month_func.provide_next_month import provide_next_month


def defatult_file_template(filename: str):
    budget = {}
    default_consent = int(input("""
        Do you want to use default budget template?

        0 -> No
        1 -> Yes
        """))
    if default_consent == 0:
        return
    if default_consent == 1:
        print("""
        Now you will provide data for your budget.
        """)
        date = provide_month()
        while True:
            budget[date] = copy.deepcopy(default_template)
            print(default_template)
            print(add_data_to_provided_date(budget, date))
            loop = int(input("""
        Do you want to add next month?

        0 -> No
        1 -> Yes
        """))
            if loop == 0:
                path = f'{os.path.abspath(file_directory)}/{filename}'
                with open(path, "w") as f:
                    json.dump(budget, f)
                break
            date = provide_next_month(date)
