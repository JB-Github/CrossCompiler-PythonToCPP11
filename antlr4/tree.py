import pandas as pd
import numpy as np
import pdb
import re
from copy import deepcopy
import cPickle as pickle

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
            #if k[-1].isdigit(): #for insert
             #   k = re.match(r'(.+?)\d*$', k).groups()[0] #strip number

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


##-----------------------------------------------------------
##Tree Classes

class vertex(NamedList):
    def __init__(self, name= None, parent= None,
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
        for v in self:
            for w in v.walk():
                yield w

    def text(self):
        """returns a list of the text in the leafs"""
        return [v.name for v in self.walk() if v.empty]

    def visit(self):

        if self.name in Tree.actions:
            Tree.actions[v.name](self)

        for v in self:
            v.visit()




class Tree(object):
    actions= {} #??

    def __init__(self, S=None):
        self.root= vertex('root')
        self.pos= self.root

        self.patterns= set()

    def __iter__(self):
        return self.pos.walk()

    def add(self, k, rename=True):
        nr= self.pos.add(k, vertex(k, self.pos))
        self.pos= self.pos[k+nr]
        self.pos.nr= nr

    def up(self, n=1):
        self.pos= self.pos.up(n)

    def text(self):
        """starting at pos, returns a list of the text in the leafs"""
        return self.pos.text()

    def visit():

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
    vtx.text()


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

print T.root.text()
"""
if __name__ == '__main__':
    T= pickle.load(open('T.dat'))

