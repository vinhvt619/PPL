import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """func foo(number a[5], string b)
                    begin
                        var i <- 0
                        for i until i >= 5 by 1
                            begin
                                a[i] <- i * i + 5
                            end
                        return -1
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test2(self):
        input = """
            var API <- 3.14
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test3(self):
        input = """
            number l[3] <- 3 * 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test4(self):
        input = """
                    func areDivisors(number num1, number num2)
                        return ((num1 % num2 = 0) or (num2 % num1 = 0))
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test5(self):
        input = """break"""
        expect = "Error on line 1 col 0: break"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test6(self):
        input = """continue"""
        expect = "Error on line 1 col 0: continue"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test7(self):
        input = """
                func main()
                    begin
                        var num1 <- readNumber()
                        var num2 <- readNumber()
                        if (areDivisors(num1, num2)) writeString("Yes")
                        else writeString("No")
                    end


            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test8(self):
        input = """func main()
                begin
                    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test9(self):
        input = """func main()
                begin
                    number r
                    number s
                    r <- 2.0
                    number a[5]
                    number b[5]
                    s <- r * r * 3.14
                    a[0] <- s
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test10(self):
        input = """func areDivisors(number num1, number num2)
                        return ((num1 % num2 = 0) or (num2 % num1 = 0))
                    func main()
                        begin
                            var num1 <- readNumber()
                            var num2 <- readNumber()
                            if (areDivisors(num1, num2)) writeString("Yes")
                            else writeString("No")
                        end
                        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test11(self):
        input = """func constructor(length, width: int) 
            selflength = length
            selfwidth = width
        """
        expect = "Error on line 1 col 17: length"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test12(self):
        input = """
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test13(self):
        input = """
        func main()
            return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test14(self):
        input = """
        class Shape  
            var length, width: int; 
            func getArea(): int  
                return self.length * self.width; 
             """
        expect = "Error on line 2 col 8: class"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test15(self):
        input = """
            func main(number num1, number num2)
                ##var numb <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 4 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test16(self):
        input = """
            func main(number num1, number num2)
                ##number=1
            func main(number f1)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test17(self):
        input = """int abc;"""
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test18(self):
        input = """
            func main()
            ## NBA
            func main(string a) ## WWE
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test19(self):
        input = """class Shape
            func setLength(): int
                return self.length = 5;
            
        """
        expect = "Error on line 1 col 0: class"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test20(self):
        input = """
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test21(self):
        input = """
            ##abc
            ##xyz
            func main(number a) return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test22(self):
        input = """
            func main(number a)
                continue
        """
        expect = "Error on line 3 col 16: continue"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test23(self):
        input = """
            func main(number a)
                break    
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test24(self):
        input = """
            func main(number a)
            ##ez
                begin
                end
                ##abc
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test25(self):
        input = """
            func main(number a)
            ##ez
                begin
                    break
                end
                ##abc
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test26(self):
        input = """
            ##abc
            var a <- 1
            ##xyz
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test27(self):
        input = """number a <- 1"""
        expect = "Error on line 1 col 13: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test28(self):
        input = """bool a <- false"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test29(self):
        input = """
            bool a <- true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test30(self):
        input = """
            string a <- "game" ... "so ez"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test31(self):
        input = """
            number a <- 1+2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test32(self):
        input = """
            var a <- 2 > 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test33(self):
        input = """
            begin   
                if(1+1) api <- 1
                ##1
                
                if(1+2 > 3) 
                    ##2
                    api <- 2
                    ##3
                else api <- 3
                ##4
                if api <- 1
                elif 1 ... 2
                    ##5
                    api <- 1
                    ##6
                elif 1 api <- 1
                
                if 1 api <- 1
                elif continue
                elif break
                else return
                ##8
            end
        """
        expect = "Error on line 2 col 12: begin"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test34(self):
        input = """
        func main() begin   
                if(1+1) api <- 1
                ##1
                
                if(1+2 > 3) 
                    ##2
                    api <- 2
                    ##3
                else api <- 3
                ##4
                if 1 api <- 1
                elif 1 ... 2
                    ##5
                    api <- 1
                    ##6
                elif 1 api <- 1
                
                if 1 api <- 1
                else return
                ##8
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test35(self):
        input = """
        func main() begin   
                if(1+1) api <- 1
                ##1
                
                if a api <- 1
                else continue
                ##8
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test36(self):
        input = """
            func main() begin   
                if(1+1) api <- 1
                ##1
                
                if 1 api <- 1
                else break
                ##8
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test37(self):
        input = """
            func main() begin   
                if(1+1) api <- 1
                ##1
                elif a continue
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test38(self):
        input = """
            func main() begin
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test39(self):
        input = """
            func main()
                begin
                    for i until i > 10 by i+1
                        a <- 1
                        return
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test40(self):
        input = """
            func main()
                begin
                    for i until i > 10 by i+1
                        a <- 1
                        break
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test41(self):
        input = """
            func main()
                begin
                    for i until i > 10 by i+1
                        a <- 1
                        continue
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test42(self):
        input = """
            func main()
                begin
                    for i until i >= 10 by 1 + 1
                        API <- 1
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test43(self):
        input = """
            func main()
            return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test44(self):
        input = """
            func main()
                return break
        """
        expect = "Error on line 3 col 23: break"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test45(self):
        input = """
            func main()
                return true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test46(self):
        input = """
            func main()
                return false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test47(self):
        input = """
            func main() return  ##1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test48(self):
        input = """
            number x <- y
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test49(self):
        input = """
            func main()
                begin
                    if i <= 1 return false
                end ##1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test50(self):
        input = """
            func main()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test51(self):
        input = """
            func main()
                return 
            var a <- []
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test52(self):
        input = """
            func a()
                number a[1+1]
        """
        expect = "Error on line 3 col 26: +"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test53(self):
        input = """
            var a[1] <- 1+1
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 253))
    def test54(self):
        input = """
            number a <- c()[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test55(self):
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test56(self):
        input = """
            string a <- "string"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test57(self):
        input = """
            bool a <- true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test58(self):
        input = """
            bool a <- false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test59(self):
        input = """
            bool a <- 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test60(self):
        input = """
            bool a <- "string"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test61(self):
        input = """
            func a()
                begin
                    c()[1+1] <- 1
                end
        """
        expect = "Error on line 4 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 261))
    def test62(self):
        input = """
            func a()
                begin
                    number a[1] <- c()[1+1]
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test63(self):
        input = """
            number x <- x
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test64(self):
        input = """
            string x <- 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test65(self):
        input = """
            func main()
                begin
                var i<- 0
                    for i until i >= 10 by 1
                        writeNumbe(i)
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test66(self):
        input = """
            func main()
                begin
                    number r
                    number s
                    r <- 2.0
                    number a[5]
                    number b[5]
                    s <- r * r * 3.14
                    a[0] <- s
                    end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test67(self):
        input = """return
        """
        expect = "Error on line 1 col 0: return"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test68(self):
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
                begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
                end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test69(self):
        input = """
            func isPrime(number x)
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test70(self):
        input = """
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) writeString("Yes")
                    else writeString("No")
                end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test71(self):
        input = """
            func isPrime(number x)
                begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin
                if (x % i = 0) return false
                end
                return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test72(self):
        input = """
        func main()
            number s <- r * r * 3.14
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test73(self):
        input = """
            func main()
                number aPI <- 3.14
                number l[3] <- value * aPi
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test74(self):
        input = """
        
            func foo(number a[5], string b)
                begin
                var i <- 0
                for i until i >= 5 by 1
                begin
                a[i] <- i * i + 5
                end
                return -1
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test75(self):
        input = """
            func main()
                begin
                    break
                    begin
                        continue
                        begin
                            return
                            begin
                            end
                        end
                    end
                end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test76(self):
        input = """
                func main()
                begin
                    begin
                        begin
                            begin
                            end
                        end
                    end
                end
             """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test77(self):
        input = """
            func main()
                begin 
                    return ([1,2,3]) + 1
                    return main()
                    main(1,2)
                    fun()
                    main([1,2,3], 1+2, a, c ... e)
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test78(self):
        input = """
            func main()
                begin 
                    return ([1,2,3]) + 1
                    return main()
                    main(1,2)
                    fun()[1,2,3]
                    main([1,2,3], 1+2, a, c ... e)
                end
        """
        expect = "Error on line 7 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 278))
    def test79(self):
        input = """
            func main()
                return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test80(self):
        input = """
            func main()
                return a()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test81(self):
        input = """
            func areDivisors(number num1, number num2)
                return (num1 % num2 = 0 ... num2 % num1 = 0)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test82(self):
        input = """
            func main()
                begin
                ##123zssxc
                    var num1 <- readNumber()##213213
                    var num2 <- readNumber()
                    ##21312
                    if areDivisors(num1, num2) printString("Yes")##22222
                    else printString("No")
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test83(self):
        input = """
            func main()
                begin
                    for i until i >= 10 by 1 + 1
                end
        """
        expect = "Error on line 5 col 16: end"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test84(self):
        input = """
            func main()
                begin 
                    break
                    continue
                    for i until i >= 10 by 1 + 1
                        begin
                            break
                            continue
                        end
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test85(self):
        input = """
            func main()
            ##11
                begin 
                    break
                    ##22
                    continue
                    ##33
                    for i until i >= 10 by 1 + 1
                        begin
                            break
                            continue
                        end
                        ##99
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test86(self):
        input = """
            func main()
            begin
                aPI[2]<- 3.14
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test87(self):
        input = """
            func main()
            begin
                (aPI[2])<- 3.14
            end
        """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 287))
    def test88(self):
        input = """
            var a <- b()[]
        """
        expect = "Error on line 2 col 25: ]"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test89(self):
        input = """
            var a <- b()()
        """
        expect = "Error on line 2 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 289))
    def test90(self):
        input = """
            var a <- b()[a ... 33]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test91(self):
        input = """
            var a <- b()[a ...33] > 55 +3
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test92(self):
        input = """
            var a <- b()[a ...33] > 55 +  not not not  -3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test93(self):
        input = """
            var a <- b()[a ...33] + 55 /  not not not  - 3 <= 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test94(self):
        input = """
            func main( number a <- 3 )
        """
        expect = "Error on line 2 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test95(self):
        input = """
            func main() 
                begin
                    a = 3 a < "string"
                end
        """
        expect = "Error on line 4 col 26: a"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test96(self):
        input = """
            func main() 
                begin
                    a = 3 <- "string"
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test97(self):
        input = """ 
            func main() 
            begin
                foo()
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test98(self):
        input = """
            var a <- - not not not 3
             """
        expect = "Error on line 2 col 23: not"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test99(self):
        input = """
            number a <- true > false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test100(self):
        input = """ 
            string a <- 1 >=3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))