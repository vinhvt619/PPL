# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u0197\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\5\2u\n\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\7-\u011c\n-\f-\16-\u011f\13-\3.\3.\3.\3.\3")
        buf.write(".\3.\7.\u0127\n.\f.\16.\u012a\13.\3.\3.\3.\3/\3/\3\60")
        buf.write("\3\60\5\60\u0133\n\60\3\60\6\60\u0136\n\60\r\60\16\60")
        buf.write("\u0137\3\61\6\61\u013b\n\61\r\61\16\61\u013c\3\61\5\61")
        buf.write("\u0140\n\61\3\61\7\61\u0143\n\61\f\61\16\61\u0146\13\61")
        buf.write("\5\61\u0148\n\61\3\61\5\61\u014b\n\61\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u0153\n\63\f\63\16\63\u0156\13\63\3")
        buf.write("\63\3\63\3\64\6\64\u015b\n\64\r\64\16\64\u015c\3\64\3")
        buf.write("\64\3\65\3\65\3\65\7\65\u0164\n\65\f\65\16\65\u0167\13")
        buf.write("\65\5\65\u0169\n\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u0174\n\67\f\67\16\67\u0177\13\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\5\67\u017f\n\67\3\67\3\67\3")
        buf.write("8\38\38\38\38\38\38\78\u018a\n8\f8\168\u018d\138\38\3")
        buf.write("8\38\38\38\58\u0194\n8\38\38\2\29\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\60")
        buf.write("c\61e\62g\63i\64k\65m\66o\67\3\2\21\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\7\2\f\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\3\2\f\f\4\2\f\f\16\17\5\2\13\13\17\17")
        buf.write("\"\"\3\2\63;\3\2))\3\2$$\4\2\16\17^^\b\2^^ddhhppttvv\2")
        buf.write("\u01b0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3t\3\2\2\2\5v\3\2\2")
        buf.write("\2\7{\3\2\2\2\t\u0081\3\2\2\2\13\u0088\3\2\2\2\r\u008d")
        buf.write("\3\2\2\2\17\u0094\3\2\2\2\21\u009b\3\2\2\2\23\u009f\3")
        buf.write("\2\2\2\25\u00a7\3\2\2\2\27\u00ac\3\2\2\2\31\u00b0\3\2")
        buf.write("\2\2\33\u00b6\3\2\2\2\35\u00b9\3\2\2\2\37\u00bf\3\2\2")
        buf.write("\2!\u00c8\3\2\2\2#\u00cb\3\2\2\2%\u00d0\3\2\2\2\'\u00d5")
        buf.write("\3\2\2\2)\u00db\3\2\2\2+\u00df\3\2\2\2-\u00e3\3\2\2\2")
        buf.write("/\u00e7\3\2\2\2\61\u00ea\3\2\2\2\63\u00ec\3\2\2\2\65\u00ee")
        buf.write("\3\2\2\2\67\u00f0\3\2\2\29\u00f2\3\2\2\2;\u00f4\3\2\2")
        buf.write("\2=\u00f6\3\2\2\2?\u00f9\3\2\2\2A\u00fc\3\2\2\2C\u00fe")
        buf.write("\3\2\2\2E\u0101\3\2\2\2G\u0103\3\2\2\2I\u0106\3\2\2\2")
        buf.write("K\u0109\3\2\2\2M\u010d\3\2\2\2O\u010f\3\2\2\2Q\u0111\3")
        buf.write("\2\2\2S\u0113\3\2\2\2U\u0115\3\2\2\2W\u0117\3\2\2\2Y\u0119")
        buf.write("\3\2\2\2[\u0120\3\2\2\2]\u012e\3\2\2\2_\u0130\3\2\2\2")
        buf.write("a\u013a\3\2\2\2c\u014c\3\2\2\2e\u014e\3\2\2\2g\u015a\3")
        buf.write("\2\2\2i\u0168\3\2\2\2k\u016a\3\2\2\2m\u016d\3\2\2\2o\u0182")
        buf.write("\3\2\2\2qu\5\13\6\2ru\5\r\7\2su\5\t\5\2tq\3\2\2\2tr\3")
        buf.write("\2\2\2ts\3\2\2\2u\4\3\2\2\2vw\7v\2\2wx\7t\2\2xy\7w\2\2")
        buf.write("yz\7g\2\2z\6\3\2\2\2{|\7h\2\2|}\7c\2\2}~\7n\2\2~\177\7")
        buf.write("u\2\2\177\u0080\7g\2\2\u0080\b\3\2\2\2\u0081\u0082\7p")
        buf.write("\2\2\u0082\u0083\7w\2\2\u0083\u0084\7o\2\2\u0084\u0085")
        buf.write("\7d\2\2\u0085\u0086\7g\2\2\u0086\u0087\7t\2\2\u0087\n")
        buf.write("\3\2\2\2\u0088\u0089\7d\2\2\u0089\u008a\7q\2\2\u008a\u008b")
        buf.write("\7q\2\2\u008b\u008c\7n\2\2\u008c\f\3\2\2\2\u008d\u008e")
        buf.write("\7u\2\2\u008e\u008f\7v\2\2\u008f\u0090\7t\2\2\u0090\u0091")
        buf.write("\7k\2\2\u0091\u0092\7p\2\2\u0092\u0093\7i\2\2\u0093\16")
        buf.write("\3\2\2\2\u0094\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7v\2\2\u0097\u0098\7w\2\2\u0098\u0099\7t\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\20\3\2\2\2\u009b\u009c\7x\2\2\u009c\u009d")
        buf.write("\7c\2\2\u009d\u009e\7t\2\2\u009e\22\3\2\2\2\u009f\u00a0")
        buf.write("\7f\2\2\u00a0\u00a1\7{\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3")
        buf.write("\7c\2\2\u00a3\u00a4\7o\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6")
        buf.write("\7e\2\2\u00a6\24\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7e\2\2\u00ab\26")
        buf.write("\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\30\3\2\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7n\2\2\u00b5\32\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7{\2\2\u00b8\34\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7m\2\2\u00be\36\3\2\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1")
        buf.write("\7q\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4")
        buf.write("\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7 \3\2\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7h\2\2\u00ca\"\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7g\2\2\u00cf$\3")
        buf.write("\2\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7h\2\2\u00d4&\3\2\2\2\u00d5\u00d6")
        buf.write("\7d\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7i\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7p\2\2\u00da(\3\2\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7f\2\2\u00de*\3")
        buf.write("\2\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2,\3\2\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\u00e6\7f\2\2\u00e6.\3\2\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7t\2\2\u00e9\60\3\2\2\2\u00ea\u00eb")
        buf.write("\7-\2\2\u00eb\62\3\2\2\2\u00ec\u00ed\7/\2\2\u00ed\64\3")
        buf.write("\2\2\2\u00ee\u00ef\7,\2\2\u00ef\66\3\2\2\2\u00f0\u00f1")
        buf.write("\7\61\2\2\u00f18\3\2\2\2\u00f2\u00f3\7\'\2\2\u00f3:\3")
        buf.write("\2\2\2\u00f4\u00f5\7?\2\2\u00f5<\3\2\2\2\u00f6\u00f7\7")
        buf.write(">\2\2\u00f7\u00f8\7/\2\2\u00f8>\3\2\2\2\u00f9\u00fa\7")
        buf.write("#\2\2\u00fa\u00fb\7?\2\2\u00fb@\3\2\2\2\u00fc\u00fd\7")
        buf.write(">\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7>\2\2\u00ff\u0100\7")
        buf.write("?\2\2\u0100D\3\2\2\2\u0101\u0102\7@\2\2\u0102F\3\2\2\2")
        buf.write("\u0103\u0104\7@\2\2\u0104\u0105\7?\2\2\u0105H\3\2\2\2")
        buf.write("\u0106\u0107\7?\2\2\u0107\u0108\7?\2\2\u0108J\3\2\2\2")
        buf.write("\u0109\u010a\7\60\2\2\u010a\u010b\7\60\2\2\u010b\u010c")
        buf.write("\7\60\2\2\u010cL\3\2\2\2\u010d\u010e\7*\2\2\u010eN\3\2")
        buf.write("\2\2\u010f\u0110\7+\2\2\u0110P\3\2\2\2\u0111\u0112\7]")
        buf.write("\2\2\u0112R\3\2\2\2\u0113\u0114\7_\2\2\u0114T\3\2\2\2")
        buf.write("\u0115\u0116\7.\2\2\u0116V\3\2\2\2\u0117\u0118\7<\2\2")
        buf.write("\u0118X\3\2\2\2\u0119\u011d\t\2\2\2\u011a\u011c\t\3\2")
        buf.write("\2\u011b\u011a\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011eZ\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u0120\u0128\7$\2\2\u0121\u0127\n\4\2\2\u0122")
        buf.write("\u0123\7^\2\2\u0123\u0127\t\5\2\2\u0124\u0125\7)\2\2\u0125")
        buf.write("\u0127\7$\2\2\u0126\u0121\3\2\2\2\u0126\u0122\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012b\u012c\7$\2\2\u012c\u012d\b.\2\2\u012d\\")
        buf.write("\3\2\2\2\u012e\u012f\t\6\2\2\u012f^\3\2\2\2\u0130\u0132")
        buf.write("\t\7\2\2\u0131\u0133\t\b\2\2\u0132\u0131\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0136\t\6\2\2")
        buf.write("\u0135\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0135\3")
        buf.write("\2\2\2\u0137\u0138\3\2\2\2\u0138`\3\2\2\2\u0139\u013b")
        buf.write("\5]/\2\u013a\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u0147\3\2\2\2\u013e")
        buf.write("\u0140\7\60\2\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2")
        buf.write("\2\u0140\u0144\3\2\2\2\u0141\u0143\t\6\2\2\u0142\u0141")
        buf.write("\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0147\u013f\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014a\3")
        buf.write("\2\2\2\u0149\u014b\5_\60\2\u014a\u0149\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014bb\3\2\2\2\u014c\u014d\t\t\2\2\u014dd\3\2")
        buf.write("\2\2\u014e\u014f\7%\2\2\u014f\u0150\7%\2\2\u0150\u0154")
        buf.write("\3\2\2\2\u0151\u0153\n\n\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\b")
        buf.write("\63\3\2\u0158f\3\2\2\2\u0159\u015b\t\13\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\b\64\3")
        buf.write("\2\u015fh\3\2\2\2\u0160\u0169\7\62\2\2\u0161\u0165\t\f")
        buf.write("\2\2\u0162\u0164\t\6\2\2\u0163\u0162\3\2\2\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0160\3\2\2\2")
        buf.write("\u0168\u0161\3\2\2\2\u0169j\3\2\2\2\u016a\u016b\13\2\2")
        buf.write("\2\u016b\u016c\b\66\4\2\u016cl\3\2\2\2\u016d\u0175\7$")
        buf.write("\2\2\u016e\u0174\n\4\2\2\u016f\u0170\7^\2\2\u0170\u0174")
        buf.write("\t\5\2\2\u0171\u0172\t\r\2\2\u0172\u0174\t\16\2\2\u0173")
        buf.write("\u016e\3\2\2\2\u0173\u016f\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u017e\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179")
        buf.write("\7\17\2\2\u0179\u017f\7\f\2\2\u017a\u017f\7\f\2\2\u017b")
        buf.write("\u017c\7G\2\2\u017c\u017d\7Q\2\2\u017d\u017f\7H\2\2\u017e")
        buf.write("\u0178\3\2\2\2\u017e\u017a\3\2\2\2\u017e\u017b\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\b")
        buf.write("\67\5\2\u0181n\3\2\2\2\u0182\u018b\7$\2\2\u0183\u018a")
        buf.write("\n\4\2\2\u0184\u0185\7^\2\2\u0185\u018a\t\5\2\2\u0186")
        buf.write("\u0187\7^\2\2\u0187\u0188\7)\2\2\u0188\u018a\7$\2\2\u0189")
        buf.write("\u0183\3\2\2\2\u0189\u0184\3\2\2\2\u0189\u0186\3\2\2\2")
        buf.write("\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c\u0193\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0194")
        buf.write("\t\17\2\2\u018f\u0190\7^\2\2\u0190\u0194\n\20\2\2\u0191")
        buf.write("\u0192\7)\2\2\u0192\u0194\n\16\2\2\u0193\u018e\3\2\2\2")
        buf.write("\u0193\u018f\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195\3")
        buf.write("\2\2\2\u0195\u0196\b8\6\2\u0196p\3\2\2\2\30\2t\u011d\u0126")
        buf.write("\u0128\u0132\u0137\u013c\u013f\u0144\u0147\u014a\u0154")
        buf.write("\u015c\u0165\u0168\u0173\u0175\u017e\u0189\u018b\u0193")
        buf.write("\7\3.\2\b\2\2\3\66\3\3\67\4\38\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    RETURN = 7
    VAR = 8
    DYNAMIC = 9
    FUNC = 10
    FOR = 11
    UNTIL = 12
    BY = 13
    BREAK = 14
    CONTINUE = 15
    IF = 16
    ELSE = 17
    ELIF = 18
    BEGIN = 19
    END = 20
    NOT = 21
    AND = 22
    OR = 23
    ADD = 24
    MINUS = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQUAL = 29
    ARROW = 30
    DIFF = 31
    LESS = 32
    LE = 33
    GREATER = 34
    GE = 35
    EE = 36
    CONCAT = 37
    LB = 38
    RB = 39
    LP = 40
    RP = 41
    CM = 42
    CL = 43
    IDENTIFIER = 44
    STRING_LIT = 45
    NUMBER_LIT = 46
    NEWLINE = 47
    COMMENTS = 48
    WS = 49
    INT = 50
    ERROR_CHAR = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'=='", "'...'", "'('", "')'", "'['", "']'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "MINUS", "MUL", "DIV", "MOD", "EQUAL", "ARROW", "DIFF", "LESS", 
            "LE", "GREATER", "GE", "EE", "CONCAT", "LB", "RB", "LP", "RP", 
            "CM", "CL", "IDENTIFIER", "STRING_LIT", "NUMBER_LIT", "NEWLINE", 
            "COMMENTS", "WS", "INT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TYPE", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "MINUS", "MUL", "DIV", "MOD", "EQUAL", 
                  "ARROW", "DIFF", "LESS", "LE", "GREATER", "GE", "EE", 
                  "CONCAT", "LB", "RB", "LP", "RP", "CM", "CL", "IDENTIFIER", 
                  "STRING_LIT", "DIGIT", "EXP", "NUMBER_LIT", "NEWLINE", 
                  "COMMENTS", "WS", "INT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.STRING_LIT_action 
            actions[52] = self.ERROR_CHAR_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


