import copy

from default_template import default_template
from functions.add_new_month_func.provide_month import provide_month
from functions.add_new_month_func.add_data_to_provided_date import add_data_to_provided_date
from functions.add_new_month_func.edit_existing_budget_file import edit_existing_budget_file
from functions.add_new_month_func.provide_next_month import provide_next_month

def add_new_month(filename: str):
    date = provide_month()
    data_to_be_added = {}
    data_to_be_added[date] = copy.deepcopy(default_template)
    add_data_to_provided_date(data_to_be_added, date)

    possibilities = [0, 1]
    while True:
        loop = int(input("""
        Do you want to add next month?

        0 -> No
        1 -> Yes
        """))
        if loop not in possibilities:
            loop = int(input("""
        Do you want to add next month?

        0 -> No
        1 -> Yes
        """))

        if loop == 0:
            break
        date = provide_next_month(date)
        data_to_be_added[date] = copy.deepcopy(default_template)
        add_data_to_provided_date(data_to_be_added, date)

    edit_existing_budget_file(data_to_be_added, filename)
