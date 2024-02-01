import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 101))


    def test0(self):
        input = "123"
        expected = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 102))
        

    def test1(self):
        input = "#123"
        expected = "Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 103))
        

    def test2(self):
        input = "@123"
        expected = "Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 104))
        

    def test3(self):
        input = "e1?23"
        expected = "e1,Error Token ?"
        self.assertTrue(TestLexer.test(input, expected, 105))
        

    def test4(self):
        input = ".123"
        expected = "Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 106))
        

    def test5(self):
        input = "#123"
        expected = "Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 107))
        


    def test6(self):
        input = "x=3 #"
        expected = "x,=,3,Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 108))
        

    def test7(self):
        input = "print @"
        expected = "print,Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 109))
        
    
    
    def test8(self):
        input = """ "He asked me: \'"Where is John?\'"" """
        expected = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 110))
        

    def test9(self):
        input = "@"
        expected = "Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 111))
        

    def test10(self):
        input = "@@#$%"
        expected = "Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 112))
        

    def test11(self):
        input = "@123"
        expected = "Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 113))
        

    def test12(self):
        input = "ILVUMW"
        expected = "ILVUMW,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 114))
        

    def test13(self):
        input = "am2310l"
        expected = "am2310l,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 115))
        

    def test14(self):
        input = "qe123-49"
        expected = "qe123,-,49,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 116))
        

    def test15(self):
        input = "ILVUMW"
        expected = "ILVUMW,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 117))
        

    def test16(self):
        input = ".12e90"
        expected = "Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 118))
        

    def test17(self):
        input = "4.3"
        expected = "4.3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 119))
        

    def test18(self):
        input = """print \"Hello, World!"""
        expected =  "print,Unclosed String: Hello, World!"
        self.assertTrue(TestLexer.test(input, expected, 120))
        

    def test19(self):
        input = """ Hello \q World! """
        expected = "Hello,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 121))
        

    def test20(self):
        input = """He asked me: \"Where is John?"""
        expected = "He,asked,me,:,Unclosed String: Where is John?"
        self.assertTrue(TestLexer.test(input, expected, 122))
        

    def test21(self):
        input = "1234567"
        expected = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 123))
        

    def test22(self):
        input = "ILVUMW"
        expected = "ILVUMW,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 124))
        

    def test23(self):
        input = "1234.567"
        expected = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 125))
        

    def test24(self):
        input = "abc\t"
        expected = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 126))
        

    def test25(self):
        input = "q asd"
        expected = "q,asd,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 127))
        

    def test26(self):
        input = "\""
        expected = "Error Token \""
        self.assertTrue(TestLexer.test(input, expected, 128))
           
    def test27(self):
        input = "qwes_231"
        expected = "qwes_231,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 129))
        
    def test28(self):
        input = "\"Unclose_string"
        expected = "Unclosed String: Unclose_string"
        self.assertTrue(TestLexer.test(input, expected, 130))
        
    def test29(self):
        input = """\\"dkjoiues"""
        expected = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 131))
        
    def test30(self):
        input = "\\asdsad}*)/ff"
        expected = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 132))
        
    def test31(self):
        input = "/123a<>?;"
        expected = "/,123,a,<,>,Error Token ?"
        self.assertTrue(TestLexer.test(input, expected, 133))
        
    def test32(self):
        input = "_123asews"
        expected = "_123asews,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 134))
        
    def test33(self):
        input = "12.1e-03"
        expected = "12.1e-03,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 135))
        
    def test34(self):
        input = "3"
        expected = "3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 136))
        
    def test35(self):
        input = "This is a \t string containing tab"
        expected = "This,is,a,string,containing,tab,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 137))
        
    def test36(self):
        input = " 0.33E-3"
        expected = "0.33E-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 138))
        
    def test39(self):
        input = "390021389324"
        expected = "390021389324,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 139))
        
    def test40(self):
        input = """ print "Hello, \n World!" """
        expected = "print,Unclosed String: Hello, "
        self.assertTrue(TestLexer.test(input, expected, 140))
        
    def test41(self):
        input = "Hello, \q World!"
        expected = "Hello,,,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 141))
        
    def test42(self):
        input = """ print \"Hello, \n\" + \"World! \q """
        expected = "print,Unclosed String: Hello, "
        self.assertTrue(TestLexer.test(input, expected, 142))
        
    def test43(self):
        input = "x=abc3=45"
        expected = "x,=,abc3,=,45,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 143))
        
    def test44(self):
        input = "scammer dinh nhat moi thoi dai"
        expected = "scammer,dinh,nhat,moi,thoi,dai,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 144))
        
    def test45(self):
        input = "#whysoez ggnoob "
        expected = "Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 145))
        
    def test46(self):
        input = "IP 15 pro max 1TB nghe ro tra loi"
        expected = "IP,15,pro,max,1,TB,nghe,ro,tra,loi,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 146))
        
    def test47(self):
        input = "?dau la day"
        expected = "Error Token ?"
        self.assertTrue(TestLexer.test(input, expected, 147))
        
    def test48(self):
        input = "$ai la toi"
        expected = "Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 148))
        
    def test49(self):
        input = "x:= 3 # 4 + 5 "
        expected = "x,:,=,3,Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 149))
        
    def test50(self):
        input = ",./;'p[213]!@#@!$"
        expected = ",,Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 150))
        
    def test51(self):
        input = "[]();:\"/.,.#$%!"
        expected = "[,],(,),Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 151))
        
    def test52(self):
        input = "int i=1; if (i>=3) print i; else print 0;"
        expected = "int,i,=,1,Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 152))
        
    def test53(self):
        input = """String a="Vinh dep trai"; print a;"""
        expected = "String,a,=,Vinh dep trai,Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 153))
        
    def test54(self):
        input = "String a=\"Vinh dep trai; print a;"
        expected = "String,a,=,Unclosed String: Vinh dep trai; print a;"
        self.assertTrue(TestLexer.test(input, expected, 154))
        
    def test55(self):
        input = "return 5/4;"
        expected = "return,5,/,4,Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 155))
        
    def test56(self):
        input = "_abcsh"
        expected = "_abcsh,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 156))
        
    def test57(self):
        input = "@LOVEF"
        expected = "Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 157))
        
    def test58(self):
        input = "Error Token #"
        expected = "Error,Token,Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 158))
        
    def test59(self):
        input = "\"aAsVN\r\r\n\tgge"
        expected = "Illegal Escape In String: aAsVN\n"
        self.assertTrue(TestLexer.test(input, expected, 159))
        
    def test60(self):
        input = "\"aA\tqq\\a\rd\n\fsVNgge\""
        expected = "Illegal Escape In String: aA\tqq\\a"
        self.assertTrue(TestLexer.test(input, expected, 160))
        
    def test61(self):
        input = "ABVCajw kll +-*/"
        expected = "ABVCajw,kll,+,-,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 161))
        
    def test62(self):
        input = "ABC123abmas"
        expected = "ABC123abmas,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 162))
        
    def test63(self):
        input = " x > 5"
        expected = "x,>,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 163))
        
    def test64(self):
        input = "x:=5"
        expected = "x,:,=,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 164))
        
    def test65(self):
        input = "\f"
        expected = "Error Token \f"
        self.assertTrue(TestLexer.test(input, expected, 165))
        
    def test66(self):
        input = "\t"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 166))
        
    def test67(self):
        input = "\b"
        expected = "Error Token \b"
        self.assertTrue(TestLexer.test(input, expected, 167))
        
    def test68(self):
        input = "This is a string with an illegal escape: \g."
        expected = "This,is,a,string,with,an,illegal,escape,:,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 168))
        
    def test69(self):
        input = """var x = "This is a string with a\t horizontal tab"""
        expected = "var,x,=,Unclosed String: This is a string with a\t horizontal tab"
        self.assertTrue(TestLexer.test(input, expected, 169))
        
    def test70(self):
        input = """This is a \"quoted\" string"""
        expected = "This,is,a,quoted,string,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 170))
        
    def test71(self):
        input = "9.0"
        expected = "9.0,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 171))
        
    def test72(self):
        input = " 12e8"
        expected = "12e8,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 172))
        
    def test73(self):
        input = "1."
        expected = "1.,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 173))
        
    def test74(self):
        input = "Hello, \\x World!"
        expected = "Hello,,,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 174))
        
    def test75(self):
        input = "Hello, \\ World!"
        expected = "Hello,,,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 175))
        
    def test76(self):
        input = "128e+42"
        expected = "128e+42,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 176))
        
    def test77(self):
        input = "143e"
        expected = "143,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 177))
        
    def test78(self):
        input = "392701782931"
        expected = "392701782931,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 178))
        
    def test79(self):
        input = "\""
        expected = "Error Token \""
        self.assertTrue(TestLexer.test(input, expected, 179))
        
    def test80(self):
        input = "[1,3,54,2,34,]"
        expected = "[,1,,,3,,,54,,,2,,,34,,,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 180))
        
    def test81(self):
        input = """ "Hello,\"+\"World!"""
        expected = "Hello,,+,Unclosed String: World!"
        self.assertTrue(TestLexer.test(input, expected, 181))
        
    def test82(self):
        input = "print @#$%"
        expected = "print,Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 182))
        
    def test83(self):
        input = """ \"Hello, World!\""""
        expected = "Hello, World!,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 183))
        
    def test84(self):
        input = """ "[Hello \n World!] " """
        expected = "Unclosed String: [Hello "
        self.assertTrue(TestLexer.test(input, expected, 184))
        
    def test85(self):
        input = """print "Hello, + World!"""
        expected = "print,Unclosed String: Hello, + World!"
        self.assertTrue(TestLexer.test(input, expected, 185))
        
    def test86(self):
        input = """print "Hello, \ World!" """
        expected = "print,Illegal Escape In String: Hello, \\ "
        self.assertTrue(TestLexer.test(input, expected, 186))
        
    def test87(self):
        input = "?"
        expected = "Error Token ?"
        self.assertTrue(TestLexer.test(input, expected, 187))
        
    def test88(self):
        input = "(1,3)"
        expected = "(,1,,,3,),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 188))
        
    def test89(self):
        input = "[0-9][a-zA-Z]"
        expected = "[,0,-,9,],[,a,-,zA,-,Z,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 189))
        
    def test90(self):
        input = "This is a string containing tab \t"
        expected = "This,is,a,string,containing,tab,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 190))
        
    def test91(self):
        input = "A string literal has a type of string."
        expected = "A,string,literal,has,a,type,of,string,Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 191))
        
    def test92(self):
        input = "[1, 2, 3]"
        expected = "[,1,,,2,,,3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 192))
        
    def test93(self):
        input = "a[3+x.foo(2)] := a[b[2]] +3;"
        expected = "a,[,3,+,x,Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 193))
        
    def test94(self):
        input = "@readInt"
        expected = "Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 194))
        
    def test95(self):
        input = "var r, s: tnt;"
        expected = "var,r,,,s,:,tnt,Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 195))
        
    def test96(self):
        input = "Shape.@getNumOfShape();"
        expected = "Shape,Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 196))
        
    def test97(self):
        input = ",./;']!@#$%^&^*()"
        expected = ",,Error Token ."
        self.assertTrue(TestLexer.test(input, expected, 197))
        
    def test98(self):
        input = """"he said to me that \n"""
        expected = "Unclosed String: he said to me that "
        self.assertTrue(TestLexer.test(input, expected, 198))
        
    def test99(self):
        input = """ Unclose String: \m """
        expected = "Unclose,String,:,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 199))
        
    def test100(self):
        input = """"Illegal Escape: \n"""
        expected = "Unclosed String: Illegal Escape: "
        self.assertTrue(TestLexer.test(input, expected, 200))
        
    














