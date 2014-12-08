from math import *
import string
import re
from collections import namedtuple
import pdb, traceback
import sys
import os

from common import *


##regular expressions
re_pattern= type(re.compile(''))

def re_pair(start,end=None):# unescaped=True
    if end is None:
        end=start
    return r'(?<![^\\]\\)\%s.*?(?<![^\\]\\)\%s'%(start, end)


class ReColl(object):
    """Collector for re expressions"""

    def __init__(self, File=None):
        self.dict= {}

    def __call__(self, string):
        """translate string to re_pattern"""
        return re.compile(string)

    def __setitem__(self, name, re_str):
        """adds new regex"""
        self.dict[name]= re_str
        setattr(self, name, self(re_str))
    def __getitem__(self, name):
        """returns regex string"""
        #return self.dict[name]
        return self.__dict__[name]
    def __iter__(self):
        return (
            (n,r) for n,r in self.__dict__.items()
            if not n.startswith('__') and type(r)==re_pattern
        )

    def update(self):
        """adds new string attributes as regular expressions"""
        #Save re name and string
        self.dict.update({
            n:s for n,s in self.__dict__.items()
            if not n.startswith('__') and type(s)==str
        })
        #Compile regular expressions
        for n,s in self.dict.items():
            setattr(self, n, self(s))

    def lex(self, S, pattern=None, ignore=[], Any=False):
        """lexes String with given grammar"""
        Tokens= []

        #updaten!!
        """
        else:
            if type(pattern)==str:
                PL= pattern.split()

                if PL[-1]=='any':
                    Any= True
                    PL.pop()

                for i,p in enumerate(PL):
                    if p[0]=='!':
                        np= p[1:]
                        PL[i]= np
                        ignore.append(np)

                PL= [(n,self[n]) for n in PL]
        """

        if pattern.endswith(' any'):
            Any= True
            pattern= pattern.rstrip('any').rstrip()

        PL= []
        if pattern is None:
            PL= list(self)
        for p in pattern, ignore:
            if type(p)==str:
                PL.extend((n,self[n]) for n in p.split())
                if p is ignore:
                    ignore= ignore.split()

        #Any= False

        i=0
        while i<len(S):
            #pdb.set_trace()
            m= None
            for name, pat in PL:
                m= pat.match(S[i:])
                if m:
                    w= m.group()
                    #print w
                    i+= len(w)
                    if name not in ignore:
                        Tokens.append(token(name, w))
                        #print Tokens[-1]
                    break
            if not m:
                if Any:
                    AL=[S[i]]
                    i+=1
                    while i<len(S) and not any(p.match(S[i:]) for n,p in PL):
                        AL.append(S[i])
                        i+=1
                    Tokens.append( token('any', ''.join(AL)) )
                #print 'Unknown character "%s"'%S[i]
                else:
                    Tokens.append(token('Unknown char', S[i]))
                    i+=1

        return Tokens


class RxColl(ReColl):
    """Collector for rx expressions"""
    def __init__(self, File=None):
        self.dict= {}
        if File: self.addfile(File)

    def re(self, T):
        """translate rx string to re string"""
        #print '----------------------rx----------------------', T
        if not T:
            return T
        if type(T)==str:
            T= regex.lex(T,
                pattern= 'brackets_sq brackets_curl str var esc_sequence flag',
                ignore= 'comment whitespace'
            )

        #pdb.set_trace()
        #assert type(T[0])==token

        for i,(n,s) in enumerate(T):
            if n=='str':
                s= re.escape(s[1:-1])
            elif n=='brackets_curl':
                #s= re.sub(r'[^\w\s]', '', s) #Sonderzeichen?
                s= s.strip()[1:-1]
                s= '('+ '|'.join( map(re.escape, s.split()) ) +')'
            elif n=='var':
                s= '('+ self.re(self.dict[s]) +')'

            if n!='str':
                s= s.strip()
            T[i]= token(n, s)


        return ''.join(s for n,s in T)

    def __call__(self, T):
        """translate string to re_pattern"""
        return re.compile(self.re(T))

    def __setitem__(self, name, T):
        """adds new rx"""
        if type(T)==str:
            self.dict[name]= T
        else:
            self.dict[name]= ''.join(s for n,s in T).strip()
        setattr(self, name, self(T))


    def addfile(self, File):
        """adds rx expressions defined in File"""
        S= open(File).read()
        Token= regex.lex(S,
            pattern= 'brackets_sq brackets_curl str vardef var esc_sequence flag whitespace',
            ignore= 'comment'
        )
        #pdb.set_trace()
        Token= [t for t in Token if t.name!='whitespace']

        assert Token[0].name=='vardef'
        L=[]
        for t in Token:
            #pdb.set_trace()
            if t.name=='vardef':
                if L: self[var]= L
                var= t.str[:-1].strip()
                L=[]
            else:
                L.append(t)
        self[var]= L


        #print self.dict

    def tst(): setattr(self, 'TST______________', 'asd')


##--------------------------------------------------------------
#ReCollection for lexing rx expressions

regex= ReColl()

regex.brackets_rnd= re_pair('(',')')
regex.brackets_sq= re_pair('[',']')
regex.brackets_curl= r'(?s)'+re_pair('{','}')

regex.str_sq= re_pair("'")
regex.str_dq= re_pair('"')
regex.str_sq3= r'(?s)'+re_pair("'''") #multi-line
regex.str_dq3= r'(?s)'+re_pair('"""')
regex.str= '|'.join((regex.str_sq3,regex.str_dq3,regex.str_sq,regex.str_dq))
regex.strings= map( re.compile, (regex.str_sq3,regex.str_dq3,regex.str_sq,regex.str_dq) )

regex.float= r"\d+(\.(\d)?)?([eE][+-]?\d+)?"

##rx-parse
regex.esc_sequence= r'(?<![^\\]\\)\\[^\\]'
regex.var= r'(?<![a-zA-Z_])[a-zA-Z_][a-zA-Z_0-9]*'
regex.comment= r'#.*'
regex.whitespace= r'\s+'
regex.vardef= r'(?<!\w)'+regex.var+r'\s*=(?!=)'
regex.setdef= regex.vardef+r'\s*'+regex.brackets_curl
regex.flag= r'\(\?[a-z]+\)'

regex.update()

#pdb.set_trace()
rx= RxColl(os.path.dirname(__file__)+'\\t.rx') #RxCollection for lexing python




