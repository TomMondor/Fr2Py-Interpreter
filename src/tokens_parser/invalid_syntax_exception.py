from typing import Union
from tokenizer.tokens import Token



class InvalidSyntaxException(Exception):
    def __init__(self, value : Union[str, list[Token]], line_nbr : int):
        self.value = value
        self.line_nbr = line_nbr

    def __str__(self):
        #TODO make debugging easier by passing the raw program and printing the raw line of code
        if isinstance(self.value, str):
            return f"InvalidSyntaxException: Invalid syntax '{self.value}' at line {self.line_nbr}"
        elif isinstance(self.value, list):
            output = ""
            for token in self.value:
                output += str(token)
                output += " "
            output += "\n"
            output += f"InvalidSyntaxException: Invalid syntax at line {self.line_nbr}"
            return output
        else:
            return f"InvalidSyntaxException: Invalid syntax at line {self.line_nbr}"
