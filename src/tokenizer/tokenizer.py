import tokens


class Tokenizer:
    """Tokenizer/Lexer class for the language.
        Relies on the Token class.
    """
    def __init__(self, input_string : str):
        self.raw_program = input_string
        self.tokenized_program = []

    def tokenize(self):
        lines = self.raw_program.split('\n')
        for line_nbr, line in enumerate(iterable)(lines):
            raw_tokens = line.split(' ')
            for raw_token in raw_tokens:
                token = self.get_token(raw_token, line_nbr)
                self.tokenized_program.append(token)

    def get_token(self, raw_token : str, line_nbr : int):
        return tokens.Token(raw_token, line_nbr)
