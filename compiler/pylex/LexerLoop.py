
from math import *
import string
import re
from collections import namedtuple
import pdb, traceback
import sys

from common import *
from rx import regex



__all__= ['lex']

def lex(prog):

    OPERATORS= r"""
    +       -       *       **      /       //      %
    <<      >>      &       |       ^       ~
    <       >       <=      >=      ==      !=      <>

    (       )       [       ]       {       }      @
    ,       :       .       `       =       ;
    +=      -=      *=      /=      //=     %=
    &=      |=      ^=      >>=     <<=     **=
    """



    ##Lexical meaning of characters:
    letters_l= set(string.ascii_lowercase)
    letters_u= set(string.ascii_uppercase)
    letters= letters_l | letters_u
    letters_= letters | {'_'}
    digits= set('0123456789')
    var= letters_ | digits

    whitespace= set(' \t\n\\') #\\?

    operators= set('=+-*/<>%&|^~!')
    operators2= set(re.findall(r'\S\S', OPERATORS))
    operators3= set(re.findall(r'\S\S\S', OPERATORS))
    op_undefined= set('?$')
    op_unary= set('+-~')
    op_binary= operators - op_unary
    delimiters= set('()[]{}@,:.`;')
    quotes= {'#', "'", '"', "'''", '"""'}
    strprefix= {'r', 'u', 'ur', 'R', 'U', 'UR', 'Ur',
                'uR', 'b', 'B', 'br', 'Br', 'bR', 'BR'}


    ##--------------------------------------------------------
    ##Lexing
    pyfile= open(prog)
    S= pyfile.read().replace('\r\n', '\n') + '$' #EOF

    CompilerError.file= pyfile.name
    CompilerError.phase= 'Lexer'

    # ##EOF
    # c= S[-1]
    # if c in op_undefined:
    #     raise CompilerError('Undefined Operator', S, -1, c)
    # else:
    #     S+= '$'


    i=0
    Words= []
    while i<len(S)-1:
        #pdb.set_trace()
        c= S[i]
        w= c
        i+= 1
        #Variable
        if c in letters_:
            while S[i] in var:
                w+= S[i]
                i+=1
            wtype= 'var'
        #Whitespace
        elif c in whitespace:
            while S[i] in whitespace:
                w+= S[i]
                i+=1
            wtype= 'whitespace'
        #Delimiters
        elif c in delimiters:
            wtype= 'delimiter'


        #Operator
        elif c in operators:
            if w+S[i] in operators2:
                w+= S[i]; i+=1
                if w+S[i] in operators3:
                    w+= S[i]; i+=1
                elif S[i] in op_binary:
                    raise CompilerError('Unknown operator', S,i,w+S[i])
            wtype= 'operator'
        #Strings, Comments
        elif c in quotes:
            if c=='#':
                lend= S.index('\n', i)
                w+= S[i:lend]
                i=lend
                wtype= 'comment'
                #pdb.set_trace()
            else:
                for r in regex.strings:
                    m= r.match(S[i-1:])
                    if m:
                        w= m.group()
                        i+= len(w)-1
                        break
                if len(w)==1:
                    raise CompilerError('Unpaired quote ', S,i-1,w)
                wtype= 'str'
        #Numbers
        elif c in digits:
            while S[i] in digits:
                w+= S[i]; i+=1
            if S[i] in '.e':
                m= regex.float.match(w+S[i:])
                if m:
                    w= m.group()
                    i+= len(w)-1
                    wtype= 'float'
                    if S[i] in '.e':
                        raise CompilerError('Incorrect number-format', S,i,w+S[i])
                else:
                    raise CompilerError('Incorrect number-format', S,i,w)
            else:
                wtype= 'int'
        ##Undefined Operators
        elif c in op_undefined:
            raise CompilerError('Undefined Operator', S, i-1, w)
        else:
            #raise CompilerError("Unknown character ", S,i,w)
            print "Unknown character "+c
            wtype= '  !!unknown!!'
        Words.append( token(wtype,w) )

if __name__ == '__main__':
    display(Words)
