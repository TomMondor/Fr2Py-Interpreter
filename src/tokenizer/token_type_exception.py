class TokenTypeException(Exception):
    def __init__(self, value : str, line_nbr : int):
        self.value = value
        self.line_nbr = line_nbr

    def __str__(self):
        return f"TokenTypeException: No token matching string '{self.value}' at line {self.line_nbr}"

class StringLiteralException(TokenTypeException):
    def __init__(self, invalid_string : str, line_nbr : int):
        self.invalid_string = invalid_string
        self.line_nbr = line_nbr

    def __str__(self):
        return f"""StringLiteralException: Invalid string literal "{self.invalid_string}" at line {self.line_nbr}"""

class InvalidOperatorException(TokenTypeException):
    def __init__(self, invalid_operator : str, line_nbr : int):
        self.invalid_operator = invalid_operator
        self.line_nbr = line_nbr

    def __str__(self):
        return f"""InvalidOperatorException: Invalid operator "{self.invalid_operator}" at line {self.line_nbr}"""
