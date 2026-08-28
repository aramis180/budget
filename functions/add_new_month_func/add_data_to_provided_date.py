def add_data_to_provided_date(budget: dict[str, dict[str, float]], date: str):
    for category in budget[date]:
        budget[date][category] = float(input(f'Provide value for {category}: '))
        print(budget)
    return budget
