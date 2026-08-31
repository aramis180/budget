def add_data_to_provided_date(budget, date: str):
    for category in budget[date]:
        if isinstance(budget[date][category], float):
            budget[date][category] = float(input(f'Provide value for {category}: '))
        if isinstance(budget[date][category], dict):
            recursive_budget_edit(budget[date][category])
        print(budget)
    return budget

def recursive_budget_edit(budget):
    for category in budget:
        if isinstance(budget[category], (float, int)):
            budget_entry = float(input(f'Provide value for {category}: '))
            budget[category] = budget_entry
        if isinstance(budget[category], dict):
            recursive_budget_edit(budget[category])
