import slp_lexer
import slp_parser
import slp_interpreter

from sys import *


lexer = slp_lexer.BasicLexer()
parser = slp_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    slp_interpreter.BasicExecute(tree, env)
