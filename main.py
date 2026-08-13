import argparse

from add_new_month import add_new_month
from allowed_functions import action_string
from action_question import action_question

def main():
    introduction = """
    Wlecome to the Budget!
    This program allows to create and alter existing budgets.
    Please follow instructions!
    """
    print(introduction)

    action_allowed = [0, 1, 2]
    action = action_question()

    while True:
        if action == 0:
            print("Goodbye")
            break
        if action == 1:
            break
        if action == 2:
            date = add_new_month()
            action = action_question()
        if action not in action_allowed:
            action = int(input(f"""
                Please provide valid number:
                    {action_string}
                    """))

    return 1


if __name__ == "__main__":
    main()
