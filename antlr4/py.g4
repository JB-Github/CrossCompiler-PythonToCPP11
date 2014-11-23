grammar py;

////Parser////
////-------------------------------------------------------------

prog : stmt+ ;

stmt : single_stmt | block_stmt ;

single_stmt
	: ( assign_stmt | exprlist | stmts) ';' //empty statement
;
stmts
	: 'pass'
	| 'del' varlist
	| 'print' ( exprlist? | '>>'exprlist )

	//errors
	| 'assert' exprlist
	| 'raise' (expr (',' expr)? (',' expr)?)?

	//loop
	| 'break'
	| 'continue'

	//function
	| 'return' exprlist?
	| 'yield' exprlist?

	//declarations
	| import_
	| 'global' var (',' var)*

	| 'exec' expr ('in' expr (',' expr)?)?
;

//import
import_
	: 'import' mod_list
	| 'from' rel_module 'import' id_list
	| 'from' module 'import' '*'
;

id_list : id_alias (',' id_alias)? ;
id_alias : id_var ('as' id_var)? ;

mod_list : mod_alias (',' mod_alias)? ;
mod_alias : module ('as' id_var)? ;
module : id_var ('.' id_var)* ;
rel_module : '.'* module | '.'+ ;

////-------------------------------------------------------------

block_stmt : block_head block | ifelse | trycatch ;//| func_block ;
block_head :  loop | func | class_ | with_ ;

loop: (while_ | for_) (else_ block)? ;
while_ : 'while' expr ;
for_ : 'for' varlist 'in' exprlist ;

with_ : 'with' alias_list ;
alias_list : alias (',' alias)* ;
alias : expr ('as' var)? ;

ifelse : if_ block (elif_ block)* (else_ block)? ;
if_ : 'if' expr ;
elif_ : 'elif' expr ;
else_ : 'else' ;

block
	: blockbegin prog blockend
	| ':' single_stmt
;


class_ : 'class' id_var ('(' exprlist? ')')? ;//exprlist??

trycatch
	: 'try' block (except_ block)+ (else_ block)? ('finally' block)?
	| 'try' block 'finally' block
;
except_ : 'except' expr (','|'as') var ; //pruefen!!

//func_block : func BlockBegin func_stmt+ BlockEnd ;
//func_stmt : stmt | 'return' expr ';' ;


////-------------------------------------------------------------

assign : varlist '=' exprlist ;
assign_stmt
	: assign
	| aug_assign
;

aug_assign : var aug_op exprlist ;
aug_op : '+=' | '-=' | '*=' | '/=' | '//=' | '%=' | '**=' | '>>=' | '<<=' | '&=' | '^=' | '|=' ;


varlist : vartuple (',' vartuple)* ','? ;
vartuple
	: var
	| '(' vartuple (',' vartuple)* ')'
;
exprlist : expr (',' expr)* ','? ;

////-------------------------------------------------------------

expr
	//Brackets
	: expr '(' (arglist | gen_expr)? ')' //#funccall //Semantics!!
	| expr ('[' slice_ ']')	//#index
	| '(' expr ')'

	| expr '.' expr 		//#attr

	| ('+'|'-'|'~') expr	//#unary

	//Arithmetic
	| <assoc=right> expr '**' expr
	| expr '%' expr
	| expr '//' expr //Reihenfolge?!
	| expr '/' expr
	| expr '*' expr
	| expr '-' expr
	| expr '+' expr

	//Bits
	| expr ('<<'|'>>') expr //#shift
	| expr '&' expr
	| expr '^' expr
	| expr '|' expr

	| expr (op_cmp expr)+ 	//#comparison

	//Booleans
	| 'not' expr
	| expr 'and' expr
	| expr 'or' expr

	| val // zuerst??


	//| generator
	| lambda_

	| <assoc=right> expr if_ else_ expr	//#ternary ////funktioniert nicht in Kombination mit generator!!
;

lambda_ : 'lambda' arglist? ':' expr ;

generator: list_gen | dict_gen | iter_gen | set_gen ;
list_gen : '[' gen_expr ']' ;
iter_gen : '(' gen_expr ')' ;
set_gen :  '{' gen_expr '}' ;
dict_gen : '{' expr ':' gen_expr '}' ;
gen_expr : expr (for_ if_?)+ ;

////-------------------------------------------------------------

val :  var | number | string | generator | list_ | tuple_ | dict_ | set_  ; //Reihenfolge beachten!!

