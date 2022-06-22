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
_abc = 4+5*6/2 + 3^4 - 3*(2+3)
affiche(_abc)
_abc = "le caractère # est permis dans les strings" # et le caractère " est permis dans des commentaires
x = demande("Quel est ton chiffre favori?")
si x < 3
alors
    affiche(x, "est plus petit que 3")
sinon
    affiche(x, "is greater than 3")
fin-si
si x = 3
alors
    affiche("J'adore 3 aussi!")
fin-si
maVariable1 = 2 + 3 * 4 # ceci est un commentaire, this is a comment
maVariable2 = maVariable1 >= 17 et maVariable1 pas= 17
maVariable3 = 3 / 2 #maVariable3 = 1.5
maVariable4 = "du texte..." + " some text"

_expression = 2 + 4 * 5 - 3 * (2 + 3)
si _expression pas= 7
alors
    affiche(_expression, "devrait être égal à 7")
    affiche("gros problème!!!!!")
fin-si

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

#bel et bien détectés par le parser
# bug = maFonction1 "syntaxe invalide"
# bug = "syntaxe invalide" + 34
# bug = "syntaxe invalide" * "syntaxe invalide"
# bug = "syntaxe invalide" & "syntaxe invalide"
# 3 = "syntaxe invalide"
"""

tokenized_program = Tokenizer(sample_code).tokenize()

ast = Parser(tokenized_program).parse()
# print(str(ast))

Interpreter(ast, Storage()).interpret()
