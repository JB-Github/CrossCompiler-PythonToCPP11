from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyClasses import pyClasses
import sys

def main(argv):
    input = FileStream(argv[1])
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.prog()

    printer = pyClasses()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
