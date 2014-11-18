import pandas as pd
import numpy as np
import pdb
import re
from copy import deepcopy
import cPickle as pickle
import collections

from pylex.rx import rx
rx['other']= '.'
rx['space']= '\s'
rx['optvar']= "var '?'?"

##-----------------------------------------------------------
##Basic Data-Structure

class NamedList(pd.Series):
    """Ordered Key-Value List"""
    def add(self, k, v, rename=True):
        """appends new entry and numbers duplicate names"""
        nr=''
        if not rename:
            #pdb.set_trace()
            S= self.append(pd.Series([v],[k]))
            self.__init__( S )
        else:
            if k[-1].isdigit(): #for insert
                k = re.match(r'(.+?)\d*$', k).groups()[0] #strip number

            rep= sum( 1 for x in self.keys() if re.match(re.escape(k)+r'\d*$', x) )
            if rep:
                if rep==1:
                    self.rename({k:k+'1'}, inplace=True)
                    #self.rename(lambda x: x+'1' if x==k else x, inplace=True)
                nr= str(rep+1)
            self[k+nr]= v
        return nr

    def insert(self, S, i, rename= False):
        """inserts new entry(s) before index/name i"""
        if type(S)!=pd.Series: #2-tuple
            S= pd.Series([S[1]], [S[0]])
            #S= pd.Series(*zip(*S))
        if type(i)==str:
            i= np.where(self.keys()==i)[0][0]

        if not rename:
            self.__init__(self[:i].append(S).append(self[i:]))
        else:
            head= NamedList(self[:i].copy())
            tail= S.append(self[i:])
            for x in tail.iteritems():
                head.add(*x)
            self.__init__(head)

    def append(self, x, verify_integrity=False):
        if type(x)==dict:
            x= pd.Series(x)
        return super(NamedList, self).append(x, verify_integrity)


##-----------------------------------------------------------
##Tree Classes

class vertex(NamedList):
    def __init__(self, name= None, parent= None, space='', #name=''?
                 data=None, index=None, dtype= object, #dtype?
                 Name=None, copy=False, fastpath=False):
        #name->Name
        if type(name)!=str:
            super(vertex, self).__init__(name, index, dtype, Name, copy, fastpath)
            return

        super(vertex, self).__init__(data, index, dtype, Name, copy, fastpath)

        self.parent= parent
        if name and name[-1].isdigit(): #??
            self.name, self.nr = re.match(r'(.+?)(\d*)$', name).groups()
        else:
            self.name= name
            self.nr= None
        self.space= space

    def __eq__(self, S):
        return S==self.name

    def rename(self, old, new=None, inplace=True):
        """changes (unique) keyname in children of vertex"""
        if new is None:
            old, new= old.items()[0]
        self.__init__(super(vertex, self).rename({old:new}))
        self[new].nr= re.match(r'(.+?)(\d*)$', new).groups()[1]

    def idx(self): # -> nr unnoetig
        for i,v in enumerate(self.parent):
            if self is v:
                return i

    def up(self, n=1):
        if n==0:
            return self
        return self.parent.up(n-1)

    def walk(self):
        """iterates over all vertices"""
        yield self
        """
        brk= yield self
        if brk:
            print '   BRK'
            exc
        """
        for v in self:
            for w in v.walk():
                yield w


    def dfind(self, S):
        D= collections.defaultdict(str)
        self._dfind(S, D)
        return D
    def _dfind(self, S, D):
        for v in self:
            if v==S:
                D[S+str(len(D)+1)]= v
            else:
                v._dfind(S, D)


    def find(self, S, nmax=0):
        L= []
        self._find(S, L)
        #L.extend(['']*(nmax-len(L)))
        L.extend(vertex() for i in range(nmax-len(L)))
        return L
    def _find(self, S, L):
        for v in self:
            if v==S:
                L.append(v)
            else:
                v._find(S, L)

    def literals(self):
        """returns a list of the translated text in the leafs"""
        return [v.name for v in self.walk() if v.empty]
    def words(self): #tauschen!
        """returns a list of the literal text in the leafs"""
        L=[]
        Tree.out= L
        self.visitchildren()
        Tree.out= Tree.TL
        """
        temp= Tree.write
        Tree.write= lambda Tree,x: L.append(x)
        self.visitchildren()
        Tree.write= temp
        """
        return L
    def text(self):
        """returns a string of the translated text in the leafs"""
        return ''.join(self.words())

    def transform(self, S, D=()):
        TL= rx.lex(S, 'optvar str space other')
        for t in TL:
            s= t.str
            
            #rules
            if t=='optvar':
                #pdb.set_trace()
                opt= 0
                if s.endswith('?'):
                    opt= 1
                    s= s[:-1]
                    
                if s in D:
                    v= D[s]
                    if type(v)==str and v:
                        Tree.write(v)
                        continue
                else:
                    v= self.get(s, '')
                    
                if v=='':
                    if opt:
                        continue
                    raise Exception('\n\tNo rule "%s" in vertex "%s"'%(s,self.name))
                v.visit()
            #literals  
            elif t=='str':
                s= s.strip(s[0])
                Tree.write(s)
            #delimiter
            elif s=='~':
                continue
            #other
            else:
                Tree.write(s)

    def visitchildren(self):
        for v in self:
            v.visit()

    def visit(self):

        if self.name in Tree.actions:
            Tree.actions[self.name](self)
        #Leaf
        elif self.empty:
            Tree.write(self.name)

        else:
            self.visitchildren()

    def startvisit(self):
        pdb.set_trace()
        Tree.TL=[] #Problem mit static/global!
        Tree.out= Tree.TL
        self.visit()




