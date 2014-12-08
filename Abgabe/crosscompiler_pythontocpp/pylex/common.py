
from math import *
import string
import re
from collections import namedtuple
import pdb, traceback
import sys


##allgemein
def display(I):
    """prints elements of Iterable on seperate lines"""
    t= type(I)
    if t==dict:
        for kv in I.items():
            print '%s\t%s'%kv
    else:
        for x in I:
            print x
def file2set(File):
    with open(File) as F:
        return set(x for x in F.read().split() if x[0]!='#')

def showpos(S,i):
    if hasattr(S, '__iter__'):
        if type(S[0])==token:
            L= zip(*S)[1]
        else:
            L= S
        S= ''.join(L)
        i= len (''.join(L[:i+1]))

    else: i+=1 #?

    lstart= S.rfind('\n', 0,i)+1
    lend= S.find('\n', i)

    lnr= S[:i].count('\n')+1
    cnr= i-lstart # 0-Indexing of columns
    pointer= ' '*(cnr-1)+'^'

    for j in range(3):
        lstart= S.rfind('\n', 0, max(0,lstart))
    line= S[lstart+1:lend]

    sep= '-'*77
    return """\
line {lnr}, col {cnr}:
{sep}
{line}
{pointer}""".format(**locals())


class CompilerError(Exception):
    file= ''
    phase=''
    def __init__(self, message, S,i,w=''):

        pdb.set_trace()

        linepointer= showpos(S,i)
        sep= '-'*77

        message= """
{sep}
 {self.phase}, File "{self.file}", {linepointer}
  ERR: {message} {w} """.format( **locals() )
        Exception.__init__(self, message)

token= namedtuple('token', ('name', 'str'))
token.__repr__= lambda t: t.name.ljust(8)+'\t'+repr(t.str)
token.__eq__= lambda t, s: t.name==s


##-----------------------------------------------------------
##Pairs

def findpairs(L, i=0, n=-1):
    """
    ckecks if every opener has corresponding closer
    findpairs.pairs= {opener1:closer1, ...}
    """
    findpairs.L= L
    findpairs.idx= []
    I= enumerate(L[i:],i)
    for i,x in I:
        if x in findpairs.pairs:
            findclose(I, findpairs.pairs[x], i)
            n-=1
            if n==0: break
    return sorted(findpairs.idx, key= lambda t: t[0])

def findclose(I, close, i_open):
    for i,x in I:
        #print x,',', findpairs.L[i]
        if x==close:
            findpairs.idx.append((i_open,i))
            return True
        if x in findpairs.pairs:
            findclose(I, findpairs.pairs[x], i)
    #EOF
    raise CompilerError( 'Missing Closer for ',
                        findpairs.L, i_open, findpairs.L[i_open] )

findpairs.pairs= dict(zip('([{', ')]}'))
#findpairs( zip(*TL)[1])
