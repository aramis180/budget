

def add_budget_data(budget: dict[str, dict[str, float]], date: str):
    for category in budget[date]:
        budget[date][category] = float(input(f'Provide value for {category}: '))
    return budget
