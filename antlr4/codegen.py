from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys
import re
import cPickle as pickle
from tree import Tree
import pdb

def ctxname(ctx):
    name= str(type(ctx))
    return name[name.find('.')+1:name.find('Context')]


AST= Tree()
AST.add('Prog')
old_depth= 0

class TreeActions(pyListener):
    
    """
    def enterString(self, ctx):
        print "Enter Str"
    def exitString(self, ctx):
        print ctx.getChild(0)
    """

    def __init__(self, tokens):
        self.tokens= tokens
    def enterEveryRule(self, ctx):
        global old_depth
       
        d_chg= ctx.depth()-old_depth
        if d_chg<=0:
            print '   BRANCH', d_chg
            AST.up(-d_chg+1)
            for v in AST.pos:
                if not v.name.startswith('_') and v.empty:
                    AST.pos= v
                    break
        old_depth= ctx.depth()
        
        name= ctxname(ctx)
        print ctx.depth(),'\t', name, '\t'
        AST.patterns.add(name)
        
        for child in ctx.getChildren():            
            if child.getChildCount()==0: #leaf
                #pdb.set_trace()
                self.tokens.getHiddenTokensToRight(ctx.start.tokenIndex, pyLexer.HIDDEN)
                name= '_' + str(child.getText()) +'_'
                #name= str(child.getText())
            else:
                name= ctxname(child).rstrip('_')
            AST.add(name)
            AST.up()

            ##Control
            print '\t', name,
        print

        for v in AST.pos: print v.name,
        print

        
        for v in AST.pos:
            if not v.name.startswith('_') and v.empty:
                AST.pos= v #AST.pos[v.name+v.nr]
                break            
        #print AST.pos is v



#def main(argv):
if __name__ == '__main__':
    input = FileStream("programm_.py")
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.prog()

    
    actions = TreeActions(stream)
    walker = ParseTreeWalker()

    pdb.set_trace()
    console= sys.stdout; sys.stdout= open('out', 'wb')
    walker.walk(actions, tree)
    sys.stdout.close(); sys.stdout= console
    
    #remove underscores and digits from leafs
    AST.pos= AST.root
    for v in AST:
        if v.empty:
            v.name= re.match(r'(.+?)(\d*)$', v.name).groups()[0]
            v.name= v.name[1:-1] #strip _

    pickle.dump(AST, open('T.dat', 'wb'))
    
    
#if __name__ == '__main__':
 #   main(sys.argv)
