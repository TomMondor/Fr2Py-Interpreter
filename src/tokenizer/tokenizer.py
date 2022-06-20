from utils.utils import is_valid_number, is_valid_identifier
from typing import Union
from tokenizer.tokens import *
from tokenizer.token_type_exception import TokenTypeException, StringLiteralException


class Tokenizer:
    """Tokenizer/Lexer class for the language.
        Relies on the Token class.
    """
    def __init__(self, input_string : str):
        self.raw_program = input_string
        self.current_line = ""
        self.tokenized_program : list[list[Token]] = [[]]

    def __str__(self):
        output = "\n"
        for line in self.tokenized_program:
            for token in line:
                output += str(token)
                output += " "
            output += "\n"
        return output

    def print_brief(self):
        for line in self.tokenized_program:
            for token in line:
                print(token.type.name + ":" + token.value, end=" ")
            print("\n")

    def tokenize(self):
        lines = self.raw_program.split('\n')
        for line_nbr, line in enumerate(lines):
            raw_tokens = self.evaluate_strings_and_comments(line, line_nbr)
            for index, raw_token in enumerate(raw_tokens):
                if isinstance(raw_token, Token):
                    self.append(raw_token)
                else:
                    next_raw_token = raw_tokens[index + 1] if (index + 1) < len(raw_tokens) else ""
                    self.parse_raw_token(raw_token, line_nbr, next_raw_token)
            self.end_program_line()
        self.append(Token(len(lines), TokenType.EOF, "EOF"))
        return self.tokenized_program

    def parse_raw_token(self, raw_token : str, line_nbr : int, next_raw_token : str) -> None:
        if TokenType.is_valid_token_type(raw_token):
            tokenType = TokenType.get_token_type_from_value(raw_token)
            self.append(Token(line_nbr, tokenType, raw_token))
            return
        elif self.is_valid_identifier(raw_token): 
            tokenType = self.get_identifier_type(raw_token, next_raw_token)
            self.append(Token(line_nbr, tokenType, raw_token))
            return
        elif is_valid_number(raw_token):
            self.append(Token(line_nbr, TokenType.NUMBER, raw_token))
            return
        else:
            for possible_token in TokenType.get_non_literal_tokens_values():
                index = raw_token.find(possible_token)
                if index != -1:
                    before, token, after = raw_token.partition(possible_token)
                    self.parse_raw_token(before, line_nbr, token) if (before != "") else None
                    self.append(Token(line_nbr, TokenType.get_token_type_from_value(token), token))
                    self.parse_raw_token(after, line_nbr, token) if (after != "") else None
                    return
            #if nothing matches
            raise TokenTypeException(raw_token, line_nbr)

    def is_valid_identifier(self, value : str) -> bool:
        return is_valid_identifier(value) and value not in TokenType.get_non_literal_tokens_values()

    def append(self, token : Token) -> None:
        self.tokenized_program[-1].append(token)

    def end_program_line(self) -> None:
        if self.tokenized_program[-1] != []:
            self.tokenized_program.append([])

    def get_identifier_type(self, raw_token : str, next_raw_token : str) -> TokenType:
        if len(self.tokenized_program[-1]) > 0 and self.tokenized_program[-1][-1].type == TokenType.FUNCTION:
            return TokenType.FUNCTION_NAME
        elif isinstance(next_raw_token, str) and next_raw_token.startswith("("):
            return TokenType.FUNCTION_NAME
        else:
            return TokenType.VARIABLE_NAME

    def evaluate_strings_and_comments(self, line : str, line_nbr : int) -> list[Union[str, Token]]:
        """Tokenizes strings in a code line and removes comments.

        Args:
            line (str): line of code.
            line_nbr (int): line number.

        Raises:
            StringLiteralException: If there is an incomplete string in the line (missing a closing quote).

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
                    raise StringLiteralException(in_string, line_nbr)
                tokens.append(Token(line_nbr, TokenType.STRING, in_string))
            line = after
        return tokens

    def contains_comment(self, line : str) -> bool:
        return line.count("#") > 0

    def drop_comment(self, line : str) -> str:
        return line[:line.find("#")]
