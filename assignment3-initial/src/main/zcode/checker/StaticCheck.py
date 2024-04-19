from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

"""
    * Type gồm
        * GROUP 1 : NumberType, BoolType, StringType, ArrayType : gồm size, eleType (NumberType, BoolType, StringType)
        * GROUP 2 : ArrayZcode : eleType chỉ bao gồm các type kiểu Zcode và ArrayZcode, typ chưa được suy diễn
            ! eleType kiểu Zcode và ArrayZcode -> eleType = ArrayZcode([VarZcode(), FuncZcode(), ArrayZcode([VarZcode(), FuncZcode()])])
        * GROUP 3 : Zcode : typ chưa được suy diễn cần xác định khi lần dùng đầu tiên
            *  FuncZcode : kiểu typ của hàm chưa suy diễn or có thể đã được suy diễn gồm
                ^ param : danh sách các biến cần truyền vào hàm được biểu diễn dưới dạng danh sách kiêu
                ^ typ : kiểu type của hàm hiện tại nếu typ là None thì hàm này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
                ^ body : xem thử hàm khai báo trước 1 phần (nghĩa là không có body) hay không
            * VarZcode : kiểu typ của biến chưa được suy diễn or có thể đã được suy diễn
                ^ typ : kiểu type của hàm hiện tại nếu typ là None thì biến này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
"""

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    #* param : list[Type]
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang FuncZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (FuncZcode)
    #* body : Bool nếu là true nghĩa là body đã có (khai báo toàn bộ có body hàm), nếu False nghĩa là khai báo 1 phần (khai báo không có body)
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body
        

class VarZcode(Zcode):
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang varZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (VarZcode)    
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    #* eleType: List[Type]
    #* Type ở đây có thể là Zcode, ArrayZcode
    def __init__(self, eleType):
        self.eleType = eleType


