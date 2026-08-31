



default_template_combo = {
    "Salary": {
        "Net salary": 1.0,
        "Bonus": 2.0,
        "Other": 3.0
    },
    "Other proceeds": 5.0,
    "Savings": {
        "IKE": 5.0,
        "IKZE obligacje": 1.0,
        "Stocks": 7.0,
        "Emergency Fund": {
            "Cash": 0.0,
            "ING": 0.0,
            "PKOBP": 0.0
        },
        "Bargain": 2.0
    },
    "Fixed payments": 0.0,
    "Food": None,
    "Lavish lifestyle": 1.0
}


def sum_up_categories(default_template_combo, default_template=None):
    if default_template is None:
        default_template = {}
    for category in default_template_combo:
        total = 0.0
        if isinstance(default_template_combo[category], (float, int)) or default_template_combo[category] is None:
            if default_template_combo[category] is None:
                default_template_combo[category] = 0
            total += default_template_combo[category]
        if isinstance(default_template_combo[category], dict):
            total += nested_sum_dict(default_template_combo[category])
        default_template[category] = total
    return default_template


def nested_sum_dict(template):
    total = 0.0
    for i in template:
        if isinstance(template[i], float):
            total += template[i]
        if isinstance(template[i], dict):
            total += nested_sum_dict(template[i])
    return total


print(sum_up_categories(default_template_combo))
