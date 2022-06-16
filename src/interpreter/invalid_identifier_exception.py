class InvalidIdentifierException(Exception):
    def __init__(self, identifier : str, line_nbr : int):
        self.identifier = identifier
        self.line_nbr = line_nbr

    def __str__(self):
        return f"InvalidIdentifierException: Invalid identifier '{self.identifier}' at line {self.line_nbr}"
