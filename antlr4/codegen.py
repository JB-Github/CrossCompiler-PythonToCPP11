from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys

CPP= [] #List for the generated C++ Code

class TreeActions(pyListener):
    def exitNumber(self, ctx):
        #CPP.append(ctx.getChild(0))
        pass

    def exitFor_(self, ctx):
        #print "for test"
        pass

    def enterString(self, ctx):
        #print "Enter Str"
        pass

    def exitString(self, ctx):
        pass

    def enterFunc(self, ctx):
        print ctx.isinstance()

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
