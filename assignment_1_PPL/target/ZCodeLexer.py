# Generated from main/bkool/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u018f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\7,\u0115\n,\f,\16")
        buf.write(",\u0118\13,\3-\3-\3-\3-\3-\3-\7-\u0120\n-\f-\16-\u0123")
        buf.write("\13-\3-\3-\3-\3.\3.\3/\3/\5/\u012c\n/\3/\6/\u012f\n/\r")
        buf.write("/\16/\u0130\3\60\6\60\u0134\n\60\r\60\16\60\u0135\3\60")
        buf.write("\5\60\u0139\n\60\3\60\7\60\u013c\n\60\f\60\16\60\u013f")
        buf.write("\13\60\5\60\u0141\n\60\3\60\5\60\u0144\n\60\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u014c\n\62\f\62\16\62\u014f")
        buf.write("\13\62\3\62\3\62\3\63\6\63\u0154\n\63\r\63\16\63\u0155")
        buf.write("\3\63\3\63\3\64\3\64\3\64\7\64\u015d\n\64\f\64\16\64\u0160")
        buf.write("\13\64\5\64\u0162\n\64\3\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\7\66\u016d\n\66\f\66\16\66\u0170\13\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\5\66\u0178\n\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u0182\n\67\f\67\16")
        buf.write("\67\u0185\13\67\3\67\3\67\3\67\3\67\3\67\5\67\u018c\n")
        buf.write("\67\3\67\3\67\2\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_/a\60c\61e\62g\63")
        buf.write("i\64k\65m\66\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\6\2\f\f")
        buf.write("\17\17$$^^\t\2))^^ddhhppttvv\3\2\62;\4\2GGgg\4\2--//\3")
        buf.write("\2\f\f\4\2\f\f\17\17\5\2\n\13\16\17\"\"\3\2\63;\4\2\17")
        buf.write("\17^^\b\2^^ddhhppttvv\3\2$$\2\u01a6\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\3o\3\2\2\2\5t\3\2\2\2\7z\3\2\2\2\t\u0081\3\2\2\2\13\u0086")
        buf.write("\3\2\2\2\r\u008d\3\2\2\2\17\u0094\3\2\2\2\21\u0098\3\2")
        buf.write("\2\2\23\u00a0\3\2\2\2\25\u00a5\3\2\2\2\27\u00a9\3\2\2")
        buf.write("\2\31\u00af\3\2\2\2\33\u00b2\3\2\2\2\35\u00b8\3\2\2\2")
        buf.write("\37\u00c1\3\2\2\2!\u00c4\3\2\2\2#\u00c9\3\2\2\2%\u00ce")
        buf.write("\3\2\2\2\'\u00d4\3\2\2\2)\u00d8\3\2\2\2+\u00dc\3\2\2\2")
        buf.write("-\u00e0\3\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2\2\63\u00e7")
        buf.write("\3\2\2\2\65\u00e9\3\2\2\2\67\u00eb\3\2\2\29\u00ed\3\2")
        buf.write("\2\2;\u00ef\3\2\2\2=\u00f2\3\2\2\2?\u00f5\3\2\2\2A\u00f7")
        buf.write("\3\2\2\2C\u00fa\3\2\2\2E\u00fc\3\2\2\2G\u00ff\3\2\2\2")
        buf.write("I\u0102\3\2\2\2K\u0106\3\2\2\2M\u0108\3\2\2\2O\u010a\3")
        buf.write("\2\2\2Q\u010c\3\2\2\2S\u010e\3\2\2\2U\u0110\3\2\2\2W\u0112")
        buf.write("\3\2\2\2Y\u0119\3\2\2\2[\u0127\3\2\2\2]\u0129\3\2\2\2")
        buf.write("_\u0133\3\2\2\2a\u0145\3\2\2\2c\u0147\3\2\2\2e\u0153\3")
        buf.write("\2\2\2g\u0161\3\2\2\2i\u0163\3\2\2\2k\u0166\3\2\2\2m\u017b")
        buf.write("\3\2\2\2op\7v\2\2pq\7t\2\2qr\7w\2\2rs\7g\2\2s\4\3\2\2")
        buf.write("\2tu\7h\2\2uv\7c\2\2vw\7n\2\2wx\7u\2\2xy\7g\2\2y\6\3\2")
        buf.write("\2\2z{\7p\2\2{|\7w\2\2|}\7o\2\2}~\7d\2\2~\177\7g\2\2\177")
        buf.write("\u0080\7t\2\2\u0080\b\3\2\2\2\u0081\u0082\7d\2\2\u0082")
        buf.write("\u0083\7q\2\2\u0083\u0084\7q\2\2\u0084\u0085\7n\2\2\u0085")
        buf.write("\n\3\2\2\2\u0086\u0087\7u\2\2\u0087\u0088\7v\2\2\u0088")
        buf.write("\u0089\7t\2\2\u0089\u008a\7k\2\2\u008a\u008b\7p\2\2\u008b")
        buf.write("\u008c\7i\2\2\u008c\f\3\2\2\2\u008d\u008e\7t\2\2\u008e")
        buf.write("\u008f\7g\2\2\u008f\u0090\7v\2\2\u0090\u0091\7w\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\u0093\7p\2\2\u0093\16\3\2\2\2\u0094")
        buf.write("\u0095\7x\2\2\u0095\u0096\7c\2\2\u0096\u0097\7t\2\2\u0097")
        buf.write("\20\3\2\2\2\u0098\u0099\7f\2\2\u0099\u009a\7{\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7c\2\2\u009c\u009d\7o\2\2\u009d")
        buf.write("\u009e\7k\2\2\u009e\u009f\7e\2\2\u009f\22\3\2\2\2\u00a0")
        buf.write("\u00a1\7h\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7e\2\2\u00a4\24\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6")
        buf.write("\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\26\3\2\2\2\u00a9")
        buf.write("\u00aa\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7v\2\2\u00ac")
        buf.write("\u00ad\7k\2\2\u00ad\u00ae\7n\2\2\u00ae\30\3\2\2\2\u00af")
        buf.write("\u00b0\7d\2\2\u00b0\u00b1\7{\2\2\u00b1\32\3\2\2\2\u00b2")
        buf.write("\u00b3\7d\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7g\2\2\u00b5")
        buf.write("\u00b6\7c\2\2\u00b6\u00b7\7m\2\2\u00b7\34\3\2\2\2\u00b8")
        buf.write("\u00b9\7e\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be")
        buf.write("\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0\36\3\2\2\2\u00c1")
        buf.write("\u00c2\7k\2\2\u00c2\u00c3\7h\2\2\u00c3 \3\2\2\2\u00c4")
        buf.write("\u00c5\7g\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7u\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\"\3\2\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\u00cb\7n\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7h\2\2\u00cd")
        buf.write("$\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write("\u00d1\7i\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3")
        buf.write("&\3\2\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7p\2\2\u00d6")
        buf.write("\u00d7\7f\2\2\u00d7(\3\2\2\2\u00d8\u00d9\7p\2\2\u00d9")
        buf.write("\u00da\7q\2\2\u00da\u00db\7v\2\2\u00db*\3\2\2\2\u00dc")
        buf.write("\u00dd\7c\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df")
        buf.write(",\3\2\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7t\2\2\u00e2")
        buf.write(".\3\2\2\2\u00e3\u00e4\7-\2\2\u00e4\60\3\2\2\2\u00e5\u00e6")
        buf.write("\7/\2\2\u00e6\62\3\2\2\2\u00e7\u00e8\7,\2\2\u00e8\64\3")
        buf.write("\2\2\2\u00e9\u00ea\7\61\2\2\u00ea\66\3\2\2\2\u00eb\u00ec")
        buf.write("\7\'\2\2\u00ec8\3\2\2\2\u00ed\u00ee\7?\2\2\u00ee:\3\2")
        buf.write("\2\2\u00ef\u00f0\7>\2\2\u00f0\u00f1\7/\2\2\u00f1<\3\2")
        buf.write("\2\2\u00f2\u00f3\7#\2\2\u00f3\u00f4\7?\2\2\u00f4>\3\2")
        buf.write("\2\2\u00f5\u00f6\7>\2\2\u00f6@\3\2\2\2\u00f7\u00f8\7>")
        buf.write("\2\2\u00f8\u00f9\7?\2\2\u00f9B\3\2\2\2\u00fa\u00fb\7@")
        buf.write("\2\2\u00fbD\3\2\2\2\u00fc\u00fd\7@\2\2\u00fd\u00fe\7?")
        buf.write("\2\2\u00feF\3\2\2\2\u00ff\u0100\7?\2\2\u0100\u0101\7?")
        buf.write("\2\2\u0101H\3\2\2\2\u0102\u0103\7\60\2\2\u0103\u0104\7")
        buf.write("\60\2\2\u0104\u0105\7\60\2\2\u0105J\3\2\2\2\u0106\u0107")
        buf.write("\7*\2\2\u0107L\3\2\2\2\u0108\u0109\7+\2\2\u0109N\3\2\2")
        buf.write("\2\u010a\u010b\7]\2\2\u010bP\3\2\2\2\u010c\u010d\7_\2")
        buf.write("\2\u010dR\3\2\2\2\u010e\u010f\7.\2\2\u010fT\3\2\2\2\u0110")
        buf.write("\u0111\7<\2\2\u0111V\3\2\2\2\u0112\u0116\t\2\2\2\u0113")
        buf.write("\u0115\t\3\2\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2\2\2")
        buf.write("\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117X\3\2\2")
        buf.write("\2\u0118\u0116\3\2\2\2\u0119\u0121\7$\2\2\u011a\u0120")
        buf.write("\n\4\2\2\u011b\u011c\7^\2\2\u011c\u0120\t\5\2\2\u011d")
        buf.write("\u011e\7)\2\2\u011e\u0120\7$\2\2\u011f\u011a\3\2\2\2\u011f")
        buf.write("\u011b\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0123\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3")
        buf.write("\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125\7$\2\2\u0125\u0126")
        buf.write("\b-\2\2\u0126Z\3\2\2\2\u0127\u0128\t\6\2\2\u0128\\\3\2")
        buf.write("\2\2\u0129\u012b\t\7\2\2\u012a\u012c\t\b\2\2\u012b\u012a")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d")
        buf.write("\u012f\t\6\2\2\u012e\u012d\3\2\2\2\u012f\u0130\3\2\2\2")
        buf.write("\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131^\3\2\2")
        buf.write("\2\u0132\u0134\5[.\2\u0133\u0132\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0140")
        buf.write("\3\2\2\2\u0137\u0139\7\60\2\2\u0138\u0137\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139\u013d\3\2\2\2\u013a\u013c\t\6\2\2")
        buf.write("\u013b\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013d\u013e\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0138\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0143\3\2\2\2\u0142\u0144\5]/\2\u0143\u0142\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144`\3\2\2\2\u0145\u0146\t\t\2\2\u0146")
        buf.write("b\3\2\2\2\u0147\u0148\7%\2\2\u0148\u0149\7%\2\2\u0149")
        buf.write("\u014d\3\2\2\2\u014a\u014c\n\n\2\2\u014b\u014a\3\2\2\2")
        buf.write("\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3")
        buf.write("\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151")
        buf.write("\b\62\3\2\u0151d\3\2\2\2\u0152\u0154\t\13\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0153\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\b\63\3")
        buf.write("\2\u0158f\3\2\2\2\u0159\u0162\7\62\2\2\u015a\u015e\t\f")
        buf.write("\2\2\u015b\u015d\t\6\2\2\u015c\u015b\3\2\2\2\u015d\u0160")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0159\3\2\2\2")
        buf.write("\u0161\u015a\3\2\2\2\u0162h\3\2\2\2\u0163\u0164\13\2\2")
        buf.write("\2\u0164\u0165\b\65\4\2\u0165j\3\2\2\2\u0166\u016e\7$")
        buf.write("\2\2\u0167\u016d\n\4\2\2\u0168\u0169\7^\2\2\u0169\u016d")
        buf.write("\t\5\2\2\u016a\u016b\7)\2\2\u016b\u016d\7$\2\2\u016c\u0167")
        buf.write("\3\2\2\2\u016c\u0168\3\2\2\2\u016c\u016a\3\2\2\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0177\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172\7")
        buf.write("\17\2\2\u0172\u0178\7\f\2\2\u0173\u0178\7\f\2\2\u0174")
        buf.write("\u0175\7G\2\2\u0175\u0176\7Q\2\2\u0176\u0178\7H\2\2\u0177")
        buf.write("\u0171\3\2\2\2\u0177\u0173\3\2\2\2\u0177\u0174\3\2\2\2")
        buf.write("\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\b")
        buf.write("\66\5\2\u017al\3\2\2\2\u017b\u0183\7$\2\2\u017c\u0182")
        buf.write("\n\4\2\2\u017d\u017e\7^\2\2\u017e\u0182\t\5\2\2\u017f")
        buf.write("\u0180\7)\2\2\u0180\u0182\7$\2\2\u0181\u017c\3\2\2\2\u0181")
        buf.write("\u017d\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u018b\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0186\u018c\t\r\2\2\u0187\u0188")
        buf.write("\7^\2\2\u0188\u018c\n\16\2\2\u0189\u018a\7)\2\2\u018a")
        buf.write("\u018c\n\17\2\2\u018b\u0186\3\2\2\2\u018b\u0187\3\2\2")
        buf.write("\2\u018b\u0189\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\b\67\6\2\u018en\3\2\2\2\27\2\u0116\u011f\u0121\u012b")
        buf.write("\u0130\u0135\u0138\u013d\u0140\u0143\u014d\u0155\u015e")
        buf.write("\u0161\u016c\u016e\u0177\u0181\u0183\u018b\7\3-\2\b\2")
        buf.write("\2\3\65\3\3\66\4\3\67\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    MINUS = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    ARROW = 29
    DIFF = 30
    LESS = 31
    LE = 32
    GREATER = 33
    GE = 34
    EE = 35
    CONCAT = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    CM = 41
    CL = 42
    IDENTIFIER = 43
    STRING_LIT = 44
    NUMBER_LIT = 45
    NEWLINE = 46
    COMMENTS = 47
    WS = 48
    INT = 49
    ERROR_CHAR = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52

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
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "MINUS", "MUL", "DIV", "MOD", "EQUAL", "ARROW", "DIFF", "LESS", 
            "LE", "GREATER", "GE", "EE", "CONCAT", "LB", "RB", "LP", "RP", 
            "CM", "CL", "IDENTIFIER", "STRING_LIT", "NUMBER_LIT", "NEWLINE", 
            "COMMENTS", "WS", "INT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
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
            actions[43] = self.STRING_LIT_action 
            actions[51] = self.ERROR_CHAR_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
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

                if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


