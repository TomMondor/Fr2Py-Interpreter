from tokenizer.tokens import *
from typing import Union

Expression = Union['Variable', 'FunctionCall', 'BinaryOperation', 'Number', 'String']
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

class AbstractSyntaxTree(Block):
    def __init__(self, children : list[Statement]):
        super().__init__(children)

class Number(AST_Node):
    def __init__(self, token : Token):
        self.token = token
        self.value = token.value

class String(AST_Node):
    def __init__(self, token : Token):
        self.token = token
        self.value = token.value

class Variable(AST_Node):
    def __init__(self, token: Token):
        self.value = token.value
        self.token = token

class Assignment(AST_Node):
    def __init__(self, var : Variable, right : Expression):
        self.left = left
        self.right = right

class BinaryOperation(AST_Node):
    def __init__(self, left : Expression, operator: Token, right : Expression):
        self.left = left
        self.operator = operator
        self.operator_value = operator.value
        self.right = right

class IfStatement(AST_Node):
    def __init__(self, condition : AST_Node, then_block : Block, else_block : Block):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class FunctionCall(AST_Node):
    def __init__(self, function : Token, args : list[Expression]):
        self.function = function
        self.function_name = function.value
        self.args = args

class ReturnStatement(AST_Node):
    def __init__(self, expression : Expression):
        self.expression = expression

class FunctionDefinition(AST_Node):
    def __init__(self, function : Token, params : list[Variable], body : Block, return_statement : ReturnStatement):
        self.function = function
        self.function_name = function.value
        self.params = params
        self.body = body
        self.return_statement = return_statement
