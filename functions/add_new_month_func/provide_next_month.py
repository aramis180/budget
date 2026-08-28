import datetime

def provide_next_month(date: str):

    date_holder = date.split("-")
    if int(date_holder[0]) == 12:
        date_holder[0] = "1"
        date_holder[1] = f'{int(date_holder[1]) + 1}'
        date = datetime.date(int(date_holder[1]), int(date_holder[0]), 1).strftime("%m-%Y")
    else:
        date = datetime.date(int(date_holder[1]), int(date_holder[0]) + 1, 1).strftime("%m-%Y")
    print(date)

    return date
