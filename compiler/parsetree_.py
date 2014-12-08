#Generator Varlist Mod_list Var Val_label__is__expr Val Stmt Ternary__is__expr Block_head Trycatch Gen_expr Aug_assign Id_alias Assign_stmt While Op_cmp Pos_arglist Exprlist Int Arglist Funccall__is__expr Comparison__is__expr For Stmts Except Blockbegin Bit_xor__is__expr Pos_arg Vartuple String Aug_op Dictitem Dictlist Id_list Kparamlist Func Dict_gen Class Unary__is__expr Pos_paramlist Block_stmt Block Import_stmt Exponentiation__is__expr Kparam Loop_stmt Dash_calc__is__expr Str_val Del_stmt Karglist Ifelse Single_stmt Prog Import Lambda_label__is__expr Func_stmt Tuple Bit_and__is__expr Loop Blockend Paramlist Global_stmt Assign Or__is__expr Lambda Pos_paramtuple Elif Set Print_stmt Number Assert_stmt Mod_alias Raise_stmt Str_prefix Slice Pass_stmt Brackets__is__expr Dict Shift__is__expr Rel_module Bit_or__is__expr Else Dot_calc__is__expr With Iter_gen And__is__expr Not__is__expr List Alias Exec_stmt Simple_var Attr__is__expr Index__is__expr Set_gen Float Module Id Karg If Alias_list List_gen
import pandas as pd;
import numpy as np;
import pdb;
import re;
from copy import deepcopy;
import cPickle as pickle;
import collections;

from pylex.rx import rx, RxColl;
rx['other']= '.';
rx['simple_space']= '\s+';
rx['optvar']= "var '?'?";

##-----------------------------------------------------------
##Basic Data-Structure

class NamedList(pd.Series):$blockbegin
    """Ordered Key-Value List""";
    def add(self, k, v, rename=True):$blockbegin
        """appends new entry and numbers duplicate names""";
        nr='';
        if not rename:$blockbegin
            #pdb.set_trace()
            S= self.append(pd.Series([v],[k]));
            self.__init__( S );
        $blockend
        else:$blockbegin
            if k[-1].isdigit():$blockbegin #for insert
                k = re.match(r'(.+?)\d*$', k).groups()[0];
            $blockend #strip number

            rep= sum( 1 for x in self.keys() if re.match(re.escape(k)+r'\d*$', x) );
            if rep:$blockbegin
                if rep==1:$blockbegin
                    self.rename({k:k+'1'}, inplace=True);
                $blockend
                    #self.rename(lambda x: x+'1' if x==k else x, inplace=True)
                nr= str(rep+1);
            $blockend
            self[k+nr]= v;
        $blockend
        return nr;
    $blockend

    def insert(self, S, i, rename= False):$blockbegin
        """inserts new entry(s) before index/name i""";
        if type(S)!=pd.Series:$blockbegin #2-tuple
            S= pd.Series([S[1]], [S[0]]);
        $blockend
            #S= pd.Series(*zip(*S))
        if type(i)==str:$blockbegin
            i= np.where(self.keys()==i)[0][0];
        $blockend

        if not rename:$blockbegin
            self.__init__(self[:i].append(S).append(self[i:]));
        $blockend
        else:$blockbegin
            head= NamedList(self[:i].copy());
            tail= S.append(self[i:]);
            for x in tail.iteritems():$blockbegin
                head.add(*x);
            $blockend
            self.__init__(head);
        $blockend
    $blockend

    def append(self, x, verify_integrity=False):$blockbegin
        if type(x)==dict:$blockbegin
            x= pd.Series(x);
        $blockend
        return super(NamedList, self).append(x, verify_integrity);
    $blockend
$blockend


##-----------------------------------------------------------
##Tree Classes

