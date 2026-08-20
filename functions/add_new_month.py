import datetime


def add_new_month():
    month_allowed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    month = int(input("Provide month as integer, ex. 1 for January and 12 for December: "))
    while True:
        if month in month_allowed:
            break
        month = int(input("Please provide proper input, ex. 1 for January and 12 for December: "))
    year = int(input("Provide year as integer, year should be in range from 0 to 9999 , ex. 2026: "))
    while True:
        if year <= 9999 and year >= 0:
            break
        year = int(input("Please provide proper input, year should be in range from 0 to 9999: "))

    date = datetime.date(year, month, 1).strftime("%m-%Y")

    return date
