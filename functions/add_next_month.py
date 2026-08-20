import datetime

from functions.add_budget_data import add_budget_data


def add_next_month(budget: dict[str, dict[str, float]], date_my: str):
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

        date_holder = date_my.split("-")
        if int(date_holder[0]) == 12:
            date_holder[0] = "1"
            date_holder[1] = f'{int(date_holder[1]) + 1}'
            date = datetime.date(int(date_holder[1]), int(date_holder[0]), 1).strftime("%m-%Y")
        else:
            date = datetime.date(int(date_holder[1]), int(date_holder[0]) + 1, 1).strftime("%m-%Y")

        return add_budget_data(budget, date)