class vertex(NamedList):$blockbegin

    isa_VL= [];

    def __init__(self, name= None, parent= None, space='', #name=''?
                 data=None, index=None, dtype= object, #dtype?
                 Name=None, copy=False, fastpath=False):$blockbegin
        #name->Name

        if type(name)!=str:$blockbegin
            #print 'S ',
            super(vertex, self).__init__(name, index, dtype, Name, copy, fastpath);
            return;
        $blockend

        super(vertex, self).__init__(data, index, dtype, Name, copy, fastpath);

        self.parent= parent;
        if name and name[-1].isdigit():$blockbegin #??
            self.name, self.nr = re.match(r'(.+?)(\d*)$', name).groups();
        $blockend
        else:$blockbegin
            self.name= name;
            self.nr= None;
        $blockend
        self.space= space;
    $blockend

        #self.isa_VL= []

    def __eq__(self, S):$blockbegin
        return S==self.name;
    $blockend
    def __nonzero__(self):$blockbegin
        return bool(self.name);
    $blockend

    def rename(self, old, new=None, inplace=True):$blockbegin
        """changes (unique) keyname in children of vertex""";
        if new is None:$blockbegin
            old, new= old.items()[0];
        $blockend
        self.__init__(super(vertex, self).rename({old:new}));
        self[new].nr= re.match(r'(.+?)(\d*)$', new).groups()[1];
    $blockend

    def idx(self):$blockbegin # -> nr unnoetig
        for i,v in enumerate(self.parent):$blockbegin
            if self is v:$blockbegin
                return i;
            $blockend
        $blockend
    $blockend

    def up(self, n=1):$blockbegin
        if n==0:$blockbegin
            return self;
        $blockend
        return self.parent.up(n-1);
    $blockend

    def walk(self):$blockbegin
        """iterates over all vertices""";
        yield self;
        """
        brk= yield self
        if brk:
            print '   BRK'
            exc
        """;
        for v in self:$blockbegin
            for w in v.walk():$blockbegin
                yield w;
            $blockend
        $blockend
    $blockend


    def dfind(self, S):$blockbegin
        D= collections.defaultdict(str);
        self._dfind(S, D);
        return D;
    $blockend
    def _dfind(self, S, D):$blockbegin
        for v in self:$blockbegin
            if v==S:$blockbegin
                D[S+str(len(D)+1)]= v;
            $blockend
            else:$blockbegin
                v._dfind(S, D);
            $blockend
        $blockend
    $blockend


    def find(self, S, nmax=0):$blockbegin
        L= [];
        self._find(S, L);
        #L.extend(['']*(nmax-len(L)))
        L.extend(vertex() for i in range(nmax-len(L)));
        return L;
    $blockend
    def _find(self, S, L):$blockbegin
        for v in self:$blockbegin
            if v==S:$blockbegin
                L.append(v);
            $blockend
            else:$blockbegin
                v._find(S, L);
            $blockend
        $blockend
    $blockend

    def is1(self, S):$blockbegin
        if self.name==S:$blockbegin
            return self;
        $blockend
        elif self.empty or len(self)>1:$blockbegin
            return False;
        $blockend
        else:$blockbegin
            return self[0].is1(S);
        $blockend
    $blockend

    def isa(self, S):$blockbegin
        """
        Tests if vertex consists of the vertices specified in the string pattern "S".
        If this is the case the vertices are returned, otherwise False

        Consists means here, that the vertices are reached at some point if you go
        down from the starting vertex and that they all together share the same leafes
        as the starting vertex.

        Rules for string pattern:
        -Variables, Integers and Strings are interpreted as vertex names
        -For Strings double quotes (like in C++) have to be used
        -Whitespace can be used as seperator
        -All unknown characters between known tokens are also interpreted
         as vertex names

        For example:
        "Id(Expr+Int)"
        is seperated in the 6 tokens
        'Id', '(', 'Expr', '+', 'Int' ')'

        "x+=-7(a b)"
        is seperated in the 7 tokens
        'x', '+=-', '7', '(', 'a', 'b', ')'

        """;
        TL= rx.lex(S, 'var simple_space int str any');
        TL= [t.str for t in TL if not t=='simple_space'];

        if len(TL)==1:$blockbegin
            vertex.isa_VL= self.is1(TL[0]);
            return vertex.isa_VL;
        $blockend

        vertex.isa_VL=[];  #Vertex-List
        PD= collections.deque(TL);  #Pattern-Deque
        #pdb.set_trace()

        if not self._isa(PD, vertex.isa_VL) or PD:$blockbegin
            return [];
        $blockend

        #pdb.set_trace()
        return vertex.isa_VL;
    $blockend
    def _isa(self, PD, VL):$blockbegin
        if self.name==PD[0]:$blockbegin
            #pdb.set_trace()
            PD.popleft();
            VL.append(self);
            return True;
        $blockend

        elif self.empty:$blockbegin
            return False;
        $blockend

        restlen= len(self);
        for v in self:$blockbegin
            if restlen>len(PD) or not v._isa(PD, VL):$blockbegin
                return False;
            $blockend
            restlen-=1;
        $blockend

        return True;
    $blockend

    def literals(self):$blockbegin
        """returns a list of the translated text in the leafs""";
        return [v.name for v in self.walk() if v.empty];
    $blockend
    def words(self):$blockbegin #tauschen!
        """returns a list of the literal text in the leafs""";
        L=[];
        temp= Tree.out;
        Tree.out= L;
        self.visitchildren();
        Tree.out= temp;
        """
        temp= Tree.write
        Tree.write= lambda Tree,x: L.append(x)
        self.visitchildren()
        Tree.write= temp
        """;
        return L;
    $blockend
    def text(self):$blockbegin
        """returns a string of the translated text in the leafs""";
        return ''.join(self.words()).rstrip();
    $blockend
    def ot(self):$blockbegin #for debugging
        """returns original text in the leafs""";
        return ''.join(v.name+v.space for v in self.walk() if v.empty);
    $blockend

    def transform(self, S, D=()):$blockbegin
        """
        Transforms the text in the momentary vertex and subvertices
        according to the syntax specified in string "S".
        The dictionary "D" can be used to pass in additional variables

        Rules for string pattern:
        -Variables are interpreted as vertex names and the text in these
         vertices is inserted
         + Variables are looked up in the dictionary "D" or in the
           momentary vertex
         + if a Variable is followed by "?" it can also not exist in
           "D" or the momentary vertex, otherwise it has to exist
        -Strings are interpreted as new text which is inserted literally
        -Whitespace is also insterted literally and thus significant
        - "~" can be used to seperate two tokens without inserting space
        - every unknown character between known tokens is also inserted
          literally

        I.e. a theoretical vertex which consists out of the direct child vertices
          Id = Expr1 * Expr2
        Could be transformed by the String pattern
          "Id(Expr1, Expr2, '13')"

        """;

        TL= rx.lex(S, 'optvar str simple_space other');
        for t in TL:$blockbegin
            s= t.str;

            #rules
            if t=='optvar':$blockbegin
                #pdb.set_trace()
                opt= 0;
                if s.endswith('?'):$blockbegin
                    opt= 1;
                    s= s[:-1];
                $blockend

                if s in D:$blockbegin
                    v= D[s];
                    if type(v)==str and v:$blockbegin
                        Tree.write(v);
                        continue;
                    $blockend
                $blockend
                else:$blockbegin
                    v= self.get(s, '');
                $blockend

                if v=='':$blockbegin
                    if opt:$blockbegin
                        continue;
                    $blockend
                    raise Exception('\n\tNo rule "%s" in vertex "%s"'%(s,self.name));
                $blockend
                v.visit();
                Tree.rstrip();
            $blockend
            #literals
            elif t=='str':$blockbegin
                s= s.strip(s[0]);
                Tree.write(s);
            $blockend
            #delimiter
            elif s=='~':$blockbegin
                continue;
            $blockend
            #other
            else:$blockbegin
                Tree.write(s);
            $blockend
        $blockend
    $blockend

    def visitchildren(self):$blockbegin
        for v in self:$blockbegin
            v.visit();
        $blockend
    $blockend

    def visit(self):$blockbegin

        if self.name in Tree.actions:$blockbegin
            Tree.actions[self.name](self);
        $blockend
        #Leaf
        elif self.empty:$blockbegin
            Tree.write(self.name+self.space);
        $blockend

        else:$blockbegin
            self.visitchildren();
        $blockend
    $blockend

    def startvisit(self):$blockbegin
        #pdb.set_trace()
        Tree.TL=[]; #Problem mit static/global!
        Tree.out= Tree.TL;
        self.visit();
    $blockend
