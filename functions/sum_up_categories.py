

def sum_up_categories(budget, default_template=None):
    if default_template is None:
        default_template = {}
    for date in budget:
        default_template[date] = {}
        for category in budget[date]:
            total = 0.0
            if isinstance(budget[date][category], (float, int)) or budget[date][category] is None:
                if budget[date][category] is None:
                    budget[date][category] = 0
                total += budget[date][category]
            if isinstance(budget[date][category], dict):
                total += nested_sum_dict(budget[date][category])
            default_template[date][category] = total
    return default_template


def nested_sum_dict(template):
    total = 0.0
    for i in template:
        if isinstance(template[i], float):
            total += template[i]
        if isinstance(template[i], dict):
            total += nested_sum_dict(template[i])
    return total
