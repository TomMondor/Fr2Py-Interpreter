class InvalidFunctionDefinitionException(Exception):
    def __init__(self, function_name : str, line_nbr : int):
        self.function_name = function_name
        self.line_nbr = line_nbr

    def __str__(self):
        output = f"InvalidFunctionDefinitionException: Invalid definition of function"
        output += f" '{self.function_name}' on line {self.line_nbr}.\n"
        output += "Functions can only be defined in the global scope."
        return output