$blockend




class Tree(object):$blockbegin
    actions= {};
    includes= {'iostream'}; #vorgeben??
    TL= []; #List for translated text
    #out= TL

    def __init__(self, S=None):$blockbegin
        self.root= vertex('root');
        self.pos= self.root;

        self.patterns= set();

        Tree.out= Tree.TL;
    $blockend

    def __iter__(self):$blockbegin
        return self.pos.walk();
    $blockend

    @classmethod;
    def write(cls, S):$blockbegin
        cls.out.append(S);
    $blockend
    @classmethod;
    def writeto(cls, L=None):$blockbegin #besser??
        cls.out= cls.TL if L is None else L;
    $blockend
    @staticmethod;
    def rstrip():$blockbegin
        Tree.out[-1]= Tree.out[-1].strip();
    $blockend


    def add(self, k, rename=True):$blockbegin
        nr= self.pos.add(k, vertex(k, self.pos));
        self.pos= self.pos[k+nr];
        self.pos.nr= nr;
    $blockend

    def up(self, n=1):$blockbegin
        self.pos= self.pos.up(n);
    $blockend

    def words(self):$blockbegin
        """starting at pos, returns a list of the translated text in the leafs""";
        return self.pos.words();
    $blockend


    def visit(self):$blockbegin
        #pdb.set_trace()
        Tree.TL=[];
        Tree.out= Tree.TL;
        self.pos.visit();
    $blockend

    def tofile(self, File):$blockbegin
        self.visit();
        setup= """\nusing namespace std;\n\n""";

        with open(File, 'wb') as F:$blockbegin
            F.write(''.join( '#include <%s>\n'%i for i in sorted(Tree.includes) ));
            F.write(setup);
            F.write(''.join(Tree.TL));
        $blockend
    $blockend
