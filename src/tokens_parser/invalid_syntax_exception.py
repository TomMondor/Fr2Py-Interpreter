class InvalidSyntaxException(Exception):
    def __init__(self, value : str, line_nbr : int):
        self.value = value
        self.line_nbr = line_nbr

    def __str__(self):
        return f"InvalidSyntaxException: Invalid syntax '{self.value}' at line {self.line_nbr}"
