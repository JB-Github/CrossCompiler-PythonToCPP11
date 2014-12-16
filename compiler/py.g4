grammar py;

////Parser////
////-------------------------------------------------------------

prog : stmt+ ;

stmt : single_stmt | block_stmt ;

single_stmt
	: ( assign_stmt | exprlist | stmts) ';' //empty statement
;
stmts
	: 'pass' 			#pass_stmt
	| 'del' varlist 	#del_stmt
	| 'print' ( exprlist? | '>>'exprlist ) #print_stmt

	//errors
	| 'assert' expr (',' expr)?					#assert_stmt
	| 'raise' (expr (',' expr)? (',' expr)?)? 	#raise_stmt

	//loop
	| 'break' 		#loop_stmt
	| 'continue'	#loop_stmt

	//function
	| 'return' exprlist?	#func_stmt
	| 'yield' exprlist?		#func_stmt

	//declarations
	| import_ 					#import_stmt
	| 'global' var (',' var)*	#global_stmt

	| 'exec' expr ('in' expr (',' expr)?)? 	#exec_stmt
;


//import
import_
	: 'import' mod_list
	| 'from' rel_module 'import' id_list
	| 'from' module 'import' '*'
;

id_list : id_alias (',' id_alias)? ;
id_alias : id_ ('as' id_)? ;

mod_list : mod_alias (',' mod_alias)? ;
mod_alias : module ('as' id_)? ;
module : id_ ('.' id_)* ;
rel_module : '.'* module | '.'+ ;

////-------------------------------------------------------------

block_stmt : block_head block | ifelse | trycatch ;//| func_block ;
block_head : decorator* (func | class_) | loop | with_ ;

decorator : '@' id_ '(' (arglist | gen_expr) ')'? ';' ;  //methods!!

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


class_ : 'class' id_ ('(' exprlist? ')')? ;//exprlist??

trycatch
	: 'try' block (except_ block)+ (else_ block)? ('finally' block)?
	| 'try' block 'finally' block
;
except_ : 'except' expr (','|'as') var ; //pruefen!!



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
	: expr '(' (arglist | gen_expr)? ')' 	#funccall__is__expr //Semantics!!
	| expr '[' slice_ ']'					#index__is__expr  	//Reihenfolge!!
	| '(' expr? ')' 						#brackets__is__expr

	| expr '.' id_ 	#attr__is__expr

	| ('+'|'-'|'~') expr	#unary__is__expr

	//Arithmetic
	| <assoc=right> expr '**' expr 	#exponentiation__is__expr
	| expr ('%'|'//'|'/'|'*') expr 	#dot_calc__is__expr
	| expr ('-'|'+') expr 			#dash_calc__is__expr

	//Bits
	| expr ('<<'|'>>') expr #shift__is__expr
	| expr '&' expr 		#bit_and__is__expr
	| expr '^' expr 		#bit_xor__is__expr
	| expr '|' expr 		#bit_or__is__expr

	| expr (op_cmp expr)+ 	#comparison__is__expr

	//Booleans
	| 'not' expr 		#not__is__expr
	| expr 'and' expr 	#and__is__expr
	| expr 'or' expr 	#or__is__expr

	| val 	#val__label__is__expr

	| lambda_ 	#lambda__label__is__expr

	| <assoc=right> expr if_ else_ expr		#ternary__is__expr
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
func : 'def' id_ '(' paramlist? ')';
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
	: id_
	| '(' var ')' //immer??
	| var '.' id_
	| var '[' slice_ ']'
;
simple_var
	: id_
	| '(' simple_var ')'
;
id_ : Var ;

number : int_ | float_ ;
int_ : Int ;
float_ : Float ;

string : str_prefix? str_val;
str_prefix : 'r' | 'u' | 'ur' | 'R' | 'U' | 'UR' | 'Ur' | 'uR' | 'b' | 'B' | 'br' | 'Br' | 'bR' | 'BR' ;
str_val : Str ;

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


Operator : '=' | '>=' | '>>' | '*=' | '<>' | '<<' | '<=' | '%=' | '//=' | '!=' | '%' | '^=' | '<<='
		 | '&' | ')' | '(' | '+' | '*' | '-' | ' |' | '/' | '.' | '>>=' | ';' | ':' | '=' | '<' | '>'
		 | '@' | '**=' | '==' | ' |=' | '&=' | '**' | '[' | ']' | '^' | '//' | '`' | '/='
		 | '-=' | '{' | '}' | ' |' | '+=' | '~' ;


Var : Letter_ (Letter_|Digit)*;
Int : Digit+;
Float :  Digit+ Exp | Digit* Decimal Exp? ;

Comment : '#' ~[\n]* -> channel(HIDDEN);
Space : ( '\t' | '\n' | '\r' | '\\' | ' ' )+ -> channel(HIDDEN);

Str : '\'\'\'' ('\\'.|~[\\])*? '\'\'\''
    | '"""' ('\\'.|~[\\])*? '"""'
    | '\'' ('\\'.|~[\\\n])*? '\''
    | '"' ('\\'.|~[\\\n])*? '"'
;
//Prefix : 'r' | 'u' | 'ur' | 'R' | 'U' | 'UR' | 'Ur' | 'uR' | 'b' | 'B' | 'br' | 'Br' | 'bR' | 'BR';


fragment Letter : [a-zA-Z];
fragment Letter_ : Letter|'_';
fragment Digit : [0-9];

fragment Exp : [eE][+-]? Int;
fragment Decimal : '.' Digit*;