$blockend




##-----------------------------------------------------------
##Tree/Visitor Actions

def tree_action(L):$blockbegin
    def wrapper(func):$blockbegin
        M=L; #nonlocal
        if type(M)==str:$blockbegin
            M= M.split();
        $blockend

        for x in M:$blockbegin
            tree_action.dict[x]= func;
        $blockend
    $blockend
    return wrapper;
$blockend
tree_action.dict= Tree.actions;


@tree_action('If');
def f(vtx):$blockbegin
    vtx.transform("'if' (Expr)");
$blockend
@tree_action('Elif');
def f(vtx):$blockbegin
    vtx.transform("'else if' (Expr)");
$blockend

@tree_action('Blockbegin');
def f(vtx):$blockbegin
    Tree.write(' {'+vtx[0].space);
$blockend

@tree_action('Blockend');
def f(vtx):$blockbegin
    Tree.write('}'+vtx[0].space);
$blockend

@tree_action('For');
def f(vtx):$blockbegin
    #print 'For'
    EL= vtx.Exprlist;
    var= vtx.Varlist.words();
    assert len(var)==1;
    var= ''.join(var).strip();

    #for-each
    if EL.literals()[0]!='range':$blockbegin
        vtx.transform("'for' ('auto' var : Exprlist)", locals());
    $blockend

    #for-range
    else:$blockbegin
        #pdb.set_trace()
        start,stop,step = EL.Expr.Funccall.Arglist.find('Expr', 3);#[v.text().strip()
                           #for v in EL.Expr.Funccall.Arglist.find('Expr', 3)]
        if not stop:$blockbegin
            start,stop = stop,start;
        $blockend
        stop= stop.text();
        start= start.text();
        start= 'int '+var+'= '+ (start or '0');

        comp= '<';
        if step:$blockbegin

            if step.isa('-Int'):$blockbegin
                comp= '>';
            $blockend
            elif step.is1('Int'):$blockbegin
                comp= '<';
            $blockend
            else:$blockbegin
                sign= 'copysign(1.,%s)'%step.text();
                comp= ' *{0}<{0}* '.format(sign);
            $blockend

            step= var+'+='+step.text();
        $blockend
        else:$blockbegin
            step= var+'++';
        $blockend
        stop= var+comp+stop;

        vtx.transform("'for' (start; stop; step)", locals());
    $blockend
