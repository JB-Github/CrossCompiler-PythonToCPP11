from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
import sys
 
def main(argv):
    input = FileStream(argv[1])
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.Prog()
 
if __name__ == '__main__':
    main(sys.argv)
