import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_declared(self):
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
        input = """
            string x <- 1
        """
        expect = str(Program([
                VarDecl(Id("x"), StringType(), None, NumberLiteral(1.0))
            ]))
        
        self.assertTrue(TestAST.test(input, expect, 302))
        
        input = """
            bool a <- 1
        """
        expect = str(Program([
                VarDecl(Id("a"), BoolType(), None, NumberLiteral(1.0)),
            ]))
        
        self.assertTrue(TestAST.test(input, expect, 303))
        
        input = """
            string a[5] <- 1
            string b[5]
        """
        expect = str(Program([
                VarDecl(Id("a"), ArrayType([5.0], StringType()), None, NumberLiteral(1.0)),
                VarDecl(Id("b"), ArrayType([5.0], StringType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 304))
        
        input = """
            bool a<- false
        """
        expect = str(Program([
                VarDecl(Id("a"), BoolType(), None, BooleanLiteral(False)),
            ]))
        
        self.assertTrue(TestAST.test(input, expect, 305))
        
        input = """
            dynamic a <- 1
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.0))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 306))
        
        input = """
            dynamic x
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "dynamic",None)
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 307))
        
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 308))
        
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 309))

        input = """
            func main()
                begin
                    break
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break()]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 310))
                
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
        """ 
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None)
                ]))
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_Expression(self):
        input = """
            var x <- 1
            var x <- "123"
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                    VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 312))
        
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 313))   
        
        input = """
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 314))  
        
        input = """
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 315))  
        
        input = """
            var x <- 2 or 3 and 1 <= 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)))
            ]))
        
        self.assertTrue(TestAST.test(input, expect, 316))  
        
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 317))  
        
        input = """
            var x <- foo()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("foo"), []))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 318)) 
        
        input = """
            var x <- foo(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("foo"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
        input = """
            var x <- foo(foo())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("foo"), [CallExpr(Id("foo"), [])]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 320)) 
        
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 321)) 
         
    def test_Statements(self):
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 322))

        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                    Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 323))
        
        input = """
            func main()
                begin
                    return
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return()])),
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 324))

        input = """
            func main()
                begin
                    foo(a)
                    foo(1,1)
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("foo"), [Id("a")]),
                    CallStmt(Id("foo"), [NumberLiteral(1.0), NumberLiteral(1.0)])]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 325))
        
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 326))
        
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 327))
        
        input = """
            func main()
                begin
                    if (true) return 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [] , None)]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 328))
        

        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 2
                    elif (true) return 3
                    else return 4
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
                       [(BooleanLiteral(True),Return(NumberLiteral(2.0))),
                        (BooleanLiteral(True),Return(NumberLiteral(3.0)))] 
                    ,Return(NumberLiteral(4.0)))]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 329))     
        
        input = """
            var c <- foo()[1,2]
            var c <- foo(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("foo"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("foo"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        
        self.assertTrue(TestAST.test(input, expect, 330))    
        
        input = """
            func main()
            begin
                var c <- 2e5
                dynamic c <- 2.56
                dynamic c
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("c"), None, "var", NumberLiteral(200000.0)), 
                 VarDecl(Id("c"), None, "dynamic", NumberLiteral(2.56)), 
                 VarDecl(Id("c"), None, "dynamic"),
            ]))]))
        
        self.assertTrue(TestAST.test(input, expect, 331))    
        
        
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 2
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(2.0))), [], None)
            ]))]))
        
        self.assertTrue(TestAST.test(input, expect, 332))     
        
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 2
                    else return 3
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(2.0))), 
               [], Return(NumberLiteral(3.0)))
            ]))]))
        
        self.assertTrue(TestAST.test(input, expect, 333))   
        
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 2
                        else return 3
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(2.0)))], Return(NumberLiteral(3.0))), [], None)
            ]))]))
        
        self.assertTrue(TestAST.test(input, expect, 334))   
        
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 2
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(2.0)))]), [], None)
            ]))]))
        
        self.assertTrue(TestAST.test(input, expect, 335))   
        
        input = """
            func main()
                begin
                    if (true)
                        return 2                        
                    else return 123
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), Return(NumberLiteral(2.0)), [], Return(NumberLiteral(123.0)))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 336))   

        input = """
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                FuncDecl(Id("main"), [VarDecl(Id("a"),ArrayType([1.0,2.0], NumberType()), None, None)], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 337))
        
        input = """
            var x <- [[1], [1]]
        """
        expect = str(Program([
                VarDecl(Id("x"), None, 'var', ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 338))
        
        input = """
            var x <- 1 and 2 or 3
        """
        expect = str(Program([
                VarDecl(Id("x"), None, 'var', BinaryOp("or",BinaryOp("and",NumberLiteral(1.0),NumberLiteral(2.0)), NumberLiteral(3.0)))
            ]))
        self.assertTrue(TestAST.test(input, expect, 339))
        
        input = """
            var x <- a[1,2,3]
        """
        expect = str(Program([
                VarDecl(Id("x"), None, 'var', ArrayCell(Id("a"),[NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 340))
        
        input = """
            var x <- ---1
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0)))))
            ]))
        self.assertTrue(TestAST.test(input, expect, 341))
        
        input = """
            var x <- not not -1
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  UnaryOp("not", UnaryOp("not", UnaryOp("-", NumberLiteral(1.0)))))
            ]))
        self.assertTrue(TestAST.test(input, expect, 342))
        
        input = """
            var x <- 1 ... "2"
        """
        expect = str(Program([
                VarDecl(Id("x"), None, 'var', BinaryOp("...", NumberLiteral(1.0), StringLiteral("2")))
            ]))
        self.assertTrue(TestAST.test(input, expect, 343))
        
        input = """
            var x <- 1 <= "2"
        """
        expect = str(Program([
                VarDecl(Id("x"), None, 'var', BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2")))
            ]))
        self.assertTrue(TestAST.test(input, expect, 344))
        
        input = """
            func main()
                begin
                    a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(3.0)]), NumberLiteral(1.0))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 345))
        
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 346))
        
        input = """
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"), [], Block([For(Id("i"),Id("i"),ArrayLiteral([NumberLiteral(1.0)]), Block([ CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 347))
        
        input = """
            func main()
                begin
                    if (true) return 2
                    else return 3
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"), [], Block([If(BooleanLiteral(True),Return(NumberLiteral(2.0)),[], Return(NumberLiteral(3.0)))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 348))
        
        input = """
            var c <- a[1,2]
        """
        expect = str(Program([
                VarDecl(Id("c"),None, 'var', ArrayCell(Id("a"),[NumberLiteral(1.0), NumberLiteral(2.0)]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 349))
        
        input = """
            ##abc
            var a <- 1
            ##xyz
        """
        expect = str(Program([
                VarDecl(Id("a"), None, 'var', NumberLiteral(1.0))
            ]))
        self.assertTrue(TestAST.test(input, expect, 350))
        
        input = """
            bool a <- true
        """
        expect = str(Program([
                VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True))
            ]))
        self.assertTrue(TestAST.test(input, expect, 351))
        
        input = """
            string a <- "game" ... "so ez"
        """
        expect = str(Program([
                VarDecl(Id("a"), StringType(), None, BinaryOp("...", StringLiteral("game"),StringLiteral("so ez")))
            ]))
        self.assertTrue(TestAST.test(input, expect, 352))
        
        input = """
            var a <- 2 > 1
        """
        expect = str(Program([
                VarDecl(Id("a"), None, 'var', BinaryOp(">", NumberLiteral(2.0), NumberLiteral(1.0)))
            ]))
        self.assertTrue(TestAST.test(input, expect, 353))
        
        input = """
            func main() 
            begin   
                if(1+1) api <- 1
                
            end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    If(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), Assign(Id("api"), NumberLiteral(1.0)), [], None)]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 354))
        
        input = """
            func main() 
            begin   
                if(1+1) api <- 1
                elif (true) continue
            end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    If(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), Assign(Id("api"), NumberLiteral(1.0)), [(BooleanLiteral(True), Continue())])]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 355))
        
        input = """
            func main() begin
            end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 356))
        
        input = """
            func main()
                begin
                    for i until i > 10 by i+1
                        a <- 1
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    For(Id("i"),BinaryOp(">",Id("i"), NumberLiteral(10.0)), BinaryOp("+",Id("i"), NumberLiteral(1.0)), Assign(Id("a"), NumberLiteral(1.0)))
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 357))
        
        input = """
            func main()
                begin
                    for i until i > 10 by i+1
                        a <- 1
                    break
                    continue
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    For(Id("i"),BinaryOp(">",Id("i"), NumberLiteral(10.0)), BinaryOp("+",Id("i"), NumberLiteral(1.0)), Assign(Id("a"), NumberLiteral(1.0))), Break(), Continue()]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 358))
        
        input = """
            func main()
                begin
                    for i until i > 10 by i+1
                    begin
                        a <- 1
                        continue
                        end
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    For(Id("i"),BinaryOp(">",Id("i"), NumberLiteral(10.0)), BinaryOp("+",Id("i"), NumberLiteral(1.0)), Block([Assign(Id("a"), NumberLiteral(1.0)), Continue()]))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 359))
        
        input = """
            func main()
                begin
                    for i until i >= 10 by 1 + 1
                        API <- 1
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    For(Id("i"),BinaryOp(">=",Id("i"), NumberLiteral(10.0)), BinaryOp("+",NumberLiteral(1.0), NumberLiteral(1.0)), Assign(Id("API"), NumberLiteral(1.0)))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 360))
        
        input = """
            func main()
            return
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 361))
        
        input = """
            func main()
                return 
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 362))
        
        input = """
            func main()
                return 
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 363))
        
        input = """
            func main() return  ##1
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 364))
        
        input = """
            number x <- 2
        """
        expect = str(Program([
                VarDecl(Id("x"), NumberType(), None, NumberLiteral(2.0))
            ]))
        self.assertTrue(TestAST.test(input, expect, 365))
        
        input = """
            func main()
                begin
                    if i <= 1 return false
                end ##1
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([If(BinaryOp("<=", Id("i"), NumberLiteral(1.0)),Return(BooleanLiteral(False)),[], None)]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 366))
        
        input = """
            func main()
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], None)
            ]))
        self.assertTrue(TestAST.test(input, expect, 367))
        
        input = """
            func main()
                return 
            var a <- [1]
        """
        expect = str(Program([
                FuncDecl(Id("main"), [], Return()),
                VarDecl(Id("a"), None, 'var', ArrayLiteral([NumberLiteral(1.0)])),
            ]))
        self.assertTrue(TestAST.test(input, expect, 368))
        
        input = """
            number a <- c()[1]
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType(), None, ArrayCell(CallExpr(Id("c"), []), [NumberLiteral(1.0)]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 369))
        
        input = """
            
            string a <- "string"
        """
        expect = str(Program([
                VarDecl(Id("a"), StringType(), None, StringLiteral("string"))
            ]))
        self.assertTrue(TestAST.test(input, expect, 370))
        
        input = """
            bool a <- "string"
        """
        expect = str(Program([
                VarDecl(Id("a"), BoolType(), None, StringLiteral("string"))
            ]))
        self.assertTrue(TestAST.test(input, expect, 371))
        
        input = """
            func main()
                begin
                    var i<- 0
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"), [], Block([
                    VarDecl(Id("i"), None, 'var', NumberLiteral(0.0))
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 372))
        
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
        """
        expect = str(Program([
                FuncDecl(Id("areDivisors"), [
                    VarDecl(Id("num1"), NumberType(),None, None),
                    VarDecl(Id("num2"), NumberType(), None, None)
                ], Return(BinaryOp("or", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0)))))
            ]))
        self.assertTrue(TestAST.test(input, expect, 373))
        
        input = """
            func isPrime(number x)
        """
        expect = str(Program([
                FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())])
            ]))
        self.assertTrue(TestAST.test(input, expect, 374))
        
        input = """
                var a <- r * r * 3.14
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, 'var', 
                        BinaryOp("*", 
                            BinaryOp("*", Id('r'), Id('r')), 
                            NumberLiteral(3.14)))
            ]))
        self.assertTrue(TestAST.test(input, expect, 375))
        
        input = """
                number aPI <- 3.14
                number l[3] <- value * aPI
        """
        expect = str(Program([
                VarDecl(Id("aPI"), NumberType(), None, NumberLiteral(3.14)),
                VarDecl(Id("l"), ArrayType([3.0], NumberType()), None, BinaryOp("*", Id("value"), Id("aPI")))
            ]))
        self.assertTrue(TestAST.test(input, expect, 376))
        
        input = """
            func main()
                return 
        """
        expect = str(Program([
                FuncDecl(Id("main"), [], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 377))
        
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) ... (num2 % num1 = 0))
        """
        expect = str(Program([
                FuncDecl(Id("areDivisors"), [
                    VarDecl(Id("num1"), NumberType(),None, None),
                    VarDecl(Id("num2"), NumberType(), None, None)
                ], Return(BinaryOp("...", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0)))))
            ]))
        self.assertTrue(TestAST.test(input, expect, 378))
        
        input = """
            func main()
                begin
                    for i until i >= 10 by 1 + 1
                        a <- 1
                end
        """
        expect = str(Program([
                FuncDecl(Id("main"),[], Block([
                    For(Id("i"),BinaryOp(">=",Id("i"), NumberLiteral(10.0)), BinaryOp("+",NumberLiteral(1.0), NumberLiteral(1.0)), Assign(Id("a"), NumberLiteral(1.0)))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 379))
        
        input = """
            func main()
            begin
                aPI[2]<- 3.14
            end
        """
        expect = str(Program([
                FuncDecl(Id("main"), [], Block([
                    Assign(ArrayCell(Id("aPI"), [NumberLiteral(2.0)]), NumberLiteral(3.14))
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 380))
        
        input = """
            var a <- b()[a ... 33]
        """
        expect = str(Program([
                VarDecl(Id("a"), None, 'var', ArrayCell(CallExpr(Id("b"), []), [BinaryOp("...", Id("a"), NumberLiteral(33.0))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 381))
        
        input = """
            var a <-55 + 3
        """
        expect = str(Program([
                VarDecl(Id("a"), None, 'var', BinaryOp("+", NumberLiteral(55.0) , NumberLiteral(3.0)))
            ]))
        self.assertTrue(TestAST.test(input, expect, 382))
        
        input = """
        var x <- foo()
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  CallExpr(Id("foo"), []))
            ]))
        self.assertTrue(TestAST.test(input, expect, 383))
        
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 384))
        
        input = """
            number a <- true > false
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType(), None, BinaryOp(">", BooleanLiteral(True), BooleanLiteral(False)))
            ]))
        self.assertTrue(TestAST.test(input, expect, 385))
        
        input = """
            string a <- 1 >=3
        """
        expect = str(Program([
                VarDecl(Id("a"), StringType(), None, BinaryOp(">=", NumberLiteral(1.0), NumberLiteral(3.0)))
            ]))
        self.assertTrue(TestAST.test(input, expect, 386))
        
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 387))
        
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 388))
        
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 389))
        
        input = """
            number a
        """
        expect = str(Program([
                VarDecl(Id("a"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 390))
        
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 391)) 
         
    def test_Statements(self):
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 392))

        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                    Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 393))
        
        input = """
            func main()
                begin
                    return
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return()])),
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 394))

        input = """
            func main()
                begin
                    foo(a)
                    foo(1,1)
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("foo"), [Id("a")]),
                    CallStmt(Id("foo"), [NumberLiteral(1.0), NumberLiteral(1.0)])]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 395))
        
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 396))
        
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 397))
        
        input = """
            func main()
                begin
                    if (true) return 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [] , None)]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 398))
        

        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 2
                    elif (true) return 3
                    else return 4
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
                       [(BooleanLiteral(True),Return(NumberLiteral(2.0))),
                        (BooleanLiteral(True),Return(NumberLiteral(3.0)))] 
                    ,Return(NumberLiteral(4.0)))]))
                ]))
        
        self.assertTrue(TestAST.test(input, expect, 399))     
        
        input = """
            var c <- foo()[1,2]
            var c <- foo(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("foo"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("foo"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        
        self.assertTrue(TestAST.test(input, expect, 400))