$blockend



@tree_action('Pass_stmt');
def f(vtx):$blockbegin
    pass;
$blockend

@tree_action('Print_stmt');
def f(vtx):$blockbegin
    if 'Exprlist' in vtx:$blockbegin
        EL= vtx.Exprlist.find('Expr');
        exprlist= '<< '+ " <<' '<< ".join(e.text() for e in EL);
        Tree.write('cout%s << endl'%exprlist);
    $blockend
    else:$blockbegin
        Tree.write('cout<< endl');
    $blockend
$blockend


@tree_action('Exponentiation');
def f(vtx):$blockbegin
    vtx.transform("'pow'(Expr1, Expr2)");
    Tree.includes.add('cmath');
$blockend

@tree_action('Dot_calc');
def f(vtx):$blockbegin
    op= vtx[1].name;
    if op=='/':$blockbegin
        vtx.transform("Expr1 /('double') Expr2");
    $blockend #pruefen ob int!!
    else:$blockbegin
        vtx.visitchildren();
    $blockend
$blockend

@tree_action('Funccall');
def f(vtx):$blockbegin
    if vtx.isa('len(Expr)'):$blockbegin
        expr= vtx.isa_VL[2];
        vtx.transform("expr.'size'()", locals());
    $blockend
    else:$blockbegin
        vtx.visitchildren();
    $blockend
$blockend


@tree_action('Single_stmt');
def f(vtx):$blockbegin

    #Multiline-Comment
    if vtx.isa('String ;'):$blockbegin
        #pdb.set_trace()
        s,sc = vtx.isa_VL;
        #if s[0]=='Str_prefix':
         #   raise Exception("Unsupported string prefix in "+s.text())
        s= s.Str_val[0].name;
        s= s.strip(s[0]);
        Tree.write(r'/*%s*/%s'%(s, sc.space));
    $blockend
    #Imports
    elif vtx.isa('Import_stmt ;'):$blockbegin
        pass;
    $blockend
    else:$blockbegin
        vtx.visitchildren();
    $blockend
$blockend


@tree_action('Assign');
def f(vtx):$blockbegin
    VL= vtx.Varlist;
    Id= VL.is1('Id');
    EL= vtx.Exprlist;
    if EL.isa('[Expr] * Int') :$blockbegin #check for var decalaration!!
        #pdb.set_trace()
        assert not Id==False;
        _,Expr,_,_,Int= vtx.isa_VL;

        if Expr.isa('0'):$blockbegin
            vtx.transform("'array'<'double',Int> Id={}", locals());
        $blockend
        else:$blockbegin
            #pdb.set_trace()
            vtx.transform("'array'<'double',Int> Id; Id.'fill'(Expr)", locals());
        $blockend

        Tree.includes.add('array');
    $blockend
    else:$blockbegin
        vtx.visitchildren();
    $blockend
$blockend


@tree_action('Aug_assign');
def f(vtx):$blockbegin
    #op= vtx.Aug_op[0].name
    #if op=='+=':
    if vtx.isa('Var+=1'):$blockbegin
        vtx.transform('Var++');
    $blockend #immer??
    else:$blockbegin
        vtx.visitchildren();
    $blockend
$blockend


@tree_action('Func');
def f(vtx):$blockbegin
    PPL= vtx.find('Pos_paramtuple'); #Positional Parameter List
    KPL= vtx.find('Kparam');         #Keyword Parameter List

    paramlist= [];

    for p in PPL:$blockbegin
        paramlist.append('double '+p.text());
    $blockend
    for p in KPL:$blockbegin
        paramlist.append('double '+p.text());
    $blockend

    paramlist= ', '.join(paramlist);

    vtx.transform("'double' Id(paramlist)", locals());
$blockend


@tree_action('Ifelse');
def f(vtx):$blockbegin

    #main function
    if vtx.If.isa('if __name__ == "__main__"'):$blockbegin
        Tree.write(
"""\
int main() {

    %s

    return 0;

}
"""%vtx.Block.Prog.text()
);
    $blockend

    else:$blockbegin
        vtx.visitchildren();
    $blockend
$blockend
