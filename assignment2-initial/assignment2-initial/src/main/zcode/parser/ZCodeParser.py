# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u01a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\7\2X\n\2\f\2\16")
        buf.write("\2[\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3d\n\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4j\n\4\3\5\3\5\3\5\5\5o\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6v\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7~\n\7\3\7\3\7")
        buf.write("\5\7\u0082\n\7\3\b\3\b\3\b\3\b\5\b\u0088\n\b\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u008e\n\t\3\n\3\n\3\n\3\n\5\n\u0094\n\n\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u009a\n\13\3\13\3\13\5\13\u009e\n")
        buf.write("\13\3\13\3\13\5\13\u00a2\n\13\3\13\3\13\5\13\u00a6\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00ad\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00b5\n\r\3\16\3\16\3\16\3\16\5\16\u00bb\n\16")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c4\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00cb\n\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u00d3\n\22\f\22\16\22\u00d6\13\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00de\n\23\f\23\16")
        buf.write("\23\u00e1\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00e9")
        buf.write("\n\24\f\24\16\24\u00ec\13\24\3\25\3\25\3\25\5\25\u00f1")
        buf.write("\n\25\3\26\3\26\3\26\5\26\u00f6\n\26\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u00fc\n\27\3\27\5\27\u00ff\n\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0106\n\27\3\30\3\30\3\30\5\30\u010b\n")
        buf.write("\30\3\30\3\30\3\30\5\30\u0110\n\30\3\30\3\30\5\30\u0114")
        buf.write("\n\30\3\31\3\31\5\31\u0118\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u011f\n\31\5\31\u0121\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0128\n\32\3\33\3\33\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0130\n\33\3\34\3\34\5\34\u0134\n\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0141\n")
        buf.write("\35\3\36\3\36\3\36\3\37\3\37\5\37\u0148\n\37\3\37\3\37")
        buf.write("\5\37\u014c\n\37\3\37\3\37\3\37\3\37\3 \3 \3 \5 \u0155")
        buf.write("\n \3 \3 \5 \u0159\n \3 \5 \u015c\n \3!\3!\3!\5!\u0161")
        buf.write("\n!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0169\n\"\3#\3#\5#\u016d")
        buf.write("\n#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u0178\n$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\5\'\u0184\n\'\3\'\3\'\3(\3(\3(\5")
        buf.write("(\u018b\n(\3(\3(\3(\3)\3)\5)\u0192\n)\3)\5)\u0195\n)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\5*\u019e\n*\3+\6+\u01a1\n+\r+\16+")
        buf.write("\u01a2\3+\2\5\"$&,\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\b\3\2/\60\3")
        buf.write("\2\6\b\4\2\37\37!&\3\2\30\31\3\2\32\33\3\2\34\36\2\u01bc")
        buf.write("\2Y\3\2\2\2\4c\3\2\2\2\6i\3\2\2\2\bn\3\2\2\2\np\3\2\2")
        buf.write("\2\fw\3\2\2\2\16\u0087\3\2\2\2\20\u008d\3\2\2\2\22\u008f")
        buf.write("\3\2\2\2\24\u0095\3\2\2\2\26\u00ac\3\2\2\2\30\u00ae\3")
        buf.write("\2\2\2\32\u00ba\3\2\2\2\34\u00bc\3\2\2\2\36\u00c3\3\2")
        buf.write("\2\2 \u00ca\3\2\2\2\"\u00cc\3\2\2\2$\u00d7\3\2\2\2&\u00e2")
        buf.write("\3\2\2\2(\u00f0\3\2\2\2*\u00f5\3\2\2\2,\u0105\3\2\2\2")
        buf.write(".\u0113\3\2\2\2\60\u0120\3\2\2\2\62\u0127\3\2\2\2\64\u012f")
        buf.write("\3\2\2\2\66\u0131\3\2\2\28\u0140\3\2\2\2:\u0142\3\2\2")
        buf.write("\2<\u0145\3\2\2\2>\u0151\3\2\2\2@\u015d\3\2\2\2B\u0168")
        buf.write("\3\2\2\2D\u016a\3\2\2\2F\u0170\3\2\2\2H\u017b\3\2\2\2")
        buf.write("J\u017e\3\2\2\2L\u0181\3\2\2\2N\u0187\3\2\2\2P\u018f\3")
        buf.write("\2\2\2R\u019d\3\2\2\2T\u01a0\3\2\2\2VX\7\61\2\2WV\3\2")
        buf.write("\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2")
        buf.write("\2\\]\5\4\3\2]^\7\2\2\3^\3\3\2\2\2_`\5\6\4\2`a\5\4\3\2")
        buf.write("ad\3\2\2\2bd\5\6\4\2c_\3\2\2\2cb\3\2\2\2d\5\3\2\2\2ej")
        buf.write("\5\24\13\2fg\5\b\5\2gh\5T+\2hj\3\2\2\2ie\3\2\2\2if\3\2")
        buf.write("\2\2j\7\3\2\2\2ko\5\n\6\2lo\5\f\7\2mo\5\22\n\2nk\3\2\2")
        buf.write("\2nl\3\2\2\2nm\3\2\2\2o\t\3\2\2\2pq\7\n\2\2qr\7.\2\2r")
        buf.write("u\7 \2\2sv\5\34\17\2tv\5\66\34\2us\3\2\2\2ut\3\2\2\2v")
        buf.write("\13\3\2\2\2wx\7\3\2\2x}\7.\2\2yz\7*\2\2z{\5\16\b\2{|\7")
        buf.write("+\2\2|~\3\2\2\2}y\3\2\2\2}~\3\2\2\2~\u0081\3\2\2\2\177")
        buf.write("\u0080\7 \2\2\u0080\u0082\5\34\17\2\u0081\177\3\2\2\2")
        buf.write("\u0081\u0082\3\2\2\2\u0082\r\3\2\2\2\u0083\u0084\7\60")
        buf.write("\2\2\u0084\u0085\7,\2\2\u0085\u0088\5\16\b\2\u0086\u0088")
        buf.write("\7\60\2\2\u0087\u0083\3\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\17\3\2\2\2\u0089\u008a\t\2\2\2\u008a\u008b\7,\2\2\u008b")
        buf.write("\u008e\5\16\b\2\u008c\u008e\t\2\2\2\u008d\u0089\3\2\2")
        buf.write("\2\u008d\u008c\3\2\2\2\u008e\21\3\2\2\2\u008f\u0090\7")
        buf.write("\13\2\2\u0090\u0093\7.\2\2\u0091\u0092\7 \2\2\u0092\u0094")
        buf.write("\5\34\17\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\23\3\2\2\2\u0095\u0096\7\f\2\2\u0096\u0097\7.\2\2\u0097")
        buf.write("\u0099\7(\2\2\u0098\u009a\5\26\f\2\u0099\u0098\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a5\7")
        buf.write(")\2\2\u009c\u009e\5T+\2\u009d\u009c\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a6\5L\'\2\u00a0")
        buf.write("\u00a2\5T+\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a6\5P)\2\u00a4\u00a6\5T+\2\u00a5")
        buf.write("\u009d\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a4\3\2\2\2")
        buf.write("\u00a6\25\3\2\2\2\u00a7\u00a8\5\30\r\2\u00a8\u00a9\7,")
        buf.write("\2\2\u00a9\u00aa\5\26\f\2\u00aa\u00ad\3\2\2\2\u00ab\u00ad")
        buf.write("\5\30\r\2\u00ac\u00a7\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\27\3\2\2\2\u00ae\u00af\t\3\2\2\u00af\u00b4\7.\2\2\u00b0")
        buf.write("\u00b1\7*\2\2\u00b1\u00b2\5\16\b\2\u00b2\u00b3\7+\2\2")
        buf.write("\u00b3\u00b5\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b4\u00b5\3")
        buf.write("\2\2\2\u00b5\31\3\2\2\2\u00b6\u00b7\5\34\17\2\u00b7\u00b8")
        buf.write("\5\32\16\2\u00b8\u00bb\3\2\2\2\u00b9\u00bb\5\34\17\2\u00ba")
        buf.write("\u00b6\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\33\3\2\2\2\u00bc")
        buf.write("\u00bd\5\36\20\2\u00bd\35\3\2\2\2\u00be\u00bf\5 \21\2")
        buf.write("\u00bf\u00c0\7\'\2\2\u00c0\u00c1\5 \21\2\u00c1\u00c4\3")
        buf.write("\2\2\2\u00c2\u00c4\5 \21\2\u00c3\u00be\3\2\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4\37\3\2\2\2\u00c5\u00c6\5\"\22\2\u00c6\u00c7")
        buf.write("\t\4\2\2\u00c7\u00c8\5\"\22\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00cb\5\"\22\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb!\3\2\2\2\u00cc\u00cd\b\22\1\2\u00cd\u00ce\5$")
        buf.write("\23\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\f\4\2\2\u00d0\u00d1")
        buf.write("\t\5\2\2\u00d1\u00d3\5$\23\2\u00d2\u00cf\3\2\2\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5#\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\b\23\1")
        buf.write("\2\u00d8\u00d9\5&\24\2\u00d9\u00df\3\2\2\2\u00da\u00db")
        buf.write("\f\4\2\2\u00db\u00dc\t\6\2\2\u00dc\u00de\5&\24\2\u00dd")
        buf.write("\u00da\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e0%\3\2\2\2\u00e1\u00df\3\2\2")
        buf.write("\2\u00e2\u00e3\b\24\1\2\u00e3\u00e4\5(\25\2\u00e4\u00ea")
        buf.write("\3\2\2\2\u00e5\u00e6\f\4\2\2\u00e6\u00e7\t\7\2\2\u00e7")
        buf.write("\u00e9\5(\25\2\u00e8\u00e5\3\2\2\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\'\3\2\2")
        buf.write("\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\7\27\2\2\u00ee\u00f1")
        buf.write("\5(\25\2\u00ef\u00f1\5*\26\2\u00f0\u00ed\3\2\2\2\u00f0")
        buf.write("\u00ef\3\2\2\2\u00f1)\3\2\2\2\u00f2\u00f3\7\33\2\2\u00f3")
        buf.write("\u00f6\5*\26\2\u00f4\u00f6\5,\27\2\u00f5\u00f2\3\2\2\2")
        buf.write("\u00f5\u00f4\3\2\2\2\u00f6+\3\2\2\2\u00f7\u00ff\7.\2\2")
        buf.write("\u00f8\u00f9\7.\2\2\u00f9\u00fb\7(\2\2\u00fa\u00fc\5\60")
        buf.write("\31\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00ff\7)\2\2\u00fe\u00f7\3\2\2\2\u00fe")
        buf.write("\u00f8\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\7*\2\2")
        buf.write("\u0101\u0102\5\62\32\2\u0102\u0103\7+\2\2\u0103\u0106")
        buf.write("\3\2\2\2\u0104\u0106\5.\30\2\u0105\u00fe\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106-\3\2\2\2\u0107\u0108\7.\2\2\u0108")
        buf.write("\u010a\7(\2\2\u0109\u010b\5\60\31\2\u010a\u0109\3\2\2")
        buf.write("\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0114")
        buf.write("\7)\2\2\u010d\u010f\7(\2\2\u010e\u0110\5\60\31\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0114\7)\2\2\u0112\u0114\5\64\33\2\u0113\u0107")
        buf.write("\3\2\2\2\u0113\u010d\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("/\3\2\2\2\u0115\u0118\5\66\34\2\u0116\u0118\5\62\32\2")
        buf.write("\u0117\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118\u0119\3")
        buf.write("\2\2\2\u0119\u011a\7,\2\2\u011a\u011b\5\60\31\2\u011b")
        buf.write("\u0121\3\2\2\2\u011c\u011f\5\66\34\2\u011d\u011f\5\62")
        buf.write("\32\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f\u0121")
        buf.write("\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u011e\3\2\2\2\u0121")
        buf.write("\61\3\2\2\2\u0122\u0123\5\34\17\2\u0123\u0124\7,\2\2\u0124")
        buf.write("\u0125\5\62\32\2\u0125\u0128\3\2\2\2\u0126\u0128\5\34")
        buf.write("\17\2\u0127\u0122\3\2\2\2\u0127\u0126\3\2\2\2\u0128\63")
        buf.write("\3\2\2\2\u0129\u0130\7\60\2\2\u012a\u0130\7/\2\2\u012b")
        buf.write("\u0130\7\4\2\2\u012c\u0130\7\5\2\2\u012d\u0130\5\66\34")
        buf.write("\2\u012e\u0130\7.\2\2\u012f\u0129\3\2\2\2\u012f\u012a")
        buf.write("\3\2\2\2\u012f\u012b\3\2\2\2\u012f\u012c\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130\65\3\2\2\2\u0131")
        buf.write("\u0133\7*\2\2\u0132\u0134\5\62\32\2\u0133\u0132\3\2\2")
        buf.write("\2\u0133\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136")
        buf.write("\7+\2\2\u0136\67\3\2\2\2\u0137\u0141\5:\36\2\u0138\u0141")
        buf.write("\5<\37\2\u0139\u0141\5> \2\u013a\u0141\5F$\2\u013b\u0141")
        buf.write("\5H%\2\u013c\u0141\5J&\2\u013d\u0141\5L\'\2\u013e\u0141")
        buf.write("\5N(\2\u013f\u0141\5P)\2\u0140\u0137\3\2\2\2\u0140\u0138")
        buf.write("\3\2\2\2\u0140\u0139\3\2\2\2\u0140\u013a\3\2\2\2\u0140")
        buf.write("\u013b\3\2\2\2\u0140\u013c\3\2\2\2\u0140\u013d\3\2\2\2")
        buf.write("\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u01419\3\2\2")
        buf.write("\2\u0142\u0143\5\b\5\2\u0143\u0144\5T+\2\u0144;\3\2\2")
        buf.write("\2\u0145\u0147\7.\2\2\u0146\u0148\5\66\34\2\u0147\u0146")
        buf.write("\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014b\3\2\2\2\u0149")
        buf.write("\u014a\7\37\2\2\u014a\u014c\7\60\2\2\u014b\u0149\3\2\2")
        buf.write("\2\u014b\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e")
        buf.write("\7 \2\2\u014e\u014f\5\34\17\2\u014f\u0150\5T+\2\u0150")
        buf.write("=\3\2\2\2\u0151\u0152\7\22\2\2\u0152\u0154\5\34\17\2\u0153")
        buf.write("\u0155\5T+\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0158\58\35\2\u0157\u0159\5B\"\2")
        buf.write("\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3")
        buf.write("\2\2\2\u015a\u015c\5D#\2\u015b\u015a\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c?\3\2\2\2\u015d\u015e\7\24\2\2\u015e\u0160")
        buf.write("\5\34\17\2\u015f\u0161\5T+\2\u0160\u015f\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\58\35\2")
        buf.write("\u0163A\3\2\2\2\u0164\u0165\5@!\2\u0165\u0166\5B\"\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0169\5@!\2\u0168\u0164\3\2\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169C\3\2\2\2\u016a\u016c\7\23\2\2\u016b")
        buf.write("\u016d\5T+\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u016f\58\35\2\u016fE\3\2\2\2\u0170")
        buf.write("\u0171\7\r\2\2\u0171\u0172\7.\2\2\u0172\u0173\7\16\2\2")
        buf.write("\u0173\u0174\5\34\17\2\u0174\u0175\7\17\2\2\u0175\u0177")
        buf.write("\5\34\17\2\u0176\u0178\5T+\2\u0177\u0176\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\58\35\2")
        buf.write("\u017aG\3\2\2\2\u017b\u017c\7\20\2\2\u017c\u017d\5T+\2")
        buf.write("\u017dI\3\2\2\2\u017e\u017f\7\21\2\2\u017f\u0180\5T+\2")
        buf.write("\u0180K\3\2\2\2\u0181\u0183\7\t\2\2\u0182\u0184\5\34\17")
        buf.write("\2\u0183\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185\u0186\5T+\2\u0186M\3\2\2\2\u0187\u0188")
        buf.write("\7.\2\2\u0188\u018a\7(\2\2\u0189\u018b\5\60\31\2\u018a")
        buf.write("\u0189\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018d\7)\2\2\u018d\u018e\5T+\2\u018eO\3\2\2\2\u018f")
        buf.write("\u0191\7\25\2\2\u0190\u0192\5T+\2\u0191\u0190\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0195\5")
        buf.write("R*\2\u0194\u0193\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u0197\7\26\2\2\u0197\u0198\5T+\2\u0198")
        buf.write("Q\3\2\2\2\u0199\u019a\58\35\2\u019a\u019b\5R*\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019e\58\35\2\u019d\u0199\3\2\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019eS\3\2\2\2\u019f\u01a1\7\61\2")
        buf.write("\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3U\3\2\2\2\66Ycinu}\u0081")
        buf.write("\u0087\u008d\u0093\u0099\u009d\u00a1\u00a5\u00ac\u00b4")
        buf.write("\u00ba\u00c3\u00ca\u00d4\u00df\u00ea\u00f0\u00f5\u00fb")
        buf.write("\u00fe\u0105\u010a\u010f\u0113\u0117\u011e\u0120\u0127")
        buf.write("\u012f\u0133\u0140\u0147\u014b\u0154\u0158\u015b\u0160")
        buf.write("\u0168\u016c\u0177\u0183\u018a\u0191\u0194\u019d\u01a2")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "TRUE", "FALSE", "NUMBER", "BOOL", 
                      "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
                      "MINUS", "MUL", "DIV", "MOD", "EQUAL", "ARROW", "DIFF", 
                      "LESS", "LE", "GREATER", "GE", "EE", "CONCAT", "LB", 
                      "RB", "LP", "RP", "CM", "CL", "IDENTIFIER", "STRING_LIT", 
                      "NUMBER_LIT", "NEWLINE", "COMMENTS", "WS", "INT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_keyword_var = 5
    RULE_list_number = 6
    RULE_number_string = 7
    RULE_implicit_dynamic = 8
    RULE_function = 9
    RULE_prameters_list = 10
    RULE_pram = 11
    RULE_exp_prime = 12
    RULE_expression = 13
    RULE_expression0 = 14
    RULE_expression1 = 15
    RULE_expression2 = 16
    RULE_expression3 = 17
    RULE_expression4 = 18
    RULE_expression5 = 19
    RULE_expression6 = 20
    RULE_expression7 = 21
    RULE_expression8 = 22
    RULE_list_array = 23
    RULE_list_expression = 24
    RULE_literal = 25
    RULE_array_literal = 26
    RULE_statement = 27
    RULE_declaration_statement = 28
    RULE_assignment_statement = 29
    RULE_if_statement = 30
    RULE_elif_statement = 31
    RULE_elif_loop = 32
    RULE_else_statement = 33
    RULE_for_statement = 34
    RULE_break_statement = 35
    RULE_continue_statement = 36
    RULE_return_statement = 37
    RULE_call_statement = 38
    RULE_block_statement = 39
    RULE_list_statement = 40
    RULE_ignore = 41

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "keyword_var", "list_number", "number_string", 
                   "implicit_dynamic", "function", "prameters_list", "pram", 
                   "exp_prime", "expression", "expression0", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "list_array", 
                   "list_expression", "literal", "array_literal", "statement", 
                   "declaration_statement", "assignment_statement", "if_statement", 
                   "elif_statement", "elif_loop", "else_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "block_statement", "list_statement", 
                   "ignore" ]

    EOF = Token.EOF
    TYPE=1
    TRUE=2
    FALSE=3
    NUMBER=4
    BOOL=5
    STRING=6
    RETURN=7
    VAR=8
    DYNAMIC=9
    FUNC=10
    FOR=11
    UNTIL=12
    BY=13
    BREAK=14
    CONTINUE=15
    IF=16
    ELSE=17
    ELIF=18
    BEGIN=19
    END=20
    NOT=21
    AND=22
    OR=23
    ADD=24
    MINUS=25
    MUL=26
    DIV=27
    MOD=28
    EQUAL=29
    ARROW=30
    DIFF=31
    LESS=32
    LE=33
    GREATER=34
    GE=35
    EE=36
    CONCAT=37
    LB=38
    RB=39
    LP=40
    RP=41
    CM=42
    CL=43
    IDENTIFIER=44
    STRING_LIT=45
    NUMBER_LIT=46
    NEWLINE=47
    COMMENTS=48
    WS=49
    INT=50
    ERROR_CHAR=51
    UNCLOSE_STRING=52
    ILLEGAL_ESCAPE=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 84
                self.match(ZCodeParser.NEWLINE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.list_declared()
            self.state = 91
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.declared()
                self.state = 94
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.function()
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.variables()
                self.state = 101
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.implicit_var()
                pass
            elif token in [ZCodeParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ZCodeParser.VAR)
            self.state = 111
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 112
            self.match(ZCodeParser.ARROW)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 113
                self.expression()
                pass

            elif la_ == 2:
                self.state = 114
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def list_number(self):
            return self.getTypedRuleContext(ZCodeParser.List_numberContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ZCodeParser.TYPE)
            self.state = 118
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 119
                self.match(ZCodeParser.LP)
                self.state = 120
                self.list_number()
                self.state = 121
                self.match(ZCodeParser.RP)


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 125
                self.match(ZCodeParser.ARROW)
                self.state = 126
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def list_number(self):
            return self.getTypedRuleContext(ZCodeParser.List_numberContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_number" ):
                return visitor.visitList_number(self)
            else:
                return visitor.visitChildren(self)




    def list_number(self):

        localctx = ZCodeParser.List_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_number)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 130
                self.match(ZCodeParser.CM)
                self.state = 131
                self.list_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def list_number(self):
            return self.getTypedRuleContext(ZCodeParser.List_numberContext,0)


        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_number_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_string" ):
                return visitor.visitNumber_string(self)
            else:
                return visitor.visitChildren(self)




    def number_string(self):

        localctx = ZCodeParser.Number_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_number_string)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.STRING_LIT or _la==ZCodeParser.NUMBER_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.match(ZCodeParser.CM)
                self.state = 137
                self.list_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.STRING_LIT or _la==ZCodeParser.NUMBER_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.DYNAMIC)
            self.state = 142
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 143
                self.match(ZCodeParser.ARROW)
                self.state = 144
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ZCodeParser.FUNC)
            self.state = 148
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 149
            self.match(ZCodeParser.LB)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 150
                self.prameters_list()


            self.state = 153
            self.match(ZCodeParser.RB)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 154
                    self.ignore()


                self.state = 157
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 158
                    self.ignore()


                self.state = 161
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 162
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pram(self):
            return self.getTypedRuleContext(ZCodeParser.PramContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prameters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrameters_list" ):
                return visitor.visitPrameters_list(self)
            else:
                return visitor.visitChildren(self)




    def prameters_list(self):

        localctx = ZCodeParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_prameters_list)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.pram()
                self.state = 166
                self.match(ZCodeParser.CM)
                self.state = 167
                self.prameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.pram()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def list_number(self):
            return self.getTypedRuleContext(ZCodeParser.List_numberContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_pram

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPram" ):
                return visitor.visitPram(self)
            else:
                return visitor.visitChildren(self)




    def pram(self):

        localctx = ZCodeParser.PramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 174
                self.match(ZCodeParser.LP)
                self.state = 175
                self.list_number()
                self.state = 176
                self.match(ZCodeParser.RP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def exp_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_prime" ):
                return visitor.visitExp_prime(self)
            else:
                return visitor.visitChildren(self)




    def exp_prime(self):

        localctx = ZCodeParser.Exp_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_prime)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.expression()
                self.state = 181
                self.exp_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression0(self):
            return self.getTypedRuleContext(ZCodeParser.Expression0Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.expression0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression0" ):
                return visitor.visitExpression0(self)
            else:
                return visitor.visitChildren(self)




    def expression0(self):

        localctx = ZCodeParser.Expression0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression0)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.expression1()
                self.state = 189
                self.match(ZCodeParser.CONCAT)
                self.state = 190
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def EE(self):
            return self.getToken(ZCodeParser.EE, 0)

        def DIFF(self):
            return self.getToken(ZCodeParser.DIFF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.expression2(0)
                self.state = 196
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.DIFF) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.EE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.expression3(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.expression4(0) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 229
                    self.expression5() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression5)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.NOT)
                self.state = 236
                self.expression5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression6)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(ZCodeParser.MINUS)
                self.state = 241
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def list_array(self):
            return self.getTypedRuleContext(ZCodeParser.List_arrayContext,0)


        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 245
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 246
                    self.match(ZCodeParser.IDENTIFIER)

                    self.state = 247
                    self.match(ZCodeParser.LB)
                    self.state = 249
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                        self.state = 248
                        self.list_array()


                    self.state = 251
                    self.match(ZCodeParser.RB)
                    pass


                self.state = 254
                self.match(ZCodeParser.LP)
                self.state = 255
                self.list_expression()
                self.state = 256
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.expression8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def list_array(self):
            return self.getTypedRuleContext(ZCodeParser.List_arrayContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = ZCodeParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expression8)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(ZCodeParser.IDENTIFIER)

                self.state = 262
                self.match(ZCodeParser.LB)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                    self.state = 263
                    self.list_array()


                self.state = 266
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(ZCodeParser.LB)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                    self.state = 268
                    self.list_array()


                self.state = 271
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def list_array(self):
            return self.getTypedRuleContext(ZCodeParser.List_arrayContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array" ):
                return visitor.visitList_array(self)
            else:
                return visitor.visitChildren(self)




    def list_array(self):

        localctx = ZCodeParser.List_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_list_array)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 275
                    self.array_literal()
                    pass

                elif la_ == 2:
                    self.state = 276
                    self.list_expression()
                    pass


                self.state = 279
                self.match(ZCodeParser.CM)
                self.state = 280
                self.list_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.array_literal()
                    pass

                elif la_ == 2:
                    self.state = 283
                    self.list_expression()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = ZCodeParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_expression)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.expression()
                self.state = 289
                self.match(ZCodeParser.CM)
                self.state = 290
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 299
                self.array_literal()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 300
                self.match(ZCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.LP)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 304
                self.list_expression()


            self.state = 307
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 314
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 315
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 316
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 317
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.variables()
            self.state = 321
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 324
                self.array_literal()


            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.EQUAL:
                self.state = 327
                self.match(ZCodeParser.EQUAL)
                self.state = 328
                self.match(ZCodeParser.NUMBER_LIT)


            self.state = 331
            self.match(ZCodeParser.ARROW)
            self.state = 332
            self.expression()
            self.state = 333
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def elif_loop(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_loopContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(ZCodeParser.IF)
            self.state = 336
            self.expression()
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 337
                self.ignore()


            self.state = 340
            self.statement()
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 341
                self.elif_loop()


            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 344
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.ELIF)
            self.state = 348
            self.expression()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 349
                self.ignore()


            self.state = 352
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elif_loop(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_loopContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_loop" ):
                return visitor.visitElif_loop(self)
            else:
                return visitor.visitChildren(self)




    def elif_loop(self):

        localctx = ZCodeParser.Elif_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elif_loop)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.elif_statement()
                self.state = 355
                self.elif_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.elif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ZCodeParser.ELSE)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 361
                self.ignore()


            self.state = 364
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.FOR)
            self.state = 367
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 368
            self.match(ZCodeParser.UNTIL)
            self.state = 369
            self.expression()
            self.state = 370
            self.match(ZCodeParser.BY)
            self.state = 371
            self.expression()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 372
                self.ignore()


            self.state = 375
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(ZCodeParser.BREAK)
            self.state = 378
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZCodeParser.CONTINUE)
            self.state = 381
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(ZCodeParser.RETURN)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 384
                self.expression()


            self.state = 387
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def list_array(self):
            return self.getTypedRuleContext(ZCodeParser.List_arrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 390
            self.match(ZCodeParser.LB)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 391
                self.list_array()


            self.state = 394
            self.match(ZCodeParser.RB)
            self.state = 395
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def list_statement(self):
            return self.getTypedRuleContext(ZCodeParser.List_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.BEGIN)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 398
                self.ignore()


            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 401
                self.list_statement()


            self.state = 404
            self.match(ZCodeParser.END)
            self.state = 405
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(ZCodeParser.List_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = ZCodeParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_list_statement)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.statement()
                self.state = 408
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 413
                self.match(ZCodeParser.NEWLINE)
                self.state = 416 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression2_sempred
        self._predicates[17] = self.expression3_sempred
        self._predicates[18] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




