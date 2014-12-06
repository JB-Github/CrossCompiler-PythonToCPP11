
from math import *;
#import programm
import string;
import re;
from collections import namedtuple;
import pdb, traceback;
import sys;



##allgemein
def display(I):$blockbegin
    """prints elements of Iterable on seperate lines""";
    t= type(I);
    if t==dict:$blockbegin
        for kv in I.items():$blockbegin
            print '%s\t%s'%kv;
        $blockend
    $blockend
    else:$blockbegin
        for x in I:$blockbegin
            print x;
        $blockend
    $blockend
$blockend
def file2set(File):$blockbegin
    with open(File) as F:$blockbegin
        return set(x for x in F.read().split() if x[0]!='#');
    $blockend
$blockend

def showpos(S,i):$blockbegin
    lstart=S.rindex('\n', 0,i)+1;
    lend= S.index('\n', i);
    line= S[lstart:lend];
    lnr= S[:i].count('\n')+1;
    cnr= i-lstart; # 0-Indexing of columns
    pointer= ' '*(cnr-1)+'^';
    print line;
    print pointer;
$blockend

class CompilerError(Exception):$blockbegin
    file= '';
    phase='';
    def __init__(self, message, S,i,w):$blockbegin

        pdb.set_trace();
        lstart=S.rindex('\n', 0,i)+1;
        lend= S.index('\n', i);
        line= S[lstart:lend];
        lnr= S[:i].count('\n')+1;
        cnr= i-lstart; # 0-Indexing of columns
        pointer= ' '*(cnr-1)+'^';


        message= """
 {self.phase}, File "{self.file}", line {lnr}, col {cnr}

  {line}
  {pointer}
  ERR: {message} "{w}" """.format( **locals() );
        Exception.__init__(self, message);
    $blockend
$blockend

token= namedtuple('token', ('name', 'str'));
token.__repr__= lambda t: t.name.ljust(8)+'\t'+repr(t.str);
token.__eq__= lambda t, s: t.name==s;

##-----------------------------------------------------------

def lex(S, re='', re_ignore=''):$blockbegin
    Tokens= [];
    t= type(re);
    if t==str:$blockbegin
        re= [(n,regex[n]) for n in S.split()];
    $blockend
$blockend

##-----------------------------------------------------------

##regular expressions
re_pattern= type(re.compile(''));

def re_pair(start,end=None):$blockbegin# unescaped=True
    if end is None:$blockbegin
        end=start;
    $blockend
    return r'(?<![^\\]\\)\%s.*?(?<![^\\]\\)\%s'%(start, end);
$blockend


class ReColl(object):$blockbegin
    """Collector for re expressions""";
    #__metaclass__= RE_COLLECTOR # => type(regex)==RE_COLLECTOR
    def __init__(self, File=None):$blockbegin
        self.dict= {};
    $blockend

    def __call__(self, string):$blockbegin
        """translate string to re_pattern""";
        return re.compile(string);
    $blockend

    def __setitem__(self, name, re_str):$blockbegin
        """adds new regex""";
        self.dict[name]= re_str;
        setattr(self, name, self(re_str));
    $blockend
    def __getitem__(self, name):$blockbegin
        """returns regex string""";
        #return self.dict[name]
        return self.__dict__[name];
    $blockend
    def __iter__(self):$blockbegin
        return (
            (n,r) for n,r in self.__dict__.items()
            if not n.startswith('__') and type(r)==re_pattern
        );
    $blockend

    def update(self):$blockbegin
        """adds new string attributes as regular expressions""";
        #Save re name and string
        self.dict.update({
            n:s for n,s in self.__dict__.items()
            if not n.startswith('__') and type(s)==str
        });
        #Compile regular expressions
        for n,s in self.dict.items():$blockbegin
            setattr(self, n, self(s));
        $blockend
    $blockend

    def lex(self, S, pattern=None, ignore=[]):$blockbegin
        """lexes String with given grammar""";
        Tokens= [];

        PL= [];
        if pattern==None:$blockbegin
            PL= list(self);
        $blockend
        for p in pattern, ignore:$blockbegin
            t= type(p);
            if t==str:$blockbegin
                PL.extend((n,self[n]) for n in p.split());
                if p==ignore:$blockbegin
                    ignore= ignore.split();
                $blockend
            $blockend
        $blockend
        i=0;
        while i<len(S):$blockbegin
            #pdb.set_trace()
            m= None;
            for name, pat in PL:$blockbegin
                m= pat.match(S[i:]);
                if m:$blockbegin
                    w= m.group();
                    #print w
                    i+= len(w);
                    if name not in ignore:$blockbegin
                        Tokens.append(token(name, w));
                        print Tokens[-1];
                    $blockend
                    break;
                $blockend
            $blockend
            if not m:$blockbegin
                print 'Unknown character "%s"'%S[i];
                Tokens.append(token('Unknown char', S[i]));
                i+=1;
            $blockend
        $blockend

        return Tokens;
    $blockend
