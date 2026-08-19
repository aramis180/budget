import argparse

from functions.add_budget_data import add_budget_data
from functions.add_new_month import add_new_month
from functions.allowed_functions import action_string
from functions.action_question import action_question
from functions.create_new_budget_file import create_new_budget_file
from default_template import default_template
from functions.default_file_template import defatult_file_template
from functions.edit_file import edit_file

def main():
    introduction = """
    Wlecome to the Budget!
    This program allows to create and alter existing budgets.
    Please follow instructions!
    """
    print(introduction)

    action_allowed = [0, 1, 2]
    action = action_question()

    budget = {}

    while True:
        if action == 0:
            print("Goodbye")
            break
        if action == 1:
            filename = create_new_budget_file()
            defatult_file_template(filename)
            action = action_question()
        if action == 2:
            edit_file()
            date = add_new_month()
            budget[date] = default_template
            print(add_budget_data(budget, date))

            action = action_question()
        if action not in action_allowed:
            action = int(input(f"""
                Please provide valid number:
                    {action_string}
                    """))

    return 1


if __name__ == "__main__":
    main()