class StaticChecker(BaseVisitor, Utils):
    #* ast : cây ở BTL2
    #* BlockFor : int, kiểm tra xem chúng ta đang ở trong vòng for thứ mấy
    #* function: FuncZcode, kiểm tra hàm hiện tại chúng ta đang vào body của nó checkStatic
    #* listFunction : Dict<string, FuncZcode>, Danh sách các hàm, ban đầu sẽ mặc định các hàm read, write file
    #* return : Bool, kiểm tra hàm hiện tại có return hay không nếu không có thì xác đinh hàm này là VoidType
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
        
               
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    """_comparType_
        #* LHS và RHS chỉ có thể là Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS đều là array
            #^ xét kích thước size có giống nha không nếu không giống nhau trả Flase
            #^ xét từng phần tử trong size của 2 thằng nếu không giống nhau trả Flase
            #^ xét tiếp eleType nếu không giống nhau trả Flase
        #* TH2 nếu cả 2 không phải array -> so sánh type của 2 nó thôi      
    """  
    
    def check(self):
        self.visit(self.ast, [{}])
        return None
    

    """_comparType_
        #* LHS và RHS chỉ có thể là Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS đều là array
            #^ xét kích thước size có giống nha không nếu không giống nhau trả Flase
            #^ xét từng phần tử trong size của 2 thằng nếu không giống nhau trả Flase
            #^ xét tiếp eleType nếu không giống nhau trả Flase
        #* TH2 nếu cả 2 không phải array -> so sánh type của 2 nó thôi      
    """
    def comparType(self, LHS, RHS):
        #! so sánh 2 type có trùm nhau hay không
        #! so sánh nếu 2 type đều là array -> kiểm tra từng phần tử trong size có giống hay không về kích thước và giá trị bên trong
        #! nếu giống thì trả true, ngược lại false


        # if type(LHS) == type(RHS) and type(LHS) != arr.array:
        #     return True
        # elif type(LHS) == type(RHS) and type(LHS) == arr.array:
        #     if len(LHS)!= len(RHS):
        #         return False
        #     else:
        #         for i in len(LHS):
        #             if type(LHS[i]) != type(RHS[i]):
        #                 return False
        #         return True
        # return False
    

        if LHS == RHS:
            if LHS == ArrayType():
                if len(LHS)!= len(RHS):
                    return False
                else:
                    for i in len(LHS):
                        if LHS[i] != RHS[i]:
                            return False
                    if LHS.eleType != RHS.eleType:
                        return False
                    return True
            else:
                return True
        return False

        
    """_comparListType
        #* LHS và RHS chỉ có thể list các type sau Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS khác kích thước -> Flase
        #* duyệt từng phần tử gọi self.comparType(LHS[i], RHS[i])
    """    
    def comparListType(self, listLHS, listRHS):
        #! so sánh 2 list type gọi hàm comparType xử lí
        if len(listLHS)!=len(listRHS):
            return False
        for i in len(listLHS):
            if self.comparType(listLHS[i], listRHS[i]) == False:
                return False
        return True
    
    def setTypeArray(self, typeArray, typeArrayZcode):
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
            for i in len(typeArrayZcode):
                if typeArrayZcode.eleType[i] == Zcode:
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                elif typeArrayZcode.eleType[i] == ArrayZcode:
                    return False
        else:
            for i in len(typeArrayZcode):
                if typeArrayZcode.eleType[i] == Zcode:
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif typeArrayZcode.eleType[i] == ArrayZcode:
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
        
        #! duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        #! sau bước này param có dạng [{biến toàn cục, hàm}]


        # raise NoDefinition(ast)
        #         print("12", j)
        #         print("11", h)
                    
        
        """
        
            TODO check No definition for a function in self.listFunction
            ^ gợi ý: duyệt tìm trong self.listFunction có FuncZcode nào có body = false hay không
            ví dụ 1 -> đúng
            func foo(number a)
            func foo(number a) return
            
            ví dụ 2 -> đúng
            func foo(number a) return
            
            ví dụ 3 -> sai  NoDefinition
            func foo(number a)
        """

        
        
        for i in self.listFunction:
            # print(type(j.values()),"abcxyz")
            if isinstance(i, FuncZcode):
                if i.body == False:
                    raise NoDefinition(ast.name.name)
             
        print("1234")
        # print("main", self.listFunction[0].get("main"))

        if self.listFunction.get("main"):
            
            print("3333")
            if isinstance(self.listFunction['main'], FuncZcode):
                if self.listFunction['main'].typ is not None:
                    raise NoEntryPoint()
                elif self.listFunction['main'].getSizeParam() != 0:
                    raise NoEntryPoint()
                elif not self.listFunction['main'].body:
                    raise NoEntryPoint()
        else:
            print("9999")
            raise NoEntryPoint()

        print(self.listFunction)


        
        # if isinstance(self.listFunction[0][j], FuncZcode):
        #     if j !='main':
        #         if not self.listFunction[0][j].getBody():
        #             raise NoDefinition(ast)
        #     elif j == 'main': 
        #         if self.listFunction[0][j].getType() is not None:
        #             raise NoEntryPoint(ast)
        #         elif self.listFunction[0][j].getSizeParam() != 0:
        #             raise NoEntryPoint(ast)
        #         elif not self.listFunction[0][j].getBody():
        #             raise NoEntryPoint(ast)
        #     else: raise NoEntryPoint(ast)
                        
        """
            TODO check No entry ponumber in self.listFunction
            ^ gợi ý: kiểm tra hàm main có trả về voidtype, không có param truyền vào hay không, có tồn tại main hay không
            #TODO check No entry Point in listFunction, tìm hàm tên "main"
             ví dụ 1 -> đúng
            func main() return
            
            ví dụ 2 -> đúng
            func main()
            func main() begin
            end
            
            ví dụ 3 -> sai NoEntryPonumber, sai param
            func main(number a) return
            
            ví dụ 4 -> sai NoEntryPonumber, sai returnType
            func main() return 1       
            
            ví dụ 5 -> sai NoEntryPonumber, không tồn tại
            không có hàm main     
        """   
        
  
        
    def visitVarDecl(self, ast, param):

        # for i in param[0]:
        if param[0].get(ast.name.name):
            # if type(param[0][ast.name.name]) == type(ast):
            raise Redeclared(Variable(), ast.name.name)

        # print("list", self.listFunction[0])
        # print("param", param[0])
        # print("var", ast, ast.name.name)

        """
            TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
            ^ gợi ý : tìm trong param[0] xem có tên trùm hay không
            ví dụ 1 -> đúng
            number a

            ví dụ 2 -> Redeclared(Variable(), ast.name.name)
            number a
            string a    
            
            ví dụ 3 -> Redeclared(Variable(), ast.name.name)
            func a()
            number a
        """       

        param[0][ast.name.name] = VarZcode(ast.varType) #! cập nhật param mới đưa tên vào, biến dynamic hay var sẽ type = None

        lhs = self.visit(ast.varType)
        rhs = self.visit(ast.VarInit)
        

        # if not isinstance(lhs, type(rhs)):
        #     if isinstance(lhs,(FuncZcode, VarZcode)) and isinstance(rhs,(FuncZcode, VarZcode)):
        #         raise TypeCannotBeInferred(ast.stmt)
        #     elif isinstance(lhs,(FuncZcode, VarZcode)) and not isinstance(rhs,(FuncZcode, VarZcode)):
        #         lhs.typ = type(rhs)
        #     elif not isinstance(lhs,(FuncZcode, VarZcode)) and isinstance(rhs,(FuncZcode, VarZcode)): 
        #         rhs.typ = type(lhs)
        # else:
        #     if not isinstance(lhs,(FuncZcode, VarZcode)):
        #         if self.comparType(lhs,rhs):
        #             raise TypeMismatchInStatement(ast.stmt)
        # param[0][ast.name.name] = VarZcode(ast.varType) 
        
        if lhs == type(rhs) == Zcode:
            raise TypeCannotBeInferred(ast)
        if isinstance(lhs, Zcode) and isinstance(rhs, ArrayZcode):
            raise TypeCannotBeInferred(ast)
        if not isinstance(lhs, Zcode) and isinstance(rhs, ArrayZcode):
            if isinstance(lhs,(StringType(), BoolType(), NumberType())):
                raise TypeMismatchInStatement(ast)
            if isinstance(lhs,ArrayType()):
                if not self.setTypeArray(lhs, rhs):
                    raise TypeMismatchInStatement(ast)
        if isinstance(lhs, Zcode) and isinstance(rhs,(StringType(), BoolType(), NumberType(), ArrayType())):
            lhs.typ = rhs
        elif isinstance(rhs, Zcode) and isinstance(lhs,(StringType(), BoolType(), NumberType(), ArrayType())):
            rhs.typ = lhs

        if lhs in (StringType(), BoolType(), NumberType(), ArrayType()) and rhs in (StringType(), BoolType(), NumberType(), ArrayType()):
            if not self.comparType(lhs, rhs):
                raise TypeMismatchInStatement(ast)
        """
            TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            
            ^ ý tưởng : visit RHS và LHS tìm được type (dùng isinstance)
            ^ có 2 loại là type bình thường (numbertype, stringtype, booleantype, arraytype) và type chưa xác định (FuncZcode, VarZcode)
            ^ TH1 : cả 2 đều trả về Zcode -> TypeCannotBeInferred -> cả 2 vế đều không suy diễn được
            ^ TH2, 3: nếu 1 trong 2 bên trả về Zcode bên kia xác định type thì gán type của Zcode với type đó -> suy diễn type của vế còn lại
            ^ TH4 : cả 2 đều có type nên kiểm tra xem 2 type có giống nhau không comparType -> TypeMismatchInStatement


            #* nguyên lí LHS (ast.varType) và RHS (ast.varInit), cả 2 đều là Type, chú ý LHS không bao giờ là ArrayZcode
                #^ TH1 cả 2 đều là Zcode chưa suy diễn được : raise TypeCannotBeInferred(ast)
                #^ TH2 nếu LHS là Zcode và RHS là ArrayZcode: raise TypeCannotBeInferred(ast) 
                #^ TH3 nếu LHS không phải Zcode và RHS là ArrayZcode:
                    #^ TH3.1 nếu LHS là string, bool, number : raise TypeMismatchInStatement(ast) 
                    #^ TH3.2 nếu LHS là arrayType kiểm tra self.setTypeArray(LHS, RHS) nếu không đúng raise TypeMismatchInStatement(ast)
                #^ TH4 nếu LHS là Zcode và RHS là string, bool, number, arrytype : LHS.typ = RHS
                #^ TH5 ngược lại TH4
                #^ TH6 cả LHS và RHS có kiểu string, bool, number, arrytype -> kiểm tra self.comparType(LHS, RHS): raise TypeMismatchInStatement(ast)
            #! TH1 TypeCannotBeInferred
            func foo()
            var a <- foo()    
            
            #! TH2 TypeCannotBeInferred(ast)
            dynamic x
            var a <- [x]
            
            #! TH3.1 TypeMismatchInStatement(ast)
            dynamic x
            number a <- [x] -> raise TypeMismatchInStatement(ast) 
            
            #! TH3.2 : X = arraytype([3], number)
            dynamic x
            number a[1][3] <- [x]
                        
            #! TH4, 5 : foo().typ = b.typ = numberType()
            func foo()
            number a <- foo()
            var b <- a            

            #! TH6 TypeMismatchInStatement
            number a <- "1"                
        """ 
        
        if ast.varInit: self.visit(ast.varInit, param)

    def visitFuncDecl(self, ast, param):
        
            # else: 
        """
            TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared 
            ^ gợi ý : tìm trong self.listFunction xem có tên trùm hay không, kiểm tra luôn phần body để xác định có khai báo 1 phần hay không
            ví dụ 1 -> đúng
            func foo() return

            ví dụ 2 -> đúng
            func foo()
            func foo() return
            
            ví dụ 3 -> Redeclared
            func foo() return
            func foo()

            ví dụ 4 -> Redeclared
            func foo()
            func foo()
            
            ví dụ 5 -> Redeclared
            func foo() return
            func foo() return

            ví dụ 5 -> Redeclared
            number foo
            func foo()
        """ 
 
        method = self.listFunction.get(ast.name.name)
        #TODO implement
        if self.listFunction.get(ast.name.name):
            if self.listFunction[0][ast.name.name].body or ast.body is None or isinstance():
                raise Redeclared(Function(), ast.name.name)
        
        
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        # param = self.visit(ast.param, param)
        # for i in len(self.visit(ast.param)):
        #     if listParam.get(ast.param[i]):
        #         raise Redeclared(Parameter(), ast.name.name)
        #     else:
        #         listParam.update(self.visit(ast.body, param))
        #         typeParam += type(self.visit(ast.body, param))

        for i in ast.param:
            # check = self.visit(i)
            print(type(i),"type i", i, i.typ)
            
            print(type(listParam),"type list", listParam)
            # if i in listParam:
            #     raise Redeclared(Parameter(), i.name.name)
            # else:
            #     listParam.update(i)
            #     typeParam += i

        # if param[0].get(ast.param):
        #     # if type(param[0][ast.name.name]) == type(ast):
        #     raise Redeclared(Variable(), ast.name.name)



        """
            TODO kiểm tra ast.param trong hàm trong listParam giống phần vardecl -> nén ra lỗi Redeclared 
            ^ cập nhật listParam (giống param) và typeParam (chỉ gồm các type)
            ^ typeParam = [numberType, stringType, ...]
            ví dụ 1 -> đúng Redeclared
            func foo(number a, string a) return
            ví dụ 1 -> đúng 
            func foo(number a, string b) return  
            -> typeParam = [numberType, stringType], listParam = {'a' : VarZcode(numberType), 'b' : VarZcode(stringType}         
            
            ví dụ 2 -> Redeclared
            func foo(number a, string a) return
        """ 
        # if param[0][ast.name.name].typ is None:
        #     param[0][ast.name.name].typ = VoidType()
        
        # self.Return = False #! kiểm tra hàm hiện tại có return hay không
        


        # param[0][ast.name.name] = FuncZcode(typeParam, None, True)
        # self.function = param[0][ast.name.name]
        # param[0][ast.name.name].typ = self.visit(ast.body, [listParam] + param)
        """
            TODO kiểm tra self.function = method hàm hiện tại chuẩn bị vào body nó xử lí
            ^ nhớ cập nhật self.function = self.listFunction[ast.name.name] -> xác định hàm hiện tại sẽ vào body của nó xử lí
            ^ TH1 : method đã tồn tại trước khi khai báo 1 phần (phần này đã có trong param) VD :
            func foo()
            func foo() begin -> đang xử lí bước này
            end
            
            ^ TH2 : method chưa tồn tại trước và khai báo 1 phần (phần này cập nhật trong param)
            func foo()
            
            ^ TH3 : method khai báo đầu đủ lần đầu không có khai báo 1 phần (phần này cập nhật trong param)
            func foo() begin
            end
            
            ^ Chú ý nếu mà có khai báo body TH1, TH3 -> khi về cuối mà type hàm không thay đổi thì gán về VoidType()
            func foo() begin 
            end     
            -> type foo là VoidType  
                 
            func foo() begin 
                return 1
            end     
            -> type foo là numberType
            ^ gợi ý : khi visit body thì thêm tầm vực mới là {listParam} -> self.visit(body, [{listParam}] + param)


            #^ TH1 : method khai báo 1 phần
                    #todo : cập nhật trong self.listFunction
            func foo()
            
                #^ TH2 : method đã khai bó 1 phần trước đó
                    #todo 1 : kiểm trả list param có giống nhau không không nếu không trả về Redeclared(Function(), ast.name.name)
                    #todo 2 : cập nhật self.listFunction[].body, self.Return, self.function và self.visit(ast.body, [listParam] + param) 
                    #todo 3 : sau khi gọi hàm kiểm tra self.Return có trong hàm hay không nếu không thì xác định typ nó VoidType, rồi xem xét với typ của hàm, nếu hàm cũng voidtype thì đúng nếu không thì lỗi  raise TypeMismatchInStatement(Return(None))
            func foo() 
            func foo() begin
            end
            
                #^ TH3 : method khai báo đầu đủ lần đầu không có khai báo 1 phần
                    #todo 1 : cập nhật self.listFunction[].body, self.Return, self.function, self.listFunction
                    #todo 2 : giống todo 3 trên
            func foo() begin 
            end
            
                #^ ví dụ todo 3 của TH2
            #! xác định kiểu
            func foo() begin 
            end     
            -> type foo là VoidType  
            
            #! xác định kiểu
            func foo()
            number a <- foo() -> foo() có typ là number
            func foo() begin  -> này lại có typ là void nên lỗi raise TypeMismatchInStatement(Return(None))
            end     
        
        """
        self.function = method
        self.Return = False
        if ast.body is None:
            self.listFuntion.update(method)
        
        #method = self.listFunction.get(ast.name.name)
        if method:
            if len(param) == len(typeParam):
                for i in param[0].values():
                    if i != typeParam[i]:
                        raise Redeclared(Function(), ast.name.name)
                #cập nhật self.listFunction[].body, self.Return, self.function và self.visit(ast.body, [listParam] + param) 
                self.listFunction[ast.name.name] = ast.body
                self.function = self.listFunction[ast.name.name]
                self.Return = False
                if self.function is not None:
                    self.function = VoidType()
            else: raise Redeclared(Function(), ast.name.name)
        else: 
            self.listFunction[ast.name.name] = ast.body
            self.function = self.listFunction[ast.name.name]
            self.Return = False
            if self.function is not None:
                self.function = VoidType()
            #todo: implement TH3
        #! hàm này không có return
        # if not self.Return:
        #     #! type cũng chưa có luôn ta xác định nó VoidType
        #     if self.listFunction[ast.name.name].typ is None:
        #         self.listFunction[ast.name.name].typ = VoidType()
        #     #! type đã có so sánh nó với VoidType
        #     elif not self.comparType(self.listFunction[ast.name.name].typ, VoidType()): 
        #         raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast, param):
        if not param[0].get(ast.name.name):
            raise Undeclared(Identifier(), ast.name.name)
        else: 
            id = param[0].get(ast.name.name)
            return id.typ if id.typ else id

        
        """
            TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
            ^ nếu không Undeclared thì return về Id.typ nếu VarZcode.typ != None còn nếu VarZcode.typ = None thì return VarZcode
            ^ nguyên lí nó truyền theo con trỏ trong c++, nếu thay đổi VarZcode thì param cũng thay đổi
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
                
            VD 1:
            number b <- a -> Undeclared(Identifier(), 'a') 
            
            VD 2:
            number a
            number b <- a -> a đã có VarZcode.typ nên return VarZcode.typ

            VD 3:
            var a
            number b <- a -> a có VarZcode.typ = None nên return VarZcode 
        """
   

    def visitCallExpr(self, ast, param):
        """
            TODO kiểm tra xem name có trong self.listFunction nén lỗi Undeclared
            kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
            VD 1: đúng 
            func foo()
            func main()begin
                var a <- foo()
            end
            
            VD 2: Undeclared
            func foo()
            func main()begin
                var a <- foo1()
            end
            
        """   
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ xét listLHS (là method.param) và listRHS (là ast.args)
                ^ nếu len khác nhau TypeMismatchInExpression
                ^ nếu self.comparType(LHS[i], RHS[i]) -> TypeMismatchInExpression

                ^ Xử lí từng phần tử theo nguyên lí LHS và RHS
            ^ nếu FuncZcode.typ is None thì return FuncZcode
            ^ nếu comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInExpression
            ^ còn lại return FuncZcode.typ (giống phần VarZcode)
            #! trả về giá trị giống ý tưởng của visitID
        """
        method = self.listFunction.get(ast.name.name)
        
        if ast.varInit: self.visit(ast.varInit, param)
        if not self.listFunction.get(ast.name.name):
            raise Undeclared(Function(), ast.name.name)
        listLHS = method.param
        listRHS = ast.args
        if len(listLHS) == len(listRHS):
            raise TypeMismatchInExpression(ast)
        for i in len(listLHS):
            if self.comparType(LHS[i], RHS[i]):
                raise TypeMismatchInExpression(ast)
        if isinstance(listLHS, Zcode) and isinstance(listRHS, (Zcode, ArrayZcode)):
            raise TypeCannotBeInferred(ast)
        elif isinstance(listLHS, (StringType(), NumberType(), BoolType(), ArrayType())) and isinstance(listRHS, ArrayZcode):
            if isinstance(listLHS, (StringType(), NumberType(), BoolType())):
                raise TypeMismatchInExpression(ast)
            elif isinstance(listLHS, ArrayType()):
                if not self.setTypeArray(LHS, RHS):
                    raise TypeMismatchInExpression(ast)
        elif isinstance(listLHS, Zcode) and isinstance(listRHS, (StringType(), NumberType(), BoolType(), ArrayType())):
            LHS.typ = RHS
        elif isinstance(listRHS, Zcode) and isinstance(listLHS, (StringType(), NumberType(), BoolType(), ArrayType())):
            RHS.typ = LHS
        elif isinstance(listLHS, (StringType(), NumberType(), BoolType(), ArrayType())) and isinstance(listRHS, (StringType(), NumberType(), BoolType(), ArrayType())):
            if not self.comparType(LHS, RHS):
                raise TypeMismatchInExpression(ast)
        
        if method.typ is not None:
            return method
        elif self.comparType(method.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        else: return method.typ if method.typ else method


    

    def visitCallStmt(self, ast, param):
        """như CallExpr chỉ khác ở chỗ not comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInStatement"""
        method = self.listFunction.get(ast.name.name)
        #TODO implement
        if ast.varInit: self.visit(ast.varInit, param)
        if not self.listFunction.get(ast.name.name):
            raise Undeclared(Function(), ast.name.name)
        listLHS = method.param
        listRHS = ast.args
        if len(listLHS) == len(listRHS):
            raise TypeMismatchInExpression(ast)
        for i in len(listLHS):
            if self.comparType(LHS[i], RHS[i]):
                raise TypeMismatchInExpression(ast)
        if isinstance(listLHS, Zcode) and isinstance(listRHS, (Zcode, ArrayZcode)):
            raise TypeCannotBeInferred(ast)
        elif isinstance(listLHS, (StringType(), NumberType(), BoolType(), ArrayType())) and isinstance(listRHS, ArrayZcode):
            if isinstance(listLHS, (StringType(), NumberType(), BoolType())):
                raise TypeMismatchInExpression(ast)
            elif isinstance(listLHS, ArrayType()):
                if not self.setTypeArray(LHS, RHS):
                    raise TypeMismatchInExpression(ast)
        elif isinstance(listLHS, Zcode) and isinstance(listRHS, (StringType(), NumberType(), BoolType(), ArrayType())):
            LHS.typ = RHS
        elif isinstance(listRHS, Zcode) and isinstance(listLHS, (StringType(), NumberType(), BoolType(), ArrayType())):
            RHS.typ = LHS
        elif isinstance(listLHS, (StringType(), NumberType(), BoolType(), ArrayType())) and isinstance(listRHS, (StringType(), NumberType(), BoolType(), ArrayType())):
            if not self.comparType(LHS, RHS):
                raise TypeMismatchInExpression(ast)
        
        if method.typ is not None:
            return method
        elif not self.comparType(method.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        else: return method.typ if method.typ else method

    def visitIf(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ ast.expr có LHS = BoolType(), RHS = self.visit(ast.expr, param)
            ^ body khi visit nhớ thêm 1 tầm vực mới

            _typExpr_
            # TODO giống phần kiểm tra TypeMismatchInStatement theo nguyên lí LHS và RHS
                #^ xét typExpr và self.visit(ast.thenStmt, [{}] + param)
            ^ LHS = BoolType(), RHS = self.visit(ast.expr, param)
        """   
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        
        
            
        if ast.typExpr is not None:
            self.visit(ast.thenStmt, [{}] + param)
            if isinstance(RHS, ArrayZcode):
                raise TypeMismatchInStatement(ast)
            elif isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif isinstance(RHS, (StringType(), NumberType(), BoolType(), ArrayType())):
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast)

        if ast.varInit: self.visit(ast.varInit, param)
        if ast.elifStmt is not None:
            self.visit(ast.thenStmt, [{}] + param)
            if isinstance(RHS, ArrayZcode):
                raise TypeMismatchInStatement(ast)
            elif isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif isinstance(RHS, (StringType(), NumberType(), BoolType(), ArrayType())):
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast)
        
        """
            TODO kiểm tra elseStmt
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """           
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
     
    def visitFor(self, ast, param):

        """_typID_
            #TODO giống mấy thằng trong if, LHS = NumberType()
        """        
        LHS = NumberType()
        RHS = self.visit(ast.expr, param)
        if ast.typID is not None:
            self.visit(ast.thenStmt, [{}] + param)
            if isinstance(RHS, ArrayZcode):
                raise TypeMismatchInStatement(ast)
            elif isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif isinstance(RHS, (StringType(), NumberType(), BoolType(), ArrayType())):
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast)
        """_typCondExpr_
            #TODO giống mấy thằng trong if, LHS = BoolType()
        """    
        #TODO implement

        """_typUpdExpr_
            #TODO giống mấy thằng trong if, LHS = NumberType()
        """            
        #TODO implement      
        
 
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tăng tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    

    def visitReturn(self, ast, param):
        """
            TODO giống phần kiểm tra TypeCannotBeInferred (ném ra ast) và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ chú ý : ban đầu sẽ xem xét ast.expr = none hay không để gán VoidType()
            ^ xét self.function.typ và typeReturn (type sau khi visit) giống lHS và RHs nhưng self.function.typ nhận giá trị None (suy nghĩ giống Zcode) or Type
            ^ LHS =  self.function.typ, RHS = ......

            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement nguyên lí LHS và RHS
                #^ LHS là self.function.typ if self.function.typ else self.function
                #^ RHS là self.visit(ast.expr, param) if ast.expr else VoidType()
        """
        self.Return = True
        # LHS = self.function.typ if self.function.typ else self.function
        # RHS = self.visit(ast.expr, param) if ast.expr else VoidType()

        #TODO implement  


    def visitAssign(self, ast, param):
        """
            TODO giống phần kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        """
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)

        #TODO implement
            

    def visitBinaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ visit left và right của BinaryOp
            ^ ['+', '-', '*', '/', '%'] -> kiểu numbertype -> return Numbertype
              ^ nếu left và right đề có type -> kiểm tra nén lỗi TypeMismatchInExpression
              ^ nếu in trong 2 left và right đề có type -> kiểm tra nén lỗi TypeMismatchInExpression và gán type left/right
              ^ nếu cả 2 left và right là kiểu Zcode -> gán type left và right
            ^ ['=', '!=', '<', '>', '>=', '<='] -> kiểu numbertype -> return Numbertype
            ^ ['and', 'or'] -> kiểu booltype -> return booltype
            ^ ['=='] -> kiểu stringtype -> return booltype
            ^ ['...'] -> kiểu stringtype -> return stringtype
            
            ^ gợi ý ['+', '-', '*', '/', '%']
                ^ b + c
                ^ xét đầu tiên là LHS_b = NumberType, RHS_b = self.visit(b)
                ^ xét đầu tiên là LHS_c = NumberType, RHS_c = self.visit(c)
                ^ return NumberType
        """        
        LHS = self.visit(ast.e1,param)
        RHS = self.visit(ast.e2,param)
        if op in ['+', '-', '*', '/', '%']:
            if type(left) is None:
                left.typ = NumberType()
            if type(right) is None:
                right.typ = NumberType()
            if type(left) != type(right):
                raise TypeMismatchInExpression(ast)
            else:
                if type(left) in [StringType, BoolType, ArrayType]:
                    raise TypeMismatchInExpression(ast)
            if isinstance(left, Zcode) and isinstance(right, Zcode):
                right.typ = NumberType()
                left.typ = NumberType()

            return NumberType()
        if op in ['=', '!=', '<', '>', '>=', '<=']:
            if type(left) != type(right):
                raise TypeMismatchInExpression(ast)
            elif type(left) != NumberType():
                raise TypeMismatchInExpression(ast)
            else: return NumberType()

        if op in ['and', 'or']:
            if type(left) != type(right):
                raise TypeMismatchInExpression(ast)
            elif type(left) != BoolType():
                raise TypeMismatchInExpression(ast)
            else: return BoolType()

        if op in ['==']:
            if type(left) != type(right):
                raise TypeMismatchInExpression(ast)
            elif type(left) != StringType():
                raise TypeMismatchInExpression(ast)
            else: return BoolType()

        if op in ['...']:
            if type(left) != type(right):
                raise TypeMismatchInExpression(ast)
            elif type(left) != StringType():
                raise TypeMismatchInExpression(ast)
            else: return StringType()
        #! vì các Association đều là left nên tiến hành ở left rồi tiếp theo right, thầy mà cho có Association right thì trúng bẫy hết
        op = ast.op
        """_left_ 
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInExpression nguyên lí LHS và RHS
            #* giống mấy thằng trong if
            #! op in ['+', '-', '*', '/', '%']
                #^ LHS = NumberType(), left = self.visit(ast.left, param)
            #! op in ['=', '!=', '<', '>', '>=', '<=']
                #^ LHS = NumberType(), left = self.visit(ast.left, param)
            #! op in ['and', 'or']
                #^ LHS = boolType(), left = self.visit(ast.left, param)
            #! op in ['==']
                #^ LHS = StringType(), left = self.visit(ast.left, param)           
            #! op in ['...']
                #^ LHS = StringType(), left = self.visit(ast.left, param)  
        """        
        
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)
        #TODO implement
        if op in ['+', '-', '*', '/', '%']:
            LHS = NumberType, left = self.visit(ast.left, param)
        if op in ['=', '!=', '<', '>', '>=', '<=']:
            LHS = NumberType, left = self.visit(ast.left, param)

        """_right_        
            TƯƠNG TỰ LEFT     
        """        
        #TODO implement
        
  

    def visitUnaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ visit ast.operand của UnaryOp
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       

        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí giống BinaryOp
            #* giống mấy thằng trong if
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       
        right = self.visit(ast.operand, param)
        op = ast.op
        #TODO implement   
        
        if ast.varInit: self.visit(ast.varInit, param)    
            


    def visitArrayCell(self, ast, param):
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần type ast.arr phải là array type ->  TypeMismatchInExpression -> không thể suy diễn kiểu biết arraytype phần tham số đâu :((, nên hỏi thầy đi nha 
        """ 
        left = self.visit(ast.arr, param)
        if type(left) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần ast.idx với LHS = NumberType(), RHS = .... từng phần tử trong ast.idx
            #* giống mấy thằng trong if
            ^ từng phần tử trong ast.idx với LHS = NumberType(), RHS = ....
        """         
   
        LHS = NumberType()
        RHS = self.visit(ast.expr, param)
       
        """
            TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
            ^ left là sau khi visit ast.arr: Expr 
            ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
            number a[1,2]
            var c <- a[1,2,3]
            ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
            number a[1,2]
            var c <- a[1,2] -> c : numbertype
            ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
            number a[1,2,3]
            var c <- a[1] -> c : number c[2,3]                   
        """ 
   
        """
            # TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
            ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
            number a[1,2]
            var c <- a[1,2,3]
            ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
            number a[1,2]
            var c <- a[1,2] -> c : numbertype
            ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
            number a[1,2,3]
            var c <- a[1] -> c : number c[2,3]                   
        """ 
        #TODO implement
        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(left.size) == len(ast.idx):
            return left.eleType
        elif len(left.size) > len(ast.idx):
            return arrayType(left.size[len(ast.idx):], left.eleType)

            


    """phần này sẽ là cố định do ngắn quá :(( """
    def visitArrayLiteral(self, ast, param):
        # #! code chỉ mang tính tham khảo, do BTL này không yêu cầu lỗi khác nhau ArrayLiteral nên thầy ko cho TypeCannotBeInferred
        # for item in ast.value: self.visit(item, param)
        # typ = self.visit(ast.value[0], param)
        
        # #! đệ quy
        # if type(typ) in [StringType, BoolType, NumberType]:
        #     return ArrayType([len(ast.value)], typ)
        # return ArrayType([len(ast.value)] + typ.size, typ.eleType)



        #* bước 1 chọn được type đã xác định kiểm trong ast.value (typ không phải là Zcode và ArrayZcode)
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break
        
        #* Bước 2: xét kiểu từng phần tử
        #^ TH1 : typ is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        #^ TH2 : typ in [StringType, BoolType, NumberType] duyệt qua ast.value nếu typ từng phần tử có ArrayZcode hay là comparType bị khác thì nén TypeMismatchInExpression
        """_VD_
            [1, x, "2", [y]] -> lỗi TypeMismatchInExpression vì khác type trong array
            #* ta tìm được typ = NumberType (vì 1 là giá trị đầu tiên tìm được)
            #* ta bắt đầu so sánh LHS = NumberType, RHS = duyệt từ 0 -> n của từng phần tử trong ast.value
                #! index = 0 -> LHS = NumberType, RHS = NubmerType -> đúng
                #! index = 1 -> LHS = NumberType, RHS = VarZcode('x') -> x.typ = NumberType -> đúng
                #! index = 2 -> LHS = NumberType, RHS = StringType -> sai -> TypeMismatchInExpression
                #! index = 3 -> LHS = NumberType, RHS = ArrayZcode([VarZcode('y')]) -> sai -> TypeMismatchInExpression
        """
        if typ is None:
            return ArrayZcode
        elif type(typ) in [StringType, BoolType, NumberType]:
            for i in ast.value:
                test = self.visit(i, param)
                if isinstance(test, VarZcode):
                    if test.typ is None:
                        test.typ = typ
                elif isinstance(test,ArrayZcode) or not self.comparType(typ, test):
                    raise TypeMismatchInExpression(ast)
        else: 
            if isinstance(typ, ArrayType()):
                for i in ast.value:
                    test = self.visit(i, param)
                    if isinstance(test, VarZcode):
                        if test.typ is None:
                            test.typ = typ
                    elif isinstance(test, ArrayType()):
                        if test.size != typ.size or test.eleType != typ.eleType:
                            raise TypeMismatchInExpression(ast)
                    elif isinstance(test, ArrayZcode):
                        self.setTypeArray(typ, test)


                
        #^ TH3 : typ in arraytype duyệt qua ast.value giống TH2 nhưng nếu ArrayType yêu cầu dùng setTypeArray để chỉnh typ 
        """_VD_
            [x, [1], [1,2], [y]] -> lỗi TypeMismatchInExpression vì khác type trong array
            #* ta tìm được typ = ArrayType([1], numberType) (vì 1 là giá trị thứ 2 tìm được)
            #* ta bắt đầu so sánh LHS = ArrayType([1], numberType), RHS = duyệt từ 0 -> n của từng phần tử trong ast.value
                #! index = 0 -> LHS = ArrayType([1], numberType), RHS = VarZcode('x') -> x.typ = ArrayType([1], numberType) -> đúng
                #! index = 1 -> LHS = ArrayType([1], numberType), RHS = ArrayType([1], numberType) -> đúng
                #! index = 2 -> LHS = ArrayType([1], numberType), RHS = ArrayType([2], numberType) -> sai -> TypeMismatchInExpression
                #! index = 3 -> LHS = ArrayType([1], numberType), RHS = ArrayZcode([VarZcode('y')]) -> gọi setTypeArray
                    #* ta thu được y = numberType -> đúng
        """
        # else:
            #TODO implement

            
    
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)           
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()