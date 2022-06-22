from __future__ import annotations
import enum
from tokenizer.token_type_exception import InvalidOperatorException


class Token:
    def __init__(self, line_nbr : int, tokenType: TokenType, value: str = None):
        self.type = tokenType
        self.value = value
        self.line_nbr = line_nbr

    def __str__(self):
        return f"Token[{self.type.name}: '{self.value}']"

    def __repr__(self):
        return self.__str__()

    def has_higher_precedence(self, other: Token):
        if self.type.value not in TokenType.get_operators_values():
            raise InvalidOperatorException(self.type.value, self.line_nbr)
        if other.type.value not in TokenType.get_operators_values():
            raise InvalidOperatorException(other.type.value, other.line_nbr)

        precedences = TokenType.get_operators_precedence()
        self_precedence = precedences[self.type.value]
        other_precedence = precedences[other.type.value]
        return self_precedence <= other_precedence



class TokenType(enum.Enum):
    # Keywords.
    RETURN = 'retourne'
    FUNCTION = 'fonction'
    ELSE = 'sinon'
    END_IF = 'fin-si'
    THEN = 'alors'
    IF = 'si'
    OR = 'ou'
    AND = 'et'

    # Single-character tokens.
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    COMMA = ','
    MINUS = '-'
    PLUS = '+'
    SLASH = '/'
    STAR = '*'
    EXPONENT = '^'
    QUOTE_MARK = '"'
    COMMENT = '#'

    # Logical operators tokens.
    NOT_EQUAL = 'pas='
    NOT = 'pas'
    GREATER_EQUAL = '>='
    GREATER = '>'
    LESS_EQUAL = '<='
    LESS = '<'
    EQUAL = '='

    # Literals.
    STRING = 'texte'
    NUMBER = 'nombre'
    BOOLEAN = 'vrai-ou-faux'
    FUNCTION_NAME = 'FUNCTION_NAME'
    VARIABLE_NAME = 'VARIABLE_NAME'

    # End markers
    EOL = '\n'
    EOF = 'EOF'

    NOT_A_TOKEN = 'NOT_A_TOKEN'

    def get_token_name(self):
        return self.name

    def get_token_value(self):
        return self.value

    @classmethod
    def get_token_type_from_value(cls, value):
        for token in cls:
            if token.value == value:
                return token
        return TokenType.NOT_A_TOKEN

    @classmethod
    def is_valid_token_type(cls, value):
        return cls.get_token_type_from_value(value) != TokenType.NOT_A_TOKEN

    @classmethod
    def get_non_literal_tokens(cls):
        return [token for token in cls if token.value not in ['\n', 'EOF', 'texte', 'nombre', 'vrai-ou-faux', 'FUNCTION_NAME', 'VARIABLE_NAME', 'NOT_A_TOKEN']]

    @classmethod
    def get_non_literal_tokens_values(cls):
        return [token.value for token in cls.get_non_literal_tokens()]

    @classmethod
    def get_non_textual_tokens_values(cls):
        return ['>=', '>', '<=', '<', '=', '+', '-', '*', '/', '^', '(', ')', ',', '"', '#']

    @classmethod
    def get_logical_operators_values(cls):
        return ['>=', '>', '<=', '<', '=', 'pas=', 'pas', 'ou', 'et']

    @classmethod
    def get_arithmetic_operators_values(cls):
        return ['+', '-', '*', '/', '^']

    @classmethod
    def get_operators_values(cls):
        return cls.get_logical_operators_values() + cls.get_arithmetic_operators_values()

    @classmethod
    def get_operators_precedence(cls) -> dict:
        """0 is the highest precedence."""
        return {
            'pas': 0,
            '^': 1,
            '*': 2,
            '/': 2,
            '+': 3,
            '-': 3,
            '>=': 4,
            '>': 4,
            '<=': 4,
            '<': 4,
            '=': 5,
            'pas=': 5,
            'ou': 6,
            'et': 6
        }
