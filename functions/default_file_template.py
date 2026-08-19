import os

from default_template import default_template
from functions.add_new_month import add_new_month
from functions.add_budget_data import add_budget_data
from config import file_directory


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
        while True:
            date = add_new_month()
            budget[date] = default_template
            print(add_budget_data(budget, date))
            loop = int(input("""
        Do you want to add next month?

        0 -> No
        1 -> Yes
        """))
            if loop == 0:
                path = f'{os.path.abspath(file_directory)}/{filename}'
                with open(path, "w") as f:
                    f.write(f'{budget}')
                break
