import re



def is_valid_number(value : str) -> bool:
    """
    Checks if the given string is a valid number.
    ex : -2, -3.25, 0, 0.56, 5, 600.43
    """
    return re.fullmatch(r"^-?(([0-9]+\.?[0-9]+)|([0-9]+))$", value)

def is_valid_identifier(value : str) -> bool:
    """
    Checks if the given string is a valid identifier.
    ex : a, abc, As_Ts, a43es, _a, _a_b5_3
    """
    return re.fullmatch(r"^[a-zA-Z_][a-zA-Z0-9_]*$", value)
