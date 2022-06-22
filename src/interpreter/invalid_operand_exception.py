class InvalidOperandException(Exception):
    def __init__(self, operand : str, operator : str, line_nbr : int):
        self.operand = operand
        self.operator = operator
        self.line_nbr = line_nbr

    def __str__(self):
        return f"InvalidOperandException: Invalid operand '{self.operand}' for operator {self.operator} at line {self.line_nbr}"

class InvalidOperandsException(Exception):
    def __init__(self, left_operand : str, operator : str, right_operand : str, line_nbr : int):
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator
        self.line_nbr = line_nbr

    def __str__(self):
        return f"InvalidOperandsException: Invalid operands '{self.left_operand}' and '{self.right_operand}' for operator {self.operator} at line {self.line_nbr}"
