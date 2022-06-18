from tokenizer.tokens import *
from typing import Union

Expression = Union['Variable', 'FunctionCall', 'BinaryOperation', 'UnaryOperation', 'Number', 'String']
Statement = Union['Assignment', 'FunctionCall', 'FunctionDefinition', 'IfStatement', 'ReturnStatement']
#all nodes store the token used to create the node
# node types : (autres spécifiques à demande et affiche?), expression (tous à réfléchir)

class AST_Node:
    pass

class Block(AST_Node):
    def __init__(self, children : list[Statement]):
        self.children : list[Statement] = children

    def append(self, statement : Statement):
        self.children.append(statement)

    def __str__(self):
        output = f"""Node["""
        for child in self.children:
            output += str(child)
            output += "\n"
        output += "]"
        return output

class AbstractSyntaxTree(Block):
    def __init__(self, children : list[Statement]):
        super().__init__(children)

class Number(AST_Node):
    def __init__(self, token : Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return f"Node[{self.value}]"

class String(AST_Node):
    def __init__(self, token : Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return f"Node[{self.value}]"

class Variable(AST_Node):
    def __init__(self, token: Token):
        self.value = token.value
        self.token = token

    def __str__(self):
        return f"Node[{self.value}]"

class Assignment(AST_Node):
    def __init__(self, left : Variable, right : Expression):
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node[{self.left} = {self.right}]"

class BinaryOperation(AST_Node):
    def __init__(self, left : Expression, operator: Token, right : Expression):
        self.left = left
        self.operator = operator
        self.operator_value = operator.value
        self.right = right

    def __str__(self):
        return f"""Node[{str(self.left)} {self.operator.type.name} {str(self.right)}]"""

class UnaryOperation(AST_Node):
    def __init__(self, operator: Token, expression : Expression):
        self.operator = operator
        self.operator_value = operator.value
        self.right = expression

    def __str__(self):
        return f"""Node[{self.operator.type.name} {str(self.right)}]"""

class IfStatement(AST_Node):
    def __init__(self, condition : AST_Node, then_block : Block, else_block : Block):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __str__(self):
        return f"""Node[if {str(self.condition)} then {str(self.then_block)} else {str(self.else_block)}]"""

class FunctionCall(AST_Node):
    def __init__(self, function : Token, args : list[Expression]):
        self.function = function
        self.function_name = function.value
        self.args = args

    def __str__(self):
        return f"""Node[{self.function_name}({', '.join([str(arg) for arg in self.args])})]"""

class ReturnStatement(AST_Node):
    def __init__(self, expression : Union[Expression, None]):
        self.expression = expression

    def returns_nothing(self):
        return self.expression is None

    def __str__(self):
        return f"""Node[return {str(self.expression)}]"""

class FunctionDefinition(AST_Node):
    def __init__(self, function : Token, params : list[Variable], body : Block, return_statement : ReturnStatement):
        self.function = function
        self.function_name = function.value
        self.params = params
        self.body = body
        self.return_statement = return_statement

    def __str__(self):
        return f"""Node[{self.function_name}({', '.join([str(param) for param in self.params])})\n{str(self.body)}\n{str(self.return_statement)}]"""
