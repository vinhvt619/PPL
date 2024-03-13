from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    
    # Visit a parse tree produced by ZCodeParser#program.
    # program: NEWLINE* list_declared EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # Visit a parse tree produced by ZCodeParser#list_declared.
    # list_declared:  declared list_declared | declared;
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declared())]
        return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())

    # Visit a parse tree produced by ZCodeParser#declared.
    # declared: function | variables ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.function():
            return self.visit(ctx.function())
        return self.visit(ctx.variables())


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.keyword_var() is None and ctx.implicit_dynamic() is None:
            return self.visit(ctx.implicit_var())
        if ctx.implicit_var() is None and ctx.implicit_dynamic() is None:
            return self.visit(ctx.keyword_var())
        return self.visit(ctx.implicit_dynamic())


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "var", self.visit(ctx.expression()))

    # Visit a parse tree produced by ZCodeParser#keyword_var.
    #keyword_var: type1 IDENTIFIER ('['list_number']')?  (ARROW expression)?;
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        expr = None
        if ctx.expression(): expr = self.visit(ctx.expression())
        
        type2 = self.visit(ctx.type1())
        if ctx.list_number():
            type2 = ArrayType(self.visit(ctx.list_number()), type2)
        return VarDecl(Id(ctx.IDENTIFIER().getText()),type2, None, expr)


    def visitType1(self, ctx:ZCodeParser.Type1Context):
        if ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        return StringType()

    # Visit a parse tree produced by ZCodeParser#list_number.
    #list_number: NUMBER_LIT ',' list_number | NUMBER_LIT;
    def visitList_number(self, ctx:ZCodeParser.List_numberContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBER_LIT().getText())]
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.list_number())


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.expression() is None:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "dynamic", None)
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "dynamic", self.visit(ctx.expression()))


    # Visit a parse tree produced by ZCodeParser#function.
    #function: FUNC IDENTIFIER '(' prameters_list? ')'  (ignore? return_statement | ignore? block_statement | ignore);
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        if ctx.prameters_list():
            if ctx.return_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.prameters_list()), self.visit(ctx.return_statement()))
            elif ctx.block_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.prameters_list()), self.visit(ctx.block_statement()))
            else:
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.prameters_list()),())
        else:
            if ctx.return_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()),[], self.visit(ctx.return_statement()))
            elif ctx.block_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()),[], self.visit(ctx.block_statement()))
            else:
                return FuncDecl(Id(ctx.IDENTIFIER().getText()),[],())


    # Visit a parse tree produced by ZCodeParser#prameters_list.
    def visitPrameters_list(self, ctx:ZCodeParser.Prameters_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.pram())]
        return [self.visit(ctx.pram())] + self.visit(ctx.prameters_list())


    # Visit a parse tree produced by ZCodeParser#pram.
    def visitPram(self, ctx:ZCodeParser.PramContext):
        type2 = self.visit(ctx.type1())
        if ctx.list_number():
            type2 = ArrayType(self.visit(ctx.list_number()), type2)
        return VarDecl(Id(ctx.IDENTIFIER().getText()), type2, None, None)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1()[0])

        op = ctx.CONCAT().getText()
        left = self.visit(ctx.expression1()[0])
        right = self.visit(ctx.expression1()[1])
        return BinaryOp(op, left, right)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2()[0])
        op = ''
        if ctx.LESS():
            op = ctx.LESS().getText()
        elif ctx.GREATER():
            op = ctx.GREATER().getText()
        elif ctx.LE():
            op = ctx.LE().getText()
        elif ctx.GE():
            op = ctx.GE().getText()
        elif ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.EE():
            op = ctx.EE().getText()
        elif ctx.DIFF():
            op = ctx.DIFF().getText()        
        left = self.visit(ctx.expression2()[0])
        right = self.visit(ctx.expression2()[1])
        return BinaryOp(op, left, right)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op, left, right)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.MINUS():
            op = ctx.MINUS().getText()
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)



    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        op = ''
        if ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(op, left, right)



    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        op = ctx.NOT().getText()
        right = self.visit(ctx.expression5())
        return UnaryOp(op, right)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        op = ctx.MINUS().getText()
        right = self.visit(ctx.expression6())
        return UnaryOp(op, right)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expression()[0]))
        elif len(ctx.list_expression()) == 2:
            return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expression()[0])), self.visit(ctx.list_expression()[1]))
        return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), []), self.visit(ctx.list_expression()[0]))


    # Visit a parse tree produced by ZCodeParser#expression8.
    #expression8: IDENTIFIER ('(' (list_expression)? ')') | '(' list_expression? ')' | literal;
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        if ctx.IDENTIFIER():
            if ctx.list_expression():
                return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expression()))
            return CallExpr(Id(ctx.IDENTIFIER().getText()),[])
        elif ctx.expression():
            return self.visit(ctx.expression())
        else: 
            return self.visit(ctx.literal())

    # Visit a parse tree produced by ZCodeParser#list_expression.
    def visitList_expression(self, ctx:ZCodeParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
        return [self.visit(ctx.expression())]


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        else: return Id(ctx.IDENTIFIER().getText())


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):\
        return ArrayLiteral(self.visit(ctx.list_expression()))


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.declaration_statement():
            return self.visit(ctx.declaration_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        return self.visit(ctx.block_statement())


    # Visit a parse tree produced by ZCodeParser#declaration_statement.
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visit(ctx.variables())


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    #assignment_statement: IDENTIFIER ('['list_expression']')? ARROW expression ignore;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        if ctx.list_expression():
            return Assign(ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expression())), self.visit(ctx.expression()))
        return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression()))


    # Visit a parse tree produced by ZCodeParser#if_statement.
    #if_statement: 'if' expression ignore? statement elif_loop? else_statement? ; 
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        # else_loop1 = None
        # if ctx.elif_loop():
        #     else_loop1 = self.visit(ctx.elif_loop())
        # else_state = None
        # if ctx.else_statement():
        #     else_state = self.visit(ctx.else_statement())
        # return If(self.visit(ctx.expression()), self.visit(ctx.statement()), else_loop1, else_state)


        if ctx.else_statement():
            return If(self.visit(ctx.expression()), self.visit(ctx.statement()),self.visit(ctx.elif_loop()), self.visit(ctx.else_statement()))
        return If(self.visit(ctx.expression()), self.visit(ctx.statement()),self.visit(ctx.elif_loop()), None)


    # Visit a parse tree produced by ZCodeParser#elif_statement.
    #elif_statement: 'elif' expression ignore? statement;
    def visitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        return [self.visit(ctx.expression()), self.visit(ctx.statement())]


    # Visit a parse tree produced by ZCodeParser#elif_loop.
    #elif_loop: elif_statement elif_loop | elif_statement;
    def visitElif_loop(self, ctx:ZCodeParser.Elif_loopContext):
        if ctx.elif_statement():
            return [self.visit(ctx.elif_statement())] + self.visit(ctx.elif_loop())
        return []


    # Visit a parse tree produced by ZCodeParser#else_statement.
    def visitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        return self.visit(ctx.statement())


    # Visit a parse tree produced by ZCodeParser#for_statement.
    #for_statement: 'for' IDENTIFIER 'until' expression 'by' expression ignore? statement;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expression()[0]), self.visit(ctx.expression()[1]), self.visit(ctx.statement()))


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return()


    # Visit a parse tree produced by ZCodeParser#call_statement.
    #call_statement: IDENTIFIER '(' (list_expression)? ')' ignore;
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        if ctx.list_expression():
            return CallStmt(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.list_expression()))
        return CallStmt(Id(ctx.IDENTIFIER().getText()),[])

    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        if ctx.list_statement():
            return Block(self.visit(ctx.list_statement()))
        return Block([])


    # Visit a parse tree produced by ZCodeParser#list_statement.
    def visitList_statement(self, ctx:ZCodeParser.List_statementContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None