class Tree(object):
    actions= {} #??
    TL= [] #List for translated text
    out= TL
    file= open('tout.txt','wb')
    #file= open('tout.txt', 'a+b')
    def __init__(self, S=None):
        self.root= vertex('root')
        self.pos= self.root

        self.patterns= set()

        Tree.out= Tree.TL

    def __iter__(self):
        return self.pos.walk()

    @staticmethod
    def write(S):
        Tree.file.write(S+'\n')
        Tree.out.append(S)
    @staticmethod
    def writeto(L=None): #besser??
        Tree.out= Tree.TL if L is None else L

    def add(self, k, rename=True):
        nr= self.pos.add(k, vertex(k, self.pos))
        self.pos= self.pos[k+nr]
        self.pos.nr= nr

    def up(self, n=1):
        self.pos= self.pos.up(n)

    def words(self):
        """starting at pos, returns a list of the translated text in the leafs"""
        return self.pos.words()


    def visit(self):
        open('tout.txt', 'wb').close()
        Tree.file= open('tout.txt', 'a+b')
        pdb.set_trace()
        Tree.TL=[]
        Tree.out= Tree.TL
        self.pos.visit()





def tree_action(L):
    def wrapper(func):
        M=L #nonlocal
        if type(M)==str:
            M= M.split()
        for x in M:
            tree_action.dict[x]= func
    return wrapper
tree_action.dict= Tree.actions

@tree_action('Number')
def f(vtx):
    #vtx.text()
    print 'Num'
    vtx.visitchildren()

@tree_action('For')
def f(vtx):
    print 'For'
    EL= vtx.Exprlist
    var= vtx.Varlist.words()
    assert len(var)==1
    var= ''.join(var)

    #for-each
    if EL.literals()[0]!='range':
        vtx.transform("'for' ('auto' var : Exprlist)", locals())
        
    #for-range
    else:
        #pdb.set_trace()
        start,stop,step = [v.text().strip()
                           for v in EL.Expr.Arglist.find('Expr', 3)]
        if not stop:
            start,stop = stop,start
        start= 'int '+var+'= '+ (start or '0')

        comp= '<'
        if step:
            if step[0]=='-': comp= '>'
            step= var+'+='+step
        else:
            step= var+'++'
        stop= var+comp+stop

        vtx.transform("'for' (start; stop; step)", locals())


"""
##Tests

N= NamedList( range(3), 'a b c'.split())
N.add('a', 111)

N.insert(('f', 777), 'b', 1)
N.insert(('a', 177), 'b', 1)


T= Tree()
for v in 'expr func ert'.split():
    T.add(v)
T.up()
T.add('(')
T.pos= T.root
T.add('expr')
T.up()
T.add('expr')
T.add('expr')

def g(D):
    for k,v in D.items():
        print k,v
def f():
    a=3
    b=4
    def h():
        c=11
        g(locals())

def str_maybe(S, default=''):
    pass

def maybe(C, idx, default=''):
    try:
        return D[idx]
    except KeyError, IndexError:
        return default


print T.root.text()
"""
if __name__ == '__main__':
    
    T= pickle.load(open('T.dat'))
    map(id, [Tree.TL, Tree.out, T.TL, T.out])

