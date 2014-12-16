from math import *
import string
import re
from collections import namedtuple
import pdb, traceback
import sys

from rx import rx
from common import *



##-----------------------------------------------------------
##Bracket check

def checkpairs(L, pairs):
    """
    checks if every opener has corresponding closer
    pairs= {opener1:closer1, ...}
    """
    I= enumerate(L)
    checkpairs.L= L
    checkpairs.idx= []
    for i,x in I:
        if x in pairs:
            checkclose(I, pairs[x], pairs, i)
    return True
def checkclose(I, close, pairs, i_open):
    for i,x in I:
        #print x,',', checkpairs.L[i]
        if x in pairs:
            checkclose(I, pairs[x], pairs, i)
        elif x==close:
            return True
    #EOF
    raise CompilerError( 'Missing Closer for ',
                        checkpairs.L, i_open, checkpairs.L[i_open] )


##-----------------------------------------------------------
##Indentation

def convert_indent(TL):

    bracket_open= set('([{')
    bracket_close= set(')]}')
    nesting= 0 #current level of bracket nesting

    TL2= []
    Indents= [0] #stack for current indentation level
    for i,t in enumerate(TL):
        #pdb.set_trace()
        assert nesting>=0
        #print nesting
        #if t.str=='list': pdb.set_trace()

        if t.str in bracket_open: nesting+=1
        elif t.str in bracket_close: nesting-=1

        elif t=='space':
            if nesting>0 or i==0:
                TL2.append(t)
                continue
            s= t.str
            ind_start= s.rfind('\n') #Indentation start
            if ind_start==-1 or s[ind_start-1]=='\\':
                TL2.append(t)
                continue

            s= s[ind_start+1:]
            s= s.replace('\t', ' '*4)

            ind= len(s)-sum(Indents) #Indentation change

            #Indent
            if TL[i-1]==':':
                if ind<=0:
                    pdb.set_trace()
                    raise CompilerError("Expected indented block", TL, i)
                else:
                    Indents.append(ind)
                    #TL2[-1]= token('space', ' ') #remove ':'
                    TL2.append( token('blockbegin', '$blockbegin') )
            #Dedent / no change
            else:
                if ind>0:
                    raise CompilerError("Unexpected indentation increase", TL, i)

                elif ind<0:
                    TL2.append( token(';',';') )
                    #comments
                    #pdb.set_trace()
                    ind_nl= t.str.find('\n')
                    TL2.append( token('space', t.str[:ind_nl]) )
                    t= token(t.name, t.str[ind_nl:])

                    while ind<0:
                        ind+= Indents.pop()
                        TL2.append( token('blockend', '\n'+sum(Indents)*' '+'$blockend') )
                    if ind>0:
                        raise CompilerError("Dedentation to incorrect level", TL, i)

                elif ind==0:
                    TL2.append( token(';',';') ) #Statement end

        TL2.append(t)

        #pdb.set_trace()

    return TL2


##-----------------------------------------------------------
#Wrapper

def space2braces(pyfile):
    """
    Inserts tokens for blockbegin and blockend and statement end in "pyfile".
    Generated text is saved in file with the same name and appended underscore
    """

    #pdb.set_trace()

    S= open(pyfile).read()+'\n' #EOF

    S= S.replace('\r\n', '\n') #for portability

    CompilerError.file= pyfile
    CompilerError.phase= 'Lexer'


    TL= rx.lex(S, pattern= 'str keyword var float int space operator op_unused')
    TL= [ t if not t=='operator' else token(t.str,t.str) for t in TL ]

    checkpairs( zip(*TL)[1], dict(zip('([{', ')]}')) )

    TL= convert_indent(TL)

    outfile= pyfile.replace('.py','_.py')
    with open(outfile, 'wb') as F: #Ending?
        F.write( ''.join(zip(*TL)[1]) )

    return outfile

