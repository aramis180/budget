from .allowed_functions import action_string

def action_question():
    action = int(input(f"""
        What do you want to do? Provide number:
            {action_string}
        """))
    return action
