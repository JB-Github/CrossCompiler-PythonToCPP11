from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys

import pdb

import antlr4.tree as at



CPP= [] #List for the generated C++ Code


class TreeActions(pyListener):
    
    """
    def exitNumber(self, ctx):
        #pdb.set_trace()
        CPP.append(ctx.getChild(0))
        #print ctx.ID()

    def exitFor_(self, ctx):
        pdb.set_trace()
        print "for test"

    def enterString(self, ctx):
        print "Enter Str"
    def exitString(self, ctx):
        print ctx.getChild(0)
"""
    def enterEveryRule(self, ctx):
        global old_depth, leafs

        
        #print ctx.getChild(0)
        #print 'EVERY'




def main(argv):
    input = FileStream("programm_.py")
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.prog()

    actions = TreeActions()
    walker = ParseTreeWalker()
    walker.walk(actions, tree)

    pdb.set_trace()

    # assume we are parsing Java
    #ParserRuleContext
    tree = parser.prog()#compilationUnit()
    #String
    #xpath = "//blockStatement/*" # get children of blockStatement
    xpath = r"//block/*"
    #String
    treePattern = "<expr> + <expr>"
    #ParseTreePattern
    p = parser.compileParseTreePattern(treePattern,   
            pyParser.RULE_expr)
    #List<ParseTreeMatch>
    matches = p.findAll(tree, xpath)
    print matches

    #print CPP

if __name__ == '__main__':
    main(sys.argv)
