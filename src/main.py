from tokenizer.tokenizer import Tokenizer
from tokens_parser.parser import Parser

"""
Main program
Will eventually offer a command line input asking for the file path containing the program to run.
A GUI could also be provided in the future.

TODO: line numbers in the error messages might be wrong, because the tokenizing and parsing ignore blank lines.
"""

sample_code = """
a = "Hello World"
b = 123.43
c = a + b # invalid operation
abc = "le caractère # est permis dans les strings" # et le caractère " est permis dans des commentaires
x = demande("Quel est ton chiffre favori")
si x < 3
alors
    affiche(x, "est plus petit que 3")
sinon
    affiche(x, "is greater than 3")
fin-si
maVariable1 = 2 + 3 * 4 # ceci est un commentaire, this is a comment
maVariable2 = maVariable1 >= 17 et pas= 17
maVariable3 = 3 / 2 #maVariable3 = 1.5
maVariable4 = "du texte..." + " some text"

fonction maFonction1(x, y, z)
    retourne x + y + z

somme = maFonction1(1.5, b, 32)

bug = maFonction1 "syntaxe invalide"
"""

the_tokenizer = Tokenizer(sample_code)
tokenized_program = the_tokenizer.tokenize()

the_parser = Parser(tokenized_program)
ast = the_parser.parse()