$blockend


class RxColl(ReColl):$blockbegin
    """Collector for rx expressions""";
    def __init__(self, File=None):$blockbegin
        self.dict= {};
        if File: self.addfile(File);
    $blockend

    def re(self, T):$blockbegin
        """translate rx string to re string""";
        print '----------------------rx----------------------', T;
        if not T:$blockbegin
            return T;
        $blockend
        if type(T)==str:$blockbegin
            T= regex.lex(T,
                pattern= 'brackets_sq brackets_curl str var esc_sequence flag',
                ignore= 'comment whitespace'
            );
        $blockend
        #elif type(X[0])==token
        #pdb.set_trace()
        #assert type(T[0])==token

        for i,(n,s) in enumerate(T):$blockbegin
            if n=='str':$blockbegin
                s= re.escape(s[1:-1]);
            $blockend
            elif n=='whitespace':  continue;
            elif n=='brackets_curl':$blockbegin
                #s= re.sub(r'[^\w\s]', '', s) #Sonderzeichen?
                s= s.strip()[1:-1];
                s= '('+ '|'.join( map(re.escape, s.split()) ) +')';
            $blockend
            elif n=='var':$blockbegin
                s= '('+ self.re(self.dict[s]) +')';
            $blockend

            if n!='str':$blockbegin
                s= s.strip();
            $blockend
            T[i]= token(n, s);
        $blockend


        return ''.join(s for n,s in T);
    $blockend #strip()?? #re.compile(string)

    def __call__(self, T):$blockbegin
        """translate string to re_pattern""";
        return re.compile(self.re(T));
    $blockend

    def __setitem__(self, name, T):$blockbegin
        """adds new rx""";
        if type(T)==str:$blockbegin
            self.dict[name]= T;
        $blockend
        else:$blockbegin
            self.dict[name]= ''.join(s for n,s in T).strip();
        $blockend
        setattr(self, name, self(T));
    $blockend


    def addfile(self, File):$blockbegin
        """adds rx expressions defined in File""";
        S= open(File).read();
        Token= regex.lex(S,
            pattern= 'brackets_sq brackets_curl str vardef var esc_sequence flag whitespace',
            ignore= 'comment'
        );
        #pdb.set_trace()
        Token= [t for t in Token if t.name!='whitespace'];
        while Token[0].name=='whitespace':$blockbegin
            Token.pop(0);
        $blockend
        assert Token[0].name=='vardef';
        L=[];
        for t in Token:$blockbegin
            #pdb.set_trace()
            if t.name=='vardef':$blockbegin
                if L: self[var]= L;
                var= t.str[:-1].strip();
                L=[];
            $blockend
            else:$blockbegin
                L.append(t);
            $blockend
        $blockend
        self[var]= L;


        print self.dict;
    $blockend

    def tst(): setattr(self, 'TST______________', 'asd');
$blockend




regex= ReColl();

regex.brackets_rnd= re_pair('(',')');
regex.brackets_sq= re_pair('[',']');
regex.brackets_curl= r'(?s)'+re_pair('{','}');

regex.str_sq= re_pair("'");
regex.str_dq= re_pair('"');
regex.str_sq3= r'(?s)'+re_pair("'''"); #multi-line
regex.str_dq3= r'(?s)'+re_pair('"""');
regex.str= '|'.join((regex.str_sq3,regex.str_dq3,regex.str_sq,regex.str_dq));
regex.strings= map( re.compile, (regex.str_sq3,regex.str_dq3,regex.str_sq,regex.str_dq) );

regex.float= r"\d+(\.(\d)?)?([eE][+-]?\d+)?";

##rx-parse
regex.esc_sequence= r'(?<![^\\]\\)\\[^\\]';
regex.var= r'(?<![a-zA-Z_])[a-zA-Z_][a-zA-Z_0-9]*';
regex.comment= r'#.*';
regex.whitespace= r'\s+';
regex.vardef= r'(?<!\w)'+regex.var+r'\s*=(?!=)';
regex.setdef= regex.vardef+r'\s*'+regex.brackets_curl;
regex.flag= r'\(\?[a-z]+\)';

regex.update();

rx= RxColl('t.re');

##--------------------------------------------------------------


