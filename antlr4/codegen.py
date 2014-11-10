from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys
import re

import pdb

from tree import Tree


def ctxname(ctx):
    name= str(type(ctx))
    return name[name.find('.')+1:name.find('Context')]

#CPP= [] #List for the generated C++ Code

#globals...
AST= Tree()
AST.add('Prog')
old_depth= 0
leafs= 0
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

        
        d_chg= ctx.depth()-old_depth
        if d_chg<=0:
            print '   BRANCH', d_chg
            AST.up(-d_chg+1)
            for v in AST.pos:
                if not v.name.startswith('_') and v.empty:
                    AST.pos= v
                    break
            pass
        old_depth= ctx.depth()
        name= ctxname(ctx)

        print ctx.depth(),'\t', name, '\t'
        
        for child in ctx.getChildren():            
            if child.getChildCount()==0:
                #name= '_%d_'%leafs + str(child.getText()) +'_' #child.depth() -> ERR
                name= '_' + str(child.getText()) +'_'
                #name= str(child.getText())
                leafs+= 1 
            else:
                name= ctxname(child)
            AST.add(name)
            AST.up()

            print '\t', name,
        print

        for v in AST.pos: print v.name,
        print
        
        #pdb.set_trace()
        for v in AST.pos:
            if not v.name.startswith('_') and v.empty:
                AST.pos= AST.pos[v.name+v.nr]
                break
        #print AST.pos is v
        #ctx.visited= True



def main(argv):
    input = FileStream("programm_.py")
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.prog()

    actions = TreeActions()
    walker = ParseTreeWalker()
    walker.walk(actions, tree)

    #remove underscores and digits from leafs
    AST.pos= AST.root
    for v in AST:
        if v.empty:
            v.name= re.match(r'(.+?)(\d*)$', v.name).groups()[0]
            v.name= v.name[1:-1] #strip _

if __name__ == '__main__':
    main(sys.argv)
