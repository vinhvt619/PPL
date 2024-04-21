"""
^name : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 15/4/2024
"""

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},body={self.body})"

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
    def __str__(self):
        return f"VarZcode(type={self.typ})"

class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType
    def __str__(self):
        return f"ArrayZcode(eleType=[{', '.join(str(i) for i in self.eleType)}])"
    
class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
    
    def print(self):
        print(f"BlockFor {self.BlockFor}")
        print(f"function {str(self.function)}")
        print(f"Return {self.Return}")
        print(f"listFunction :")
        for key, value in self.listFunction.items():
            print(f"    {key}  {str(value)}")       
    
    def check(self):
        print("11")
        self.visit(self.ast, [{}])
        return None

    def LHS_RHS_stmt(self,LHS : Type, RHS : Type, ast):
        print("asm",ast, type(LHS), type(RHS))
        print(f"LHS_RHS_stmt {LHS} {RHS}")
        print("ListFunc", self.listFunction)
        #! ĐỌC TRONG DISCORD
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            print("1.")
            raise TypeCannotBeInferred(ast)
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            print("2.")
            raise TypeCannotBeInferred(ast)
        elif isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            print("3.")
            raise TypeCannotBeInferred(ast)
        elif isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            print("4.")
            self.setTypeArray(LHS, RHS)
            raise TypeMismatchInStatement(ast)
        elif isinstance(RHS, ArrayZcode):
            print("5.")
            raise TypeCannotBeInferred(ast)
        elif isinstance(LHS, Zcode):
            if RHS is not None:
                print("6.")
                LHS.typ = RHS
            elif not isinstance(RHS, VoidType): 
                print("a.b", ast)
                raise TypeCannotBeInferred(ast)
        elif isinstance(RHS, Zcode):
            if not isinstance(LHS, VoidType):
                print("7.")
                RHS.typ = LHS
            else: raise TypeCannotBeInferred(ast)
        elif not self.comparType(LHS, RHS):
            print("8.")
            print(ast, LHS, RHS)
            raise TypeMismatchInStatement(ast)
        
        if isinstance(ast, Return) and ast.expr is not None and list(self.listFunction.keys())[-1] == "main":
            print("POINT", ast.expr.value)
            raise NoEntryPoint()
        
    def LHS_RHS_expr(self, LHS : Type, RHS : Type,ast) -> bool:
        print("asttttt",ast, type(LHS), type(RHS))
        print(f"LHS_RHS_EXPR {LHS} {RHS}")
        print("ListFunc", self.listFunction)
        #! ĐỌC TRONG DISCORD
        # if isinstance(LHS, (ArrayType, ArrayLiteral, list)):
        #     if self.listFunction.get(ast.name.name):
        #         # print("18.9",len(self.listFunction[ast.name.name].param))
        #         if len(str(LHS))!= len(self.listFunction[ast.name.name].param):
        #             raise TypeMismatchInExpression(ast)
        # elif isinstance(RHS, (ArrayType, ArrayLiteral, list)):
        #     if self.listFunction.get(ast.name.name):
        #     # print("18.9",len(self.listFunction[ast.name.name].param))
        #         if len(str(RHS))!= len(self.listFunction[ast.name.name].param):
        #             raise TypeMismatchInExpression(ast)
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            print("1.1")
            return True
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            print("2.1")
            return True
        elif isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            print("3.1")
            return True
        elif isinstance(LHS, ArrayType) and isinstance(RHS, (ArrayZcode, ArrayLiteral)):
            print("4.1")
            self.setTypeArray(LHS, RHS)
            raise TypeMismatchInExpression(ast)
        elif isinstance(RHS, (ArrayZcode, ArrayLiteral, list)):
            print("5.1")
            return True
        elif isinstance(LHS, Zcode):
            print("6.1")
            LHS.typ = RHS
        elif isinstance(RHS, Zcode):
            print("7.1")
            RHS.typ = LHS
        elif not self.comparType(LHS, RHS):
            print("8.1", ast)
            raise TypeMismatchInExpression(ast)
        else: return False


    def comparType(self, LHS : Type, RHS : Type) -> bool:
        print("12", LHS, RHS)
        
        print("12.3", isinstance(LHS,(BoolType, StringType, NumberType)), isinstance(RHS,(BoolType, StringType, NumberType)))
        if isinstance(LHS, type(RHS)):
            print("12.1")
            return True
        if isinstance(LHS,(BoolType, StringType, NumberType)) and not isinstance(RHS,(BoolType, StringType, NumberType)):
            print("12.11")
            return True
        if isinstance(LHS, ArrayType) and isinstance(RHS, ArrayType):
            print("12.2")
            for i in range(len(LHS)):
                self.comparType(LHS[i], RHS[i])
        return False
    
    def setTypeArray(self, typeArray, typeArrayZcode):
        print("13")
        #* Trường hợp size khác nhau
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        
        #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu    là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
        """_VD 
            typeArray = arrayType([3], StringType), typeArrayZcode = ArrayZcode([VarZcode('a'), FuncZcode('foo'), ArrayZcode([VarZcode('b')])])
            index = 0 -> VarZcode('a').type = StringType
            index = 1 -> FuncZcode('foo').type = StringType
            index = 2 -> ArrayZcode([VarZcode('b')]) ->  fail -> return Flase
        """
        if len(typeArray.size) == 1:
            for i in len(typeArrayZcode.eleType):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                    return False
        else: 
            for i in len(typeArrayZcode.eleType):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                    self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i])

            
        #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
        """_VD 
            typeArray = arrayType([2,3], StringType), typeArrayZcode = ArrayZcode([VarZcode('a'), FuncZcode('foo'), ArrayZcode([VarZcode('b')])])
            index = 0 -> VarZcode('a').type = arrayType([3], StringType)
            index = 1 -> FuncZcode('foo').type = arrayType([3], StringType)
            index = 2 -> đệ quy typeArray = arrayType([3], StringType), typeArrayZcode = ArrayZcode([VarZcode('b')])
                vì typeArray  có 3 phần tử mà typeArrayZcode chỉ có 1 phần tử -> return false
        """

    def visitProgram(self, ast, param):
        print("14")
        for i in ast.decl: self.visit(i, param)
        # print("14.111", param, self.listFunction, self.listFunction['main'])
        
        #TODO implement dùng for duyệt qua self.listFunction nếu item[i].body == Flase thì nén ra lỗi
        for i in self.listFunction:
            # print("14.2222", self.listFunction[i].body)
            if self.listFunction[i].body == False:
                raise NoDefinition(i)

        # print("ast1", type(ast.decl[0].body), self.listFunction["main"], param)
        # for i in ast.decl[0].body:
        #     print(i, "5555")
        #TODO implement kiểm tra main có None hay không, main.param có rỗng hay không, main.typ có phải là VoidType hay không
        if self.listFunction.get("main"):
            main = self.listFunction["main"]
            if isinstance(main, FuncZcode):
                if len(main.param) != 0 or main.typ != VoidType(): #main.body == False
                    raise NoEntryPoint()
        else: raise NoEntryPoint()

        
    def visitVarDecl(self, ast, param):
        print("15")
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
        print("ast", ast, ast.varType, ast.varInit)
        print(param)
        for i in param:
            if i.get(ast.name.name):
                print("param",i[ast.name.name].typ)
        if param[0].get(ast.name.name): 
            print("15.1")
            raise Redeclared(Variable(), ast.name.name)
        
        # for i in param:
        #     if i.get(ast.name.name):
        #         a=i.get(ast.name.name)
        #         print(ast.name.name,i.get(ast.name.name), type(i[ast.name.name].typ), type(ast.varType))
        #         if isinstance(a.typ, type(ast.varType)):
        #             raise Redeclared(Variable(), ast.name.name)
                # else: print("15.14")


        param[0][ast.name.name] = VarZcode(ast.varType)
        
        if ast.varInit:
            print("15.2")
            LHS = param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
            print("15.21")
            RHS = self.visit(ast.varInit, param)
            print("15.23")
            print("varInittt",LHS, RHS, ast, param)
            self.LHS_RHS_stmt(LHS, RHS, ast)


    def visitFuncDecl(self, ast, param):
        print("16")
        print(ast, self.listFunction)
        for i in ast.param:
            print(i.varType)
        # if self.listFunction.get(ast.name.name):
        #     # for i in self.listFunction[ast.name.name]:
        #     print("typeeee",self.listFunction[ast.name.name].param, ast.param, ast.name.name)
        #     for i in ast.param:
        #         print("i",i)
        #         if len(self.listFunction[ast.name.name].param) == len(ast.param):
        #             print("length 1", len(self.listFunction[ast.name.name].param), len(ast.param))
        #         else: 
        #             print("length 2", len(self.listFunction[ast.name.name].param), len(ast.param))
        method = self.listFunction.get(ast.name.name)
        #TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared
        if self.listFunction.get(ast.name.name):
            print("16.1", ast.param)
            
            for i in ast.param:
                if len(self.listFunction[ast.name.name].param) != len(ast.param):
                    raise Redeclared(Function(), ast.name.name)
                else: 
                    # print("type2", type(i.varType), type(self.listFunction[ast.name.name].param[0]))
                    if not isinstance(i.varType, type(self.listFunction[ast.name.name].param[0])):
                        raise Redeclared(Function(), ast.name.name)
            if self.listFunction[ast.name.name].body == True :
                print("16.2")
                raise Redeclared(Function(), ast.name.name)
            else: 
                if not ast.body:
                    raise Redeclared(Function(), ast.name.name)

        #^th1: KHAI BÁO TRƯỚC 1 PHẦN KHÔNG CÓ BODY
        if not ast.body:
            print("abc2")
            typeParam = [] #! tìm ra listtype
            #TODO: implement 
            
            for i in ast.param:
                typeParam += [i.varType]
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
            return
         
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        #TODO: implement
        for i in range(len(ast.param)):
            if listParam.get(ast.param[i].name.name): 
                raise Redeclared(Parameter(), ast.param[i].name.name)
            else:
                print("16.3")
                listParam.update({ast.param[i].name.name : VarZcode(ast.param[i].varType)})
                typeParam += [ast.param[i].varType]

        if self.listFunction.get(ast.name.name):
            self.listFunction[ast.name.name].param = typeParam
        print("listParam",listParam)
        print("typeParam",typeParam)
        # param[0]
        #^TH2 khai báo 1 phần trước rồi lần này khai báo có body
        if method:
            print("16.122", method)
            print(ast, self.listFunction[ast.name.name], self.listFunction[ast.name.name].param, typeParam, listParam)
            ListLHS = self.listFunction[ast.name.name].param
            ListRHS = typeParam
            print("tessstt", ListLHS, ListRHS)
            #TODO: implement kiểm tra 2 dánh sách có giống nhau không -> Redeclared(Function(), ast.name.name) 
            print(ListLHS, ListRHS, len(ListLHS), len(ListRHS))
            if len(ListLHS) == len(ListRHS):
                print("lkjmn")
                for i in ListLHS:
                    print("i", i, type(ListRHS[0]))
                    if not i in ListRHS:
                        print("16.4")
                        raise Redeclared(Function(), ast.name.name)
            else: 
                print("16.5")
                raise Redeclared(Function(), ast.name.name)
            
            self.listFunction[ast.name.name].body = True
        else:
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
        
        self.Return = False
        self.function = self.listFunction[ast.name.name] 
        if ast.body:
            print("abc1", param)
            self.visit(ast.body, [listParam] + param)
        if not self.Return:
            if self.listFunction[ast.name.name].typ is None: 
                self.listFunction[ast.name.name].typ = VoidType()
            elif not isinstance(self.listFunction[ast.name.name].typ, VoidType):
                raise TypeMismatchInStatement(Return(None))
 
    def visitId(self, ast, param):
        print("17")
        """
            # TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
                #^ đối với giá trị trả về nếu Id.typ = None thì trả về chính nó luôn Id, nếu cso Id.typ thì trả về typ của nó
                #^ return Id.typ if Id.typ else Id (trả cơ chế reference hay con trỏ)
                #^ https://www.geeksforgeeks.org/references-in-cpp/
            Vd reference:
                def visitId() :
                    param = [{'a' : VarZcode(None)}]
                    id = param[0].get('a')
                    return Id.typ if Id.typ else Id
                
                x = visitId() # lúc này x với VarZcode(None) là như 1
                x.typ = NumberType
                -> có thể hiểu param = [{'a' : VarZcode(None)}] chuyển thành param = [{'a' : VarZcode(NumberType)}]         
        """
        print("17.7",ast, param)
        for i in param:
            print(i)
            if i.get(ast.name):
                Id = i.get(ast.name)
                print("17.3", Id)
                return Id.typ if Id.typ else Id
        raise Undeclared(Identifier(), ast.name)


    def visitCallExpr(self, ast, param):
        print("18")
        method = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        if not self.listFunction.get(ast.name.name):
            raise Undeclared(Function(), ast.name.name)
        
        # print("args", ast.args)
        #TODO: implement kiểm tra kích thước method.param và ast.args -> TypeMismatchInStatement
        if len(method.param) != len(ast.args):
            print("18.1")
            raise TypeMismatchInStatement(ast)
        # if isinstance(ast.args,(list, ArrayLiteral, ArrayType)):
        
        
        for i in range(len(method.param)):
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = method.param[i]
            RHS = ast.args[i]
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            print("callexpr", LHS, RHS, cannotBeInferred, method, method.param, ast.args[0])
            if cannotBeInferred : return CannotBeInferredZcode()

        #TODo: implement nếu method.typ là voidtype -> TypeMismatchInExpression, nếu không thì trả về theo nguyên lí giống ID trên
        if isinstance(method.typ, VoidType):
            raise TypeMismatchInExpression(ast)
        else:
            return method.typ if method.typ else method


        if self.listFunction.get(ast.name.name):
            # print("18.9",len(self.listFunction[ast.name.name].param))
            if len(str(ast.args[0].value))!= len(self.listFunction[ast.name.name].param):
                raise TypeMismatchInExpression(ast)

    def visitCallStmt(self, ast, param):
        print("19")
        method = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        if not self.listFunction.get(ast.name.name):
            raise Undeclared(Function(), ast.name.name)
        print("19.11")
        #TODO: implement kiểm tra kích thước method.param và ast.args -> TypeMismatchInStatement
        if len(method.param) != len(ast.args):
            print("19.12")
            raise TypeMismatchInStatement(ast)
        # else: 
        for i in ast.args:
            for j in method.param:
                h = self.visit(i, param)
                print("test", h, type(j))
                # if h.typ is not None:
                #     print("sucess")
                if not isinstance(h, type(j)):
                    print("19.13", ast)
                    raise TypeMismatchInStatement(ast)
            # if not j in type(method.param[0]):
            #     raise TypeMismatchInStatement(ast)
        # print("19.12", method.param, ast.args)
        for i in range(len(method.param)):
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
            print("methoddd", method, method.param)
            LHS = method.param[i]  #.typ if method.param[i].typ else method.param[i]
            RHS = ast.args
            self.LHS_RHS_stmt(LHS, RHS, ast)

        #TODO: implement nếu method.typ là None thì gán Voidtype, nếu không thì kiểm tra có phải voidtype hay không nén ra lỗi TypeMismatchInStatement
        if method.typ is None:
            method.typ = VoidType()
        elif method.typ != VoidType():
            raise TypeMismatchInStatement(ast)


    def visitIf(self, ast, param):
        print("20")
        """_typExpr_"""   
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        print(LHS, RHS, ast)
        self.LHS_RHS_stmt(LHS, RHS, ast)

        self.visit(ast.thenStmt, param)    
        
        """_elifStmt_"""   
        for item in ast.elifStmt:
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng 
            LHS = BoolType()
            RHS = self.visit(ast.expr, param)
            self.LHS_RHS_stmt(LHS, RHS, ast)
            self.visit(item[1], param)           

        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)
        
    def visitFor(self, ast, param):
        print("21")
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        """_typID_"""        
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng 
        LHS = NumberType()
        RHS = self.visit(ast.name, param)
        print("21.1")
        self.LHS_RHS_stmt(LHS, RHS, ast)        
        
        """_typCondExpr_"""    
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng  
        LHS = BoolType()
        RHS = self.visit(ast.condExpr, param)
        print("21.2")
        self.LHS_RHS_stmt(LHS, RHS, ast)      


        """_typUpdExpr_"""            
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = NumberType()
        RHS = self.visit(ast.updExpr, param)
        print("21.3")
        self.LHS_RHS_stmt(LHS, RHS, ast)      
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, param)
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    
    def visitReturn(self, ast, param):
        print("22")
        self.Return = True
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        print(self.function, self.listFunction, param)
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        self.LHS_RHS_stmt(LHS, RHS, ast)      



    def visitAssign(self, ast, param):
        print("23")
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)      
            
    def visitBinaryOp(self, ast, param):
        print("24")
        op = ast.op
        if op in ['+', '-', '*', '/', '%']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.1")
            LHS = NumberType()
            RHS = self.visit(ast.left, param)   
            print("PLUS", LHS, RHS)
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred : return CannotBeInferredZcode()

        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.2")
            LHS = NumberType()
            RHS = self.visit(ast.left, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            print("assign", LHS, RHS, cannotBeInferred)
            if cannotBeInferred : return CannotBeInferredZcode()

        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.3")
            LHS = BoolType()
            RHS = self.visit(ast.left, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred : return CannotBeInferredZcode()

        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.4")
            LHS = StringType()
            RHS = self.visit(ast.left, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred : return CannotBeInferredZcode()
        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.5")
            LHS = StringType()
            RHS = self.visit(ast.left, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()
        
        

        """_right_        
            TƯƠNG TỰ LEFT     
        """        
        if op in ['+', '-', '*', '/', '%']:            
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.6")
            
            LHS = NumberType()
            RHS = self.visit(ast.right, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()
            #TODO: implement trả về type
            return NumberType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.7")
            
            LHS = NumberType()
            RHS = self.visit(ast.right, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()

            #TODO: implement trả về type
            return NumberType()

        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.8")
            LHS = BoolType()
            RHS = self.visit(ast.right, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()

            #TODO: implement trả về type
            return BoolType()

        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            
            print("24.9")
            LHS = StringType()
            RHS = self.visit(ast.right, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()
            #TODO: implement trả về type
            return StringType()

        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            print("24.10")
            
            LHS = StringType()
            RHS = self.visit(ast.right, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()
            #TODO: implement trả về type
            return StringType()

    def visitUnaryOp(self, ast, param):
        print("25")
        op = ast.op
        if op in ['+', '-']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            RHS = self.visit(ast.operand, param)
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()

            #TODO: implement trả về type
            return NumberType()

        if op in ['not']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = BoolType()
            RHS = self.visit(ast.operand, param)
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

            if cannotBeInferred : return CannotBeInferredZcode()
            #TODO: implement trả về type
            return BoolType()

    def visitArrayCell(self, ast, param):
        print("26")
        arr = self.visit(ast.arr, param)
        print("arrr",self.visit(ast.arr, param))
        if isinstance(arr, (BoolType, StringType, NumberType)):
            print("26.1")
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            print("26.2", arr)
            return CannotBeInferredZcode()

        for item in ast.idx:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            RHS = item
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred : return CannotBeInferredZcode()

            
        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType)   

    # def visitArrayLiteral(self, ast, param, mainTyp = None):
        # mainTyp = None
        # for item in ast.value:
        #     checkTyp = self.visit(item, param)
        #     if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
        #         mainTyp = checkTyp
        #     elif isinstance(checkTyp, CannotBeInferredZcode):
        #         return CannotBeInferredZcode()
        
        # if mainTyp is None: 
        #     return ArrayZcode([self.visit(item, param) for item in ast.value], ast)
            
            
        # for item in ast.value:
        #     LHS = NumberType()
        #     RHS = self.visit(item, param)
        #     cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)

        #     if cannotBeInferred : return CannotBeInferredZcode()


        # if self.listFunction.get("main"):
        #     if self.listFunction["main"].typ in [BoolType(), StringType(), NumberType()]:
        #         return ArrayType([ast.value], mainTyp)
        #     elif self.listFunction["main"].typ == ArrayType():
        #         return ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)
        

        
        # return self.visitArrayLiteral(ast, param)
    def visitArrayLiteral(self, ast, param, mainTyp = None):
        
        if mainTyp is not None:
            result = mainTyp
            mainTyp = mainTyp.eleType if len(mainTyp.size) == 1 else ArrayType(mainTyp.size[1:], mainTyp.eleType) 
            
            
            for item in ast.value:
                RHS = self.visit(item, param)   
                print(f"xxx {RHS} {mainTyp}")
                if isinstance(RHS,CannotBeInferredZcode) or isinstance(mainTyp,CannotBeInferredZcode):
                    return CannotBeInferredZcode()
                if isinstance(mainTyp,ArrayType) and isinstance(RHS,ArrayZcode):
                    mainTyp = self.visitArrayLiteral(RHS.ast, param, mainTyp)
                elif isinstance(RHS, ArrayZcode):
                    return CannotBeInferredZcode()
                elif isinstance(RHS, Zcode):
                    RHS.typ = mainTyp
            
            return self.visitArrayLiteral(ast, param)

    """phần này sẽ là cố định do ngắn quá :(( """
    def visitBlock(self, ast, param):
        print("28")
        paramNew = [{}] + param #! tăng tầm vực
        for item in ast.stmt: 
            self.visit(item,paramNew)   
    def visitContinue(self, ast, param):
        print("29")
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        print("30")
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()

        
        





