from tokenizer.tokenizer import Tokenizer
from tokens_parser.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.storage import Storage

"""
Main program
Will eventually offer a command line input asking for the file path containing the program to run.
A GUI could also be provided in the future.

TODO: line numbers in the error messages might be wrong, because the tokenizing and parsing ignore blank lines.
"""

sample_code = """
a = "Hello World"
b = 123.43
#c = a + b # invalid operation
affiche(a, "or Hello There")
abc = "le caractère # est permis dans les strings" # et le caractère " est permis dans des commentaires
x = demande("Quel est ton chiffre favori?")
si x < 3
alors
    affiche(x, "est plus petit que 3")
sinon
    affiche(x, "is greater than 3")
fin-si
maVariable1 = 2 + 3 * 4 # ceci est un commentaire, this is a comment
maVariable2 = maVariable1 >= 17 et maVariable1 pas= 17
maVariable3 = 3 / 2 #maVariable3 = 1.5
maVariable4 = "du texte..." + " some text"

fonction maFonction1(x, y, z)
    retourne x + y + z

fonction volume(x, y, z)
    maFonction1(x, y, z)
    retourne x * y * z

fonction quelconque(x, y, z)
    x = maFonction1(x, y, z)
    y = volume(x, y, z)
    retourne x / y

qqch = quelconque(1, 2, 3)
affiche("qqch = ", qqch)

somme = maFonction1(1.5, b, 32)
affiche("somme devrait être '156.93' et est :", somme)

#bug = maFonction1 "syntaxe invalide" #bel et bien détecté par le parser
"""

tokenized_program = Tokenizer(sample_code).tokenize()

ast = Parser(tokenized_program).parse()
# print(str(ast))

Interpreter(ast, Storage()).interpret()
