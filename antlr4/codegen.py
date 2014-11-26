from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys
import re
import cPickle as pickle
from tree import Tree, vertex
import pdb

def ctxname(ctx):
    name= str(type(ctx))
    return name[name.find('.')+1:name.find('Context')]

S= open('py.g4').read()
PL= re.findall(r'\n[ \t]*([a-z]\w*)\s*:', S)
PL.extend( re.findall(r'\s+#([a-z]\w*)\s+', S) ) #ungenau!!
Tree.patterns= {s.capitalize().rstrip('_') for s in PL}
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
        #AST.patterns.add(name)

        for child in ctx.getChildren():
            if child.getChildCount()==0: #leaf            
                name= '_' + str(child.getText()) +'_'
            else:
                name= ctxname(child).rstrip('_')
            AST.add(name)
            AST.up()

            ##Control-Prints
            print '\t', name,
        print

        for v in AST.pos: print v.name,
        print


        for v in AST.pos:
            if not v.name.startswith('_') and v.empty:
                AST.pos= v #AST.pos[v.name+v.nr]
                break
        #print AST.pos is v



if __name__ == '__main__':
    input = FileStream("programm_.py")
    lexer = pyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pyParser(stream)
    tree = parser.prog()


    actions = TreeActions(stream)
    walker = ParseTreeWalker()

    #pdb.set_trace()
    console= sys.stdout; sys.stdout= open('out', 'wb')
    walker.walk(actions, tree)
    sys.stdout.close(); sys.stdout= console
    

    #get whitespace (and comments) to the right of each leaf/token
    Tk= actions.tokens.tokens
    WS=[] #whitespace
    H=[] #hidden tokens
    for t in Tk:
        if t.channel==1:
            s=str(t.text)
            H.append('//'+s[1:] if s[0]=='#'
                     else s.replace('\\', '') ) #remove linebreaks
        elif t.channel==0:
            if H:
                WS.append(''.join(H))
                H=[]
            else:
                WS.append('')
    WS.reverse()
    WS.pop() # whitespace at program start

    
    #remove underscores and digits from leafs, safe whitespace
    AST.pos= AST.root
    for v in AST:
        if v.empty:
            v.name= re.match(r'(.+?)(\d*)$', v.name).groups()[0]
            v.name= v.name[1:-1] #strip _
            v.space= WS.pop()
            sys.stdout.write( v.name+v.space )
    pickle.dump(AST, open('T.dat', 'wb'))


    print '------------------------------------------------------------'

    AST.visit()
    print ''.join(AST.TL)
