import enum


class Token:
    def __init__(value : str, line_nbr : int):
        self.type = self.get_token_type(value)
        self.value = value
        self.line_nbr = line_nbr

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def get_token_type(self, value : str):
        #TODO return a TokenType (create exception class if no match)
        pass



class TokenType(enum.Enum):
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

    # One or two character tokens.
    NOT_EQUAL = 'pas='
    NOT = 'pas'
    EQUAL = '='
    GREATER = '>'
    GREATER_EQUAL = '>='
    LESS = '<'
    LESS_EQUAL = '<='

    # Literals.
    STRING = 'texte'
    NUMBER = 'nombre'
    BOOLEAN = 'vrai-ou-faux'
    FUNCTION_NAME = 'FUNCTION_NAME'
    VARIABLE_NAME = 'VARIABLE_NAME'

    # Keywords.
    ELSE = 'sinon'
    END_IF = 'fin-si'
    THEN = 'alors'
    IF = 'si'
    OR = 'ou'
    AND = 'et'
    PRINT = 'affiche'
    RETURN = 'retourne'
    FUNCTION = 'fonction'

    # End markers
    EOL = '\n'
    EOF = 'EOF'
