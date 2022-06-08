class UnexpectedEndOfFileException(Exception):
    def __init__(self, line_nbr : int):
        self.line_nbr = line_nbr

    def __str__(self):
        return f"UnexpectedEndOfFileException: Unexpected end of file at line {self.line_nbr}"
