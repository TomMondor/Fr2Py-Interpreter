import re
from typing import Union
from tokenizer.tokens import *
from tokenizer.token_type_exception import TokenTypeException


class Tokenizer:
    """Tokenizer/Lexer class for the language.
        Relies on the Token class.
    """
    def __init__(self, input_string : str):
        self.raw_program = input_string
        self.current_line = ""
        self.tokenized_program : list[Token] = []

    def __str__(self):
        output = "\n"
        for token in self.tokenized_program:
            output += str(token)
            output += " " if token.type != TokenType.EOL else "\n"
        return output

    def print_brief(self):
        for token in self.tokenized_program:
            end_char = " " if token.type != TokenType.EOL else "\n"
            print(token.type.name + ":" + token.value, end=end_char)

    def tokenize(self):
        lines = self.raw_program.split('\n')
        for line_nbr, line in enumerate(lines):
            raw_tokens = self.evaluate_strings_and_comments(line, line_nbr)
            for raw_token in raw_tokens:
                if isinstance(raw_token, Token):
                    self.append(raw_token)
                else:
                    self.parse_raw_token(raw_token, line_nbr)
            self.append(Token(line_nbr, TokenType.EOL, "\\n"))
        self.append(Token(len(lines), TokenType.EOF, "EOF"))
        return self.tokenized_program

    def parse_raw_token(self, raw_token : str, line_nbr : int):
        if TokenType.is_valid_token_type(raw_token):
            tokenType = TokenType.get_token_type_from_value(raw_token)
            self.append(Token(line_nbr, tokenType, raw_token))
            return
        elif self.is_valid_identifier(raw_token): 
            tokenType = self.get_identifier_type(raw_token)
            self.append(Token(line_nbr, tokenType, raw_token))
            return
        elif self.is_valid_number(raw_token):
            self.append(Token(line_nbr, TokenType.NUMBER, raw_token))
            return
        else:
            for possible_token in TokenType.get_non_litteral_tokens_values():
                index = raw_token.find(possible_token)
                if index != -1:
                    before, token, after = raw_token.partition(possible_token)
                    self.parse_raw_token(before, line_nbr) if (before != "") else None
                    self.append(Token(line_nbr, TokenType.get_token_type_from_value(token), token))
                    self.parse_raw_token(after, line_nbr) if (after != "") else None
                    return
                    return
            #si ne match rien
            raise TokenTypeException(raw_token, line_nbr)

    def is_valid_identifier(self, value : str) -> bool:
        return re.fullmatch(r"^[a-zA-Z_][a-zA-Z0-9_]*$", value) and value not in TokenType.get_non_litteral_tokens_values()

    def is_valid_number(self, value : str) -> bool:
        return re.fullmatch(r"^-?(([0-9]+\.?[0-9]+)|([0-9]+))$", value)

    def append(self, token : Token) -> None:
        self.tokenized_program.append(token)

    def get_identifier_type(self, raw_token : str) -> TokenType:
        if self.tokenized_program[-1].type == TokenType.FUNCTION:
            return TokenType.FUNCTION_NAME
        else:
            return TokenType.VARIABLE_NAME

    def evaluate_strings_and_comments(self, line : str, line_nbr : int) -> list[Union[str, Token]]:
        """Tokenizes strings in a code line and removes comments.

        Args:
            line (str): line of code.
            line_nbr (int): line number.

        Raises:
            StringLitteralException: If there is an incomplete string in the line (missing a closing quote).

        Returns:
            list[Union[str, Token]]: List of raw tokens (strings) and STRING tokens.
        """
        tokens = []
        while line != "":
            before, quote, after = line.partition('"')
            if self.contains_comment(before):
                tokens.extend(self.drop_comment(before).split())
                return tokens
            tokens.extend(before.split())
            if quote == '"':
                in_string, quote, after = after.partition('"')
                if quote != '"':
                    raise StringLitteralException(in_string, line_nbr)
                tokens.append(Token(line_nbr, TokenType.STRING, in_string))
            line = after
        return tokens

    def contains_comment(self, line : str) -> bool:
        return line.count("#") > 0

    def drop_comment(self, line : str) -> str:
        return line[:line.find("#")]