op_cmp : 'in' | 'not' 'in' | 'is' | 'is' 'not' | '<' | '<=' | '>' | '>=' | '<>' | '!=' | '==' ;

slice_
	: expr (':' expr?)? (':' expr?)?
	| expr? (':' expr?)? ':' expr
	| ':' ':'?
;//unschoen!!

list_ : '[' exprlist? ']' ;
tuple_ : '(' expr',' exprlist? ')' ; //Trailing Comma??
set_ : '{' exprlist '}' ;


dict_ : '{' dictlist? '}' ;
dictlist : dictitem (',' dictitem )* ','?;
dictitem : expr ':' expr ;


////-------------------------------------------------------------
////Function

//Function Defintion
func : 'def' id_var '(' paramlist? ')';
paramlist
	: pos_paramlist (',' kparamlist)?  (',' '*'simple_var)? (',' '**'simple_var)?
	| kparamlist (',' '*'simple_var)? (',' '**'simple_var)?
	| '*'simple_var (',' '**'simple_var)?
	| '**'simple_var
; //unschoen!!

pos_paramlist : pos_paramtuple (',' pos_paramtuple)* ;
pos_paramtuple
	: simple_var
	| '(' pos_paramtuple (',' pos_paramtuple)* ')'
;
kparamlist : kparam (',' kparam)* ;
kparam : pos_paramtuple '=' expr; //only Python2

//Function Call
//funccall : simple_var '(' arglist? ')' ;
arglist
	: pos_arglist (',' karglist)?
	| karglist
;
pos_arglist : pos_arg (',' pos_arg)* ;
pos_arg : ('*'|'**')? expr ;
karglist : karg (',' karg)* ;
karg : simple_var '=' expr;


////-------------------------------------------------------------

var
	: Var
	| '(' var ')' //immer???
	| var '.' var
	| var '[' slice_ ']'
;
simple_var
	: Var
	| '(' simple_var ')'
;
id_var : Var ;

number : int_ | float_ ;
int_ : Int ;
float_ : Float ;
string : Str;

blockbegin : BlockBegin ;
blockend : BlockEnd ;

////-------------------------------------------------------------
////Lexer////

BlockBegin : ':$blockbegin' ;// ':' mitnehmen?
BlockEnd : '$blockend' ;

Keyword : 'and' | 'del' | 'from' | 'not' | 'while' | 'as' | 'elif' | 'global' | 'or'
		| 'with' | 'assert' | 'else' | 'if' | 'pass' | 'yield' | 'break' | 'except'
		| 'import' | 'print' | 'class' | 'exec' | 'in' | 'raise' | 'continue'
		| 'finally' | 'is' | 'return' | 'def' | 'for' | 'lambda' | 'try';


Operator : '=' | '>='| '>>'| '*='| '<>'| '<<'| '<='| '%='| '//='| '!='| '%'| '^='| '<<='
		 | '&'| ')'| '('| '+'| '*'| '-'| '|'| '/'| '.'| '>>='| ';'| ':'| '='| '<'| '>'
		 | '@'| '**='| '=='| '|='| '&='| '**'| '['| ']'| '^'| '//'| '`'| '/='
		 | '-='| '{'| '}'| '|'| '+='| '~' ;


Var : Letter_ (Letter_|Digit)*;
Int : Digit+;
Float :  Digit+ Exp | Digit+ Decimal Exp? | Decimal Exp?;

Comment : '#' ~[\n]* -> channel(HIDDEN);//skip;
Space : ( '\t' | '\n' | '\r' | '\\' | ' ' )+ -> channel(HIDDEN);//skip;

Str : Prefix? '\'\'\'' ('\\'.|~[\\])*? '\'\'\''
    | Prefix? '"""' ('\\'.|~[\\])*? '"""'
    | Prefix? '\'' ('\\'.|~[\\\n])*? '\''
    | Prefix? '"' ('\\'.|~[\\\n])*? '"'
;


fragment Letter : [a-zA-Z];
fragment Letter_ : Letter|'_';
fragment Digit : [0-9];

fragment Exp : [eE][+-]? Int;
fragment Decimal : '.' Digit*;

fragment Prefix : 'r' | 'u' | 'ur' | 'R' | 'U' | 'UR' | 'Ur' | 'uR' | 'b' | 'B' | 'br' | 'Br' | 'bR' | 'BR';


/*abc
	: ('b' {_input.LA(1).equals('c')}? {System.out.println("1111111111111111");}
	| 'a'|'c')+
;
*/