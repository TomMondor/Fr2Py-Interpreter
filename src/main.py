import argparse

from tokenizer.tokenizer import Tokenizer
from tokens_parser.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.storage import Storage

"""
Main program
Command line input asking for the file path containing the program to run.

TODO: line numbers in the error messages might be wrong, because the tokenizing and parsing ignore blank lines.
"""

def main():
    path = parse_args()

    code = read_file(path)

    run(code)


def parse_args() -> str:
    parser = argparse.ArgumentParser(description='Run the Fr2Py Interpreter.')
    parser.add_argument('path', help='Path/filename of the Fr2Py script', type=str)

    args = vars(parser.parse_args())
    return args["path"]


def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


def run(code: str):
    try:
        tokenized_program = Tokenizer(code).tokenize()

        ast = Parser(tokenized_program).parse()

        Interpreter(ast, Storage()).interpret()
    except Exception as error:
        print(error)



if __name__ == "__main__":
    main()
