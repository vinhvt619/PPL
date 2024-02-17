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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u017f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3^\n\3\3\4\3\4\3\4\3\4\5\4d\n\4\3")
        buf.write("\5\3\5\3\5\5\5i\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7v\n\7\3\7\3\7\5\7z\n\7\3\b\3\b\3\b\3\b\5")
        buf.write("\b\u0080\n\b\3\t\3\t\3\t\3\t\5\t\u0086\n\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u008e\n\13\3\13\3\13\5\13\u0092\n")
        buf.write("\13\3\13\3\13\5\13\u0096\n\13\3\13\3\13\5\13\u009a\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00a1\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00a9\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00b0")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00b7\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u00bf\n\20\f\20\16\20\u00c2")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00ca\n\21\f")
        buf.write("\21\16\21\u00cd\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00d5\n\22\f\22\16\22\u00d8\13\22\3\23\3\23\3\23\5")
        buf.write("\23\u00dd\n\23\3\24\3\24\3\24\5\24\u00e2\n\24\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00e8\n\25\3\25\5\25\u00eb\n\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00f2\n\25\3\26\3\26\3\26\5\26")
        buf.write("\u00f7\n\26\3\26\3\26\3\26\5\26\u00fc\n\26\3\26\3\26\5")
        buf.write("\26\u0100\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u0107\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u010f\n\30\3\31\3")
        buf.write("\31\5\31\u0113\n\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0120\n\32\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u012a\n\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\5\35\u0133\n\35\3\35\3\35\3\35\5")
        buf.write("\35\u0138\n\35\3\36\3\36\3\36\5\36\u013d\n\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0145\n\37\3 \3 \5 \u0149\n")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u0154\n!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\5$\u0160\n$\3$\3$\3%\3%\3%\5%\u0167")
        buf.write("\n%\3%\3%\3%\3&\3&\3&\5&\u016f\n&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u0178\n\'\3(\6(\u017b\n(\r(\16(\u017c\3(\2\5")
        buf.write("\36 \")\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLN\2\7\3\2\5\7\4\2\36\36 %\3\2")
        buf.write("\27\30\3\2\31\32\3\2\33\35\2\u0190\2S\3\2\2\2\4]\3\2\2")
        buf.write("\2\6c\3\2\2\2\bh\3\2\2\2\nj\3\2\2\2\fo\3\2\2\2\16\177")
        buf.write("\3\2\2\2\20\u0081\3\2\2\2\22\u0087\3\2\2\2\24\u0089\3")
        buf.write("\2\2\2\26\u00a0\3\2\2\2\30\u00a2\3\2\2\2\32\u00af\3\2")
        buf.write("\2\2\34\u00b6\3\2\2\2\36\u00b8\3\2\2\2 \u00c3\3\2\2\2")
        buf.write("\"\u00ce\3\2\2\2$\u00dc\3\2\2\2&\u00e1\3\2\2\2(\u00f1")
        buf.write("\3\2\2\2*\u00ff\3\2\2\2,\u0106\3\2\2\2.\u010e\3\2\2\2")
        buf.write("\60\u0110\3\2\2\2\62\u011f\3\2\2\2\64\u0121\3\2\2\2\66")
        buf.write("\u0124\3\2\2\28\u012f\3\2\2\2:\u0139\3\2\2\2<\u0144\3")
        buf.write("\2\2\2>\u0146\3\2\2\2@\u014c\3\2\2\2B\u0157\3\2\2\2D\u015a")
        buf.write("\3\2\2\2F\u015d\3\2\2\2H\u0163\3\2\2\2J\u016b\3\2\2\2")
        buf.write("L\u0177\3\2\2\2N\u017a\3\2\2\2PR\7\60\2\2QP\3\2\2\2RU")
        buf.write("\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\5\4")
        buf.write("\3\2WX\7\2\2\3X\3\3\2\2\2YZ\5\6\4\2Z[\5\4\3\2[^\3\2\2")
        buf.write("\2\\^\5\6\4\2]Y\3\2\2\2]\\\3\2\2\2^\5\3\2\2\2_d\5\24\13")
        buf.write("\2`a\5\b\5\2ab\5N(\2bd\3\2\2\2c_\3\2\2\2c`\3\2\2\2d\7")
        buf.write("\3\2\2\2ei\5\n\6\2fi\5\f\7\2gi\5\20\t\2he\3\2\2\2hf\3")
        buf.write("\2\2\2hg\3\2\2\2i\t\3\2\2\2jk\7\t\2\2kl\7-\2\2lm\7\37")
        buf.write("\2\2mn\5\32\16\2n\13\3\2\2\2op\5\22\n\2pu\7-\2\2qr\7)")
        buf.write("\2\2rs\5\16\b\2st\7*\2\2tv\3\2\2\2uq\3\2\2\2uv\3\2\2\2")
        buf.write("vy\3\2\2\2wx\7\37\2\2xz\5\32\16\2yw\3\2\2\2yz\3\2\2\2")
        buf.write("z\r\3\2\2\2{|\7/\2\2|}\7+\2\2}\u0080\5\16\b\2~\u0080\7")
        buf.write("/\2\2\177{\3\2\2\2\177~\3\2\2\2\u0080\17\3\2\2\2\u0081")
        buf.write("\u0082\7\n\2\2\u0082\u0085\7-\2\2\u0083\u0084\7\37\2\2")
        buf.write("\u0084\u0086\5\32\16\2\u0085\u0083\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\21\3\2\2\2\u0087\u0088\t\2\2\2\u0088\23")
        buf.write("\3\2\2\2\u0089\u008a\7\13\2\2\u008a\u008b\7-\2\2\u008b")
        buf.write("\u008d\7\'\2\2\u008c\u008e\5\26\f\2\u008d\u008c\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0099")
        buf.write("\7(\2\2\u0090\u0092\5N(\2\u0091\u0090\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u009a\5F$\2\u0094\u0096")
        buf.write("\5N(\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u009a\5J&\2\u0098\u009a\5N(\2\u0099\u0091")
        buf.write("\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\25\3\2\2\2\u009b\u009c\5\30\r\2\u009c\u009d\7+\2\2\u009d")
        buf.write("\u009e\5\26\f\2\u009e\u00a1\3\2\2\2\u009f\u00a1\5\30\r")
        buf.write("\2\u00a0\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\27\3")
        buf.write("\2\2\2\u00a2\u00a3\5\22\n\2\u00a3\u00a8\7-\2\2\u00a4\u00a5")
        buf.write("\7)\2\2\u00a5\u00a6\5\16\b\2\u00a6\u00a7\7*\2\2\u00a7")
        buf.write("\u00a9\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\31\3\2\2\2\u00aa\u00ab\5\34\17\2\u00ab\u00ac\7")
        buf.write("&\2\2\u00ac\u00ad\5\34\17\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00b0\5\34\17\2\u00af\u00aa\3\2\2\2\u00af\u00ae\3\2\2")
        buf.write("\2\u00b0\33\3\2\2\2\u00b1\u00b2\5\36\20\2\u00b2\u00b3")
        buf.write("\t\3\2\2\u00b3\u00b4\5\36\20\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b7\5\36\20\2\u00b6\u00b1\3\2\2\2\u00b6\u00b5\3\2\2")
        buf.write("\2\u00b7\35\3\2\2\2\u00b8\u00b9\b\20\1\2\u00b9\u00ba\5")
        buf.write(" \21\2\u00ba\u00c0\3\2\2\2\u00bb\u00bc\f\4\2\2\u00bc\u00bd")
        buf.write("\t\4\2\2\u00bd\u00bf\5 \21\2\u00be\u00bb\3\2\2\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\37\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\b\21")
        buf.write("\1\2\u00c4\u00c5\5\"\22\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7")
        buf.write("\f\4\2\2\u00c7\u00c8\t\5\2\2\u00c8\u00ca\5\"\22\2\u00c9")
        buf.write("\u00c6\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc!\3\2\2\2\u00cd\u00cb\3\2\2")
        buf.write("\2\u00ce\u00cf\b\22\1\2\u00cf\u00d0\5$\23\2\u00d0\u00d6")
        buf.write("\3\2\2\2\u00d1\u00d2\f\4\2\2\u00d2\u00d3\t\6\2\2\u00d3")
        buf.write("\u00d5\5$\23\2\u00d4\u00d1\3\2\2\2\u00d5\u00d8\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7#\3\2\2")
        buf.write("\2\u00d8\u00d6\3\2\2\2\u00d9\u00da\7\26\2\2\u00da\u00dd")
        buf.write("\5$\23\2\u00db\u00dd\5&\24\2\u00dc\u00d9\3\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd%\3\2\2\2\u00de\u00df\7\32\2\2\u00df")
        buf.write("\u00e2\5&\24\2\u00e0\u00e2\5(\25\2\u00e1\u00de\3\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\'\3\2\2\2\u00e3\u00eb\7-\2")
        buf.write("\2\u00e4\u00e5\7-\2\2\u00e5\u00e7\7\'\2\2\u00e6\u00e8")
        buf.write("\5,\27\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00eb\7(\2\2\u00ea\u00e3\3\2\2\2")
        buf.write("\u00ea\u00e4\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\7")
        buf.write(")\2\2\u00ed\u00ee\5,\27\2\u00ee\u00ef\7*\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00f2\5*\26\2\u00f1\u00ea\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f4\7-\2\2\u00f4")
        buf.write("\u00f6\7\'\2\2\u00f5\u00f7\5,\27\2\u00f6\u00f5\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u0100\7")
        buf.write("(\2\2\u00f9\u00fb\7\'\2\2\u00fa\u00fc\5\32\16\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u0100\7(\2\2\u00fe\u0100\5.\30\2\u00ff\u00f3\3")
        buf.write("\2\2\2\u00ff\u00f9\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100+")
        buf.write("\3\2\2\2\u0101\u0102\5\32\16\2\u0102\u0103\7+\2\2\u0103")
        buf.write("\u0104\5,\27\2\u0104\u0107\3\2\2\2\u0105\u0107\5\32\16")
        buf.write("\2\u0106\u0101\3\2\2\2\u0106\u0105\3\2\2\2\u0107-\3\2")
        buf.write("\2\2\u0108\u010f\7/\2\2\u0109\u010f\7.\2\2\u010a\u010f")
        buf.write("\7\3\2\2\u010b\u010f\7\4\2\2\u010c\u010f\5\60\31\2\u010d")
        buf.write("\u010f\7-\2\2\u010e\u0108\3\2\2\2\u010e\u0109\3\2\2\2")
        buf.write("\u010e\u010a\3\2\2\2\u010e\u010b\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010d\3\2\2\2\u010f/\3\2\2\2\u0110\u0112")
        buf.write("\7)\2\2\u0111\u0113\5,\27\2\u0112\u0111\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\7*\2\2")
        buf.write("\u0115\61\3\2\2\2\u0116\u0120\5\64\33\2\u0117\u0120\5")
        buf.write("\66\34\2\u0118\u0120\58\35\2\u0119\u0120\5@!\2\u011a\u0120")
        buf.write("\5B\"\2\u011b\u0120\5D#\2\u011c\u0120\5F$\2\u011d\u0120")
        buf.write("\5H%\2\u011e\u0120\5J&\2\u011f\u0116\3\2\2\2\u011f\u0117")
        buf.write("\3\2\2\2\u011f\u0118\3\2\2\2\u011f\u0119\3\2\2\2\u011f")
        buf.write("\u011a\3\2\2\2\u011f\u011b\3\2\2\2\u011f\u011c\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\63\3\2")
        buf.write("\2\2\u0121\u0122\5\b\5\2\u0122\u0123\5N(\2\u0123\65\3")
        buf.write("\2\2\2\u0124\u0129\7-\2\2\u0125\u0126\7)\2\2\u0126\u0127")
        buf.write("\5,\27\2\u0127\u0128\7*\2\2\u0128\u012a\3\2\2\2\u0129")
        buf.write("\u0125\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\7\37\2\2\u012c\u012d\5\32\16\2\u012d\u012e")
        buf.write("\5N(\2\u012e\67\3\2\2\2\u012f\u0130\7\21\2\2\u0130\u0132")
        buf.write("\5\32\16\2\u0131\u0133\5N(\2\u0132\u0131\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\5\62\32")
        buf.write("\2\u0135\u0137\5<\37\2\u0136\u0138\5> \2\u0137\u0136\3")
        buf.write("\2\2\2\u0137\u0138\3\2\2\2\u01389\3\2\2\2\u0139\u013a")
        buf.write("\7\23\2\2\u013a\u013c\5\32\16\2\u013b\u013d\5N(\2\u013c")
        buf.write("\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u013f\5\62\32\2\u013f;\3\2\2\2\u0140\u0141\5:\36")
        buf.write("\2\u0141\u0142\5<\37\2\u0142\u0145\3\2\2\2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u0140\3\2\2\2\u0144\u0143\3\2\2\2\u0145")
        buf.write("=\3\2\2\2\u0146\u0148\7\22\2\2\u0147\u0149\5N(\2\u0148")
        buf.write("\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014b\5\62\32\2\u014b?\3\2\2\2\u014c\u014d\7\f")
        buf.write("\2\2\u014d\u014e\7-\2\2\u014e\u014f\7\r\2\2\u014f\u0150")
        buf.write("\5\32\16\2\u0150\u0151\7\16\2\2\u0151\u0153\5\32\16\2")
        buf.write("\u0152\u0154\5N(\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2")
        buf.write("\2\2\u0154\u0155\3\2\2\2\u0155\u0156\5\62\32\2\u0156A")
        buf.write("\3\2\2\2\u0157\u0158\7\17\2\2\u0158\u0159\5N(\2\u0159")
        buf.write("C\3\2\2\2\u015a\u015b\7\20\2\2\u015b\u015c\5N(\2\u015c")
        buf.write("E\3\2\2\2\u015d\u015f\7\b\2\2\u015e\u0160\5\32\16\2\u015f")
        buf.write("\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u0162\5N(\2\u0162G\3\2\2\2\u0163\u0164\7-\2\2\u0164")
        buf.write("\u0166\7\'\2\2\u0165\u0167\5,\27\2\u0166\u0165\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\7")
        buf.write("(\2\2\u0169\u016a\5N(\2\u016aI\3\2\2\2\u016b\u016c\7\24")
        buf.write("\2\2\u016c\u016e\5N(\2\u016d\u016f\5L\'\2\u016e\u016d")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\7\25\2\2\u0171\u0172\5N(\2\u0172K\3\2\2\2\u0173")
        buf.write("\u0174\5\62\32\2\u0174\u0175\5L\'\2\u0175\u0178\3\2\2")
        buf.write("\2\u0176\u0178\5\62\32\2\u0177\u0173\3\2\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178M\3\2\2\2\u0179\u017b\7\60\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017dO\3\2\2\2-S]chuy\177\u0085\u008d\u0091")
        buf.write("\u0095\u0099\u00a0\u00a8\u00af\u00b6\u00c0\u00cb\u00d6")
        buf.write("\u00dc\u00e1\u00e7\u00ea\u00f1\u00f6\u00fb\u00ff\u0106")
        buf.write("\u010e\u0112\u011f\u0129\u0132\u0137\u013c\u0144\u0148")
        buf.write("\u0153\u015f\u0166\u016e\u0177\u017c")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "MINUS", "MUL", 
                      "DIV", "MOD", "EQUAL", "ARROW", "DIFF", "LESS", "LE", 
                      "GREATER", "GE", "EE", "CONCAT", "LB", "RB", "LP", 
                      "RP", "CM", "CL", "IDENTIFIER", "STRING_LIT", "NUMBER_LIT", 
                      "NEWLINE", "COMMENTS", "WS", "INT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_keyword_var = 5
    RULE_list_number = 6
    RULE_implicit_dynamic = 7
    RULE_type1 = 8
    RULE_function = 9
    RULE_prameters_list = 10
    RULE_pram = 11
    RULE_expression = 12
    RULE_expression1 = 13
    RULE_expression2 = 14
    RULE_expression3 = 15
    RULE_expression4 = 16
    RULE_expression5 = 17
    RULE_expression6 = 18
    RULE_expression7 = 19
    RULE_expression8 = 20
    RULE_list_expression = 21
    RULE_literal = 22
    RULE_array_literal = 23
    RULE_statement = 24
    RULE_declaration_statement = 25
    RULE_assignment_statement = 26
    RULE_if_statement = 27
    RULE_elif_statement = 28
    RULE_elif_loop = 29
    RULE_else_statement = 30
    RULE_for_statement = 31
    RULE_break_statement = 32
    RULE_continue_statement = 33
    RULE_return_statement = 34
    RULE_call_statement = 35
    RULE_block_statement = 36
    RULE_list_statement = 37
    RULE_ignore = 38

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "keyword_var", "list_number", "implicit_dynamic", 
                   "type1", "function", "prameters_list", "pram", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "list_expression", "literal", "array_literal", "statement", 
                   "declaration_statement", "assignment_statement", "if_statement", 
                   "elif_statement", "elif_loop", "else_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "block_statement", "list_statement", 
                   "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    MINUS=24
    MUL=25
    DIV=26
    MOD=27
    EQUAL=28
    ARROW=29
    DIFF=30
    LESS=31
    LE=32
    GREATER=33
    GE=34
    EE=35
    CONCAT=36
    LB=37
    RB=38
    LP=39
    RP=40
    CM=41
    CL=42
    IDENTIFIER=43
    STRING_LIT=44
    NUMBER_LIT=45
    NEWLINE=46
    COMMENTS=47
    WS=48
    INT=49
    ERROR_CHAR=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52

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
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 78
                self.match(ZCodeParser.NEWLINE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.list_declared()
            self.state = 85
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.declared()
                self.state = 88
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.variables()
                self.state = 95
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
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
            self.state = 104
            self.match(ZCodeParser.VAR)
            self.state = 105
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 106
            self.match(ZCodeParser.ARROW)
            self.state = 107
            self.expression()
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

        def type1(self):
            return self.getTypedRuleContext(ZCodeParser.Type1Context,0)


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
            self.state = 109
            self.type1()
            self.state = 110
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 111
                self.match(ZCodeParser.LP)
                self.state = 112
                self.list_number()
                self.state = 113
                self.match(ZCodeParser.RP)


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 117
                self.match(ZCodeParser.ARROW)
                self.state = 118
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 122
                self.match(ZCodeParser.CM)
                self.state = 123
                self.list_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(ZCodeParser.NUMBER_LIT)
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
        self.enterRule(localctx, 14, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ZCodeParser.DYNAMIC)
            self.state = 128
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 129
                self.match(ZCodeParser.ARROW)
                self.state = 130
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType1" ):
                return visitor.visitType1(self)
            else:
                return visitor.visitChildren(self)




    def type1(self):

        localctx = ZCodeParser.Type1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self.state = 135
            self.match(ZCodeParser.FUNC)
            self.state = 136
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 137
            self.match(ZCodeParser.LB)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 138
                self.prameters_list()


            self.state = 141
            self.match(ZCodeParser.RB)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 142
                    self.ignore()


                self.state = 145
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 146
                    self.ignore()


                self.state = 149
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 150
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.pram()
                self.state = 154
                self.match(ZCodeParser.CM)
                self.state = 155
                self.prameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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

        def type1(self):
            return self.getTypedRuleContext(ZCodeParser.Type1Context,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

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
            self.state = 160
            self.type1()
            self.state = 161
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 162
                self.match(ZCodeParser.LP)
                self.state = 163
                self.list_number()
                self.state = 164
                self.match(ZCodeParser.RP)


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

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.expression1()
                self.state = 169
                self.match(ZCodeParser.CONCAT)
                self.state = 170
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
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
        self.enterRule(localctx, 26, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.expression2(0)
                self.state = 176
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.DIFF) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.EE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 177
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 187
                    self.expression3(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 198
                    self.expression4(0) 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.expression5() 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_expression5)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ZCodeParser.NOT)
                self.state = 216
                self.expression5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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
        self.enterRule(localctx, 36, self.RULE_expression6)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(ZCodeParser.MINUS)
                self.state = 221
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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

        def list_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.List_expressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.List_expressionContext,i)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

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
        self.enterRule(localctx, 38, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 225
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 226
                    self.match(ZCodeParser.IDENTIFIER)

                    self.state = 227
                    self.match(ZCodeParser.LB)
                    self.state = 229
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                        self.state = 228
                        self.list_expression()


                    self.state = 231
                    self.match(ZCodeParser.RB)
                    pass


                self.state = 234
                self.match(ZCodeParser.LP)
                self.state = 235
                self.list_expression()
                self.state = 236
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 40, self.RULE_expression8)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(ZCodeParser.IDENTIFIER)

                self.state = 242
                self.match(ZCodeParser.LB)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                    self.state = 243
                    self.list_expression()


                self.state = 246
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(ZCodeParser.LB)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                    self.state = 248
                    self.expression()


                self.state = 251
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.literal()
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
        self.enterRule(localctx, 42, self.RULE_list_expression)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.expression()
                self.state = 256
                self.match(ZCodeParser.CM)
                self.state = 257
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
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
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
                self.array_literal()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 267
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
        self.enterRule(localctx, 46, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.LP)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 271
                self.list_expression()


            self.state = 274
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
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 281
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 282
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 283
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 284
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
        self.enterRule(localctx, 50, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.variables()
            self.state = 288
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


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 291
                self.match(ZCodeParser.LP)
                self.state = 292
                self.list_expression()
                self.state = 293
                self.match(ZCodeParser.RP)


            self.state = 297
            self.match(ZCodeParser.ARROW)
            self.state = 298
            self.expression()
            self.state = 299
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


        def elif_loop(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_loopContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


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
        self.enterRule(localctx, 54, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.IF)
            self.state = 302
            self.expression()
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 303
                self.ignore()


            self.state = 306
            self.statement()
            self.state = 307
            self.elif_loop()
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 308
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
        self.enterRule(localctx, 56, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.ELIF)
            self.state = 312
            self.expression()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 313
                self.ignore()


            self.state = 316
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
        self.enterRule(localctx, 58, self.RULE_elif_loop)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.elif_statement()
                self.state = 319
                self.elif_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 60, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.ELSE)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 325
                self.ignore()


            self.state = 328
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
        self.enterRule(localctx, 62, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(ZCodeParser.FOR)
            self.state = 331
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 332
            self.match(ZCodeParser.UNTIL)
            self.state = 333
            self.expression()
            self.state = 334
            self.match(ZCodeParser.BY)
            self.state = 335
            self.expression()
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 336
                self.ignore()


            self.state = 339
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
        self.enterRule(localctx, 64, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZCodeParser.BREAK)
            self.state = 342
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
        self.enterRule(localctx, 66, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(ZCodeParser.CONTINUE)
            self.state = 345
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
        self.enterRule(localctx, 68, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.RETURN)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 348
                self.expression()


            self.state = 351
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


        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 354
            self.match(ZCodeParser.LB)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 355
                self.list_expression()


            self.state = 358
            self.match(ZCodeParser.RB)
            self.state = 359
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

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

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
        self.enterRule(localctx, 72, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(ZCodeParser.BEGIN)
            self.state = 362
            self.ignore()
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 363
                self.list_statement()


            self.state = 366
            self.match(ZCodeParser.END)
            self.state = 367
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
        self.enterRule(localctx, 74, self.RULE_list_statement)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.statement()
                self.state = 370
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
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
        self.enterRule(localctx, 76, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 375
                self.match(ZCodeParser.NEWLINE)
                self.state = 378 
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
        self._predicates[14] = self.expression2_sempred
        self._predicates[15] = self.expression3_sempred
        self._predicates[16] = self.expression4_sempred
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
         




