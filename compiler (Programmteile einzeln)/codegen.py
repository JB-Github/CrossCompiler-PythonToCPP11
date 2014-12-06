from antlr4 import *
from pyLexer import pyLexer
from pyParser import pyParser
from pyListener import pyListener
import sys
import re
import cPickle as pickle
from parsetree import Tree, vertex
import pdb


def ctxname(ctx):
    name= str(type(ctx))
    return name[name.find('.')+1:name.find('Context')]

def pyname(S):
    return S.capitalize().rstrip('_')

S= open('py.g4').read()
PL= re.findall(r'\n[ \t]*([a-z]\w*)\s*:', S)
PL.extend( re.findall(r'\s+#([a-z]\w*)\s+', S) ) #ungenau!!
Tree.patterns= {pyname(s) for s in PL}
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

        parent_name= ctxname(ctx)
        print ctx.depth(),'\t', parent_name, '\t'
        #AST.patterns.add(name)

        for child in ctx.getChildren():

            if child.getChildCount()==0: #leaf
                name= str(child.getText())
                #if parent_name=='Str_val': #double quote all strings #Fallunterscheidung!!
                 #   name= '"' + name.strip(name[0]) + '"'
                name= '_'+ name +'_'
            else:
                name= ctxname(child).rstrip('_')


            m= re.match('([^_].*)__is__(.*)$', name)
            if not m:
                AST.add(name)
            else:
                subpat, pat= m.groups()
                AST.add(pyname(pat)) #add labeled pattern as parentpattern
                AST.pos.name= name   #save label in vertex name
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
            #replace comment sign; remove linebreaks, carriage returns
            H.append('//'+s[1:] if s[0]=='#'
                     else s.replace('\\', '').replace('\r\n','\n') )

        elif t.channel==0:
            if H:
                WS.append(''.join(H))
                H=[]
            else:
                WS.append('')
    WS.reverse()
    AST.root.space= WS.pop() # whitespace/comments at program start


    AST.pos= AST.root
    #add additional vertices for patterns with labels
    for v in AST:
        m= re.match('([^_].*)__is__(.*)$', v.name)
        if m:
            subpat, pat= m.groups()

            v.name= subpat
            v0= vertex(pyname(pat), v.parent)
            v0.nr= v.nr
            v0[subpat]= v

            v.parent[v.idx()]= v0
            v.parent= v0
            v.nr= None
    #remove vertices of redundant labels
    for v in AST:
        if v.name.endswith('_label'):
            v2= v[0]
            v2.parent= v.parent

            k= v.parent.keys()[v.idx()]
            v.parent.rename({k:v2.name}, inplace=True)
            v.parent[v2.name]= v2

    #remove underscores and digits from leafs, safe whitespace
    for v in AST:
        if v.empty:
            v.name= re.match(r'(?s)(.+?)(\d*)$', v.name).groups()[0]
            v.name= v.name[1:-1] #strip _
            v.space= WS.pop()
            sys.stdout.write( v.name+v.space )
            #format strings
            if v.parent.name=='Str_val':
                #pdb.set_trace()
                n= v.name
                n= '"' + n.strip(n[0]) + '"'
                v.name= n.replace('\r\n', '\n')

    pickle.dump(AST, open('T.dat', 'wb'))


    print '------------------------------------------------------------'

    AST.visit()
    print ''.join(AST.TL)

    AST.tofile('program.cpp')
