grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
program: NEWLINE* list_declared EOF;
list_declared:  declared list_declared |  declared;
declared: function | variables ignore;



variables: implicit_var | keyword_var | implicit_dynamic; 
implicit_var: VAR IDENTIFIER ARROW ( expression | array_literal);
keyword_var: (BOOL | STRING | NUMBER) IDENTIFIER ('['list_number']')?  (ARROW expression)?;
list_number: NUMBER_LIT ',' list_number | NUMBER_LIT;
number_string: (NUMBER_LIT | STRING_LIT) ',' list_number | (NUMBER_LIT | STRING_LIT);
implicit_dynamic: DYNAMIC IDENTIFIER (ARROW expression)?;




function: FUNC IDENTIFIER '(' prameters_list? ')'  (ignore? return_statement | ignore? block_statement | ignore);
prameters_list: pram ',' prameters_list | pram;
pram: ((BOOL | STRING | NUMBER) IDENTIFIER ('['list_number']')?);




exp_prime: expression exp_prime | expression;
expression: expression0;
expression0: expression1 CONCAT expression1 | expression1;
expression1: expression2 (LESS | GREATER | LE | GE | EQUAL | EE | DIFF) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | MINUS) expression4 | expression4;
expression4: expression4 (DIV | MUL | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: MINUS expression6 | expression7;
expression7: (IDENTIFIER | IDENTIFIER ('(' (list_array)? ')')) '[' list_expression ']'| expression8;
expression8: IDENTIFIER ('(' (list_array)? ')') | '(' list_array? ')' | literal;


list_array: (array_literal | list_expression) CM list_array | (array_literal | list_expression);

list_expression: expression CM list_expression | expression;

literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal | IDENTIFIER;
array_literal: '[' (list_expression)? ']';


statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;



declaration_statement: variables ignore;
assignment_statement: IDENTIFIER array_literal? ('=' NUMBER_LIT)? ARROW expression ignore;


if_statement: 'if' expression ignore? statement elif_loop? else_statement? ; 
elif_statement: 'elif' expression ignore? statement;
elif_loop: elif_statement elif_loop | elif_statement;
else_statement: 'else' ignore? statement;
 


for_statement: 'for' IDENTIFIER 'until' expression 'by' expression ignore? statement;

break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;
return_statement: RETURN (expression)? ignore;

call_statement: IDENTIFIER '(' (list_array)? ')' ignore;

block_statement: BEGIN ignore? list_statement?  END ignore;
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


STRING_LIT: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"')* '"' {self.text = self.text[1:-1];};
fragment DIGIT: [0-9];
fragment EXP: ('e' | 'E') ('+' | '-')?[0-9]+;
NUMBER_LIT: DIGIT+ ('.'?[0-9]*)? EXP?;

NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r]* -> skip; // Comments
WS : [ \t\r\f\b]+ -> skip ; // skip spaces, tabs
INT: '0' | [1-9][0-9]*;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"')* ('\r\n' | '\n' | 'EOF')?
{
    if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
    };
ILLEGAL_ESCAPE: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"')*([\r\\] | '\\' ~[bfrnt\\] | '\'' ~["])
{
    raise IllegalEscape(self.text[1:])
};