OPERATORS= r"""
+       -       *       **      /       //      %
<<      >>      &       |       ^       ~
<       >       <=      >=      ==      !=      <>

(       )       [       ]       {       }      @
,       :       .       `       =       ;
+=      -=      *=      /=      //=     %=
&=      |=      ^=      >>=     <<=     **=
""";



##Lexical meaning of characters:
letters_l= set(string.ascii_lowercase);
letters_u= set(string.ascii_uppercase);
letters= letters_l | letters_u;
letters_= letters | {'_'};
digits= set('0123456789');
var= letters_ | digits;

whitespace= set(' \t\n\\'); #\\?

operators= set('=+-*/<>%&|^~!');
operators2= set(re.findall(r'\S\S', OPERATORS));
operators3= set(re.findall(r'\S\S\S', OPERATORS));
op_undefined= set('?$');
op_unary= set('+-~');
op_binary= operators - op_unary;
delimiters= set('()[]{}@,:.`;');
quotes= {'#', "'", '"', "'''", '"""'};
strprefix= {'r', 'u', 'ur', 'R', 'U', 'UR', 'Ur',
            'uR', 'b', 'B', 'br', 'Br', 'bR', 'BR'};


##--------------------------------------------------------
pyfile= open('programm.py');
S= pyfile.read();#+'\r' #EOF

CompilerError.file= pyfile.name;
CompilerError.phase= 'Lexer';

##EOF
c= S[-1];
if c in op_undefined:$blockbegin
    raise CompilerError('Undefined Operator', S, -1, c);
$blockend
else:$blockbegin
    S+= '$';
$blockend


i=0;
Words= [];
while i<len(S)-1:$blockbegin
    #pdb.set_trace()
    c= S[i];
    w= c;
    i+= 1;
    #Variable
    if c in letters_:$blockbegin
        while S[i] in var:$blockbegin
            w+= S[i];
            i+=1;
        $blockend
        wtype= 'var';
    $blockend
    #Whitespace
    elif c in whitespace:$blockbegin
        while S[i] in whitespace:$blockbegin
            w+= S[i];
            i+=1;
        $blockend
        wtype= 'whitespace';
    $blockend
    #Delimiters
    elif c in delimiters:$blockbegin
        wtype= 'delimiter';
    $blockend


    #Operator
    elif c in operators:$blockbegin
        if w+S[i] in operators2:$blockbegin
            w+= S[i]; i+=1;
            if w+S[i] in operators3:$blockbegin
                w+= S[i]; i+=1;
            $blockend
            elif S[i] in op_binary:$blockbegin
                raise CompilerError('Unknown operator', S,i,w);
            $blockend
        $blockend
        wtype= 'operator';
    $blockend
    #Strings, Comments
    elif c in quotes:$blockbegin
        if c=='#':$blockbegin
            lend= S.index('\n', i);
            w+= S[i:lend];
            i=lend;
            wtype= 'comment';
        $blockend
            #pdb.set_trace()
        else:$blockbegin
            for r in regex.strings:$blockbegin
                m= r.match(S[i-1:]);
                if m:$blockbegin
                    w= m.group();
                    i+= len(w)-1;
                    break;
                $blockend
            $blockend
            if len(w)==1:$blockbegin
                r;
            $blockend
            wtype= 'str';
        $blockend
    $blockend
    #Numbers
    elif c in digits:$blockbegin
        while S[i] in digits:$blockbegin
            w+= S[i]; i+=1;
        $blockend
        if S[i] in '.e':$blockbegin
            m= regex.float.match(w+S[i:]);
            if m:$blockbegin
                w= m.group();
                i+= len(w)-1;
                wtype= 'float';
                if S[i] in '.e':$blockbegin
                    raise CompilerError('Incorrect number-format', S,i,w+S[i]);
                $blockend
            $blockend
            else:$blockbegin
                raise CompilerError('Incorrect number-format', S,i,w);
            $blockend
        $blockend
        else:$blockbegin
            wtype= 'int';
        $blockend
    $blockend
    ##Undefined Operators
    elif c in op_undefined:$blockbegin
        raise CompilerError('Undefined Operator', S, i, w);
    $blockend
    else:$blockbegin
        #raise CompilerError("Unknown character ", S,i,w)
        print "Unknown character "+c;
        wtype= '  !!unknown!!';
    $blockend
    Words.append( token(wtype,w) );
$blockend

    #i+= 1

#printL(Words)
"""
TL= regex.lex(open('t.re').read(),
            pattern= 'brackets_sq brackets_curl str vardef var esc_sequence flag',
            ignore= 'whitespace comment'
)
""";
TL= rx.lex(S, pattern= 'str keyword var float int space operator op_unused', ignore= 'comment');
display(TL);

