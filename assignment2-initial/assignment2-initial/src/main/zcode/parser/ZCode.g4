grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
program: NEWLINE* list_declared EOF;
list_declared:  declared list_declared | declared;
declared: function | variables ignore;



variables: implicit_var | keyword_var | implicit_dynamic; 
implicit_var: VAR IDENTIFIER ARROW expression;
keyword_var: type1 IDENTIFIER ('['list_number']')?  (ARROW expression)?;
list_number: NUMBER_LIT ',' list_number | NUMBER_LIT;
implicit_dynamic: DYNAMIC IDENTIFIER (ARROW expression)?;

type1: (BOOL | STRING | NUMBER);


function: FUNC IDENTIFIER '(' prameters_list? ')'  (ignore? return_statement | ignore? block_statement | ignore);
prameters_list: pram ',' prameters_list | pram;
pram: type1 IDENTIFIER ('['list_number']')?;



expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (LESS | GREATER | LE | GE | EQUAL | EE | DIFF) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | MINUS) expression4 | expression4;
expression4: expression4 (DIV | MUL | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: MINUS expression6 | expression7;
expression7: (IDENTIFIER | IDENTIFIER ('(' (list_expression)? ')')) '[' list_expression ']'| expression8;
expression8: IDENTIFIER ('(' (list_expression)? ')') | '(' list_expression? ')' | literal;


list_expression: expression CM list_expression | expression;

literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal | IDENTIFIER;
array_literal: '[' (list_expression)? ']';


statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;



declaration_statement: variables ignore;
assignment_statement: IDENTIFIER ('['list_expression']')? ARROW expression ignore;


if_statement: 'if' expression ignore? statement elif_loop? else_statement? ; 
elif_statement: 'elif' expression ignore? statement;
elif_loop: elif_statement elif_loop | elif_statement;
else_statement: 'else' ignore? statement;
 


for_statement: 'for' IDENTIFIER 'until' expression 'by' expression ignore? statement;

break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;
return_statement: RETURN (expression)? ignore;

call_statement: IDENTIFIER '(' (list_expression)? ')' ignore;

block_statement: BEGIN ignore list_statement?  END ignore;
list_statement: statement list_statement | statement;



            
ignore: NEWLINE+;

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND:'and';
OR: 'or';

ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
ARROW: '<-';
DIFF: '!=';
LESS: '<';
LE: '<=';
GREATER: '>';
GE: '>=';
EE: '==';
CONCAT: '...';

LB:'(';
RB:')';
LP:'[';
RP:']';
CM:',';
CL: ':';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;


STRING_LIT: '"' (~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\'"')* '"' {self.text = self.text[1:-1];};
fragment DIGIT: [0-9];
fragment EXP: ('e' | 'E') ('+' | '-')?[0-9]+;
NUMBER_LIT: DIGIT+ ('.'?[0-9]*)? EXP?;

NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS : [ \t\r]+ -> skip ; // skip spaces, tabs
INT: '0' | [1-9][0-9]*;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\r\n\f\\'"] | '\\' [bfrnt'\\] | ['] ["])* ('\r\n' | '\n' | 'EOF')?
{
    if self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
    };
ILLEGAL_ESCAPE: '"' (~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\\\'"')*([\r\f\\] | '\\' ~[bfrnt\\] | '\'' ~["])
{
    raise IllegalEscape(self.text[1:])
};
