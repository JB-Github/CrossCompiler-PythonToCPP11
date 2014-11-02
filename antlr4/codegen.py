from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys

CPP= [] #List for the generated C++ Code

class TreeActions(pyListener):
    def exitNumber(self, ctx):
        CPP.append(ctx.getChild(0));

    def exitFor_(self, ctx):
        print "for test"

    def enterString(self, ctx):
        print "Enter Str"
    def exitString(self, ctx):
        print ctx.getChild(0)



def main(argv):
    input = FileStream("programm_.py")
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.prog()

    actions = TreeActions()
    walker = ParseTreeWalker()
    walker.walk(actions, tree)

    #print CPP

if __name__ == '__main__':
    main(sys.argv)
