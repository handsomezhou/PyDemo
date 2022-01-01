# -*- coding: utf-8 -*-
# @Time : 2020/8/20
# @Author : handsomezhou


#start:  
# https: // en.wikipedia.org / wiki / ASCII
#start: ASCII control code chart

NULL_CHARACTER = '\0'

BACKSPACE = '\b'

HORIZONTAL_TAB_CHARACTERS = '\t'

NEW_LINE = '\n'

PAGE_BREAK = '\f'

CARRIAGE_RETURN = '\r'
#end: ASCII control code chart

#start: ASCII printable code chart 

SPACE = ' '

EXCLAMATION_MARK = '!'

QUOTATION_MARK = '"'

NUMBER_SIGN = '#'

DOLLAR_SIGN = '$'

PERCENT_SIGN = '%'

AMPERSAND = '&'

APOSTROPHE = '\''

LEFT_ROUND_BRACKETS = '('

RIGHT_ROUND_BRACKETS = ')'

ASTERISK = '*'

PLUS_SIGN = '+'

COMMA = ','

HYPHEN_MINUS = '-'

FULL_STOP = '.'

SLASH = '/'

BACK_SLASH='\\'

NUMBER_0 = '0'

NUMBER_1 = '1'

NUMBER_2 = '2'

NUMBER_3 = '3'

NUMBER_4 = '4'

NUMBER_5 = '5'

NUMBER_6 = '6'

NUMBER_7 = '7'

NUMBER_8 = '8'

NUMBER_9 = '9'

COLON = ':'

SEMICOLON = ';'

LESS_THAN_SIGN = '<'

EQUALS_SIGN = '='

GREATER_THAN_SIGN = '>'

QUESTION_MARK = '?'

AT_SIGN = '@'

A = 'A'

B = 'B'

C = 'C'

D = 'D'

E = 'E'

F = 'F'

G = 'G'

H = 'H'

I = 'I'

J = 'J'

K = 'K'

L = 'L'

M = 'M'

N = 'N'

O = 'O'

P = 'P'

Q = 'Q'

R = 'R'

S = 'S'

T = 'T'

U = 'U'

V = 'V'

W = 'W'

X = 'X'

Y = 'Y'

Z = 'Z'

LEFT_SQUARE_BRACKETS = '['

BACKSLASH = '\\'

RIGHT_SQUARE_BRACKETS = ']'

CARET = '^'

UNDERSCORE = '_'

GRAVE_ACCENT = '`'

a = 'a'

b = 'b'

c = 'c'

d = 'd'

e = 'e'

f = 'f'

g = 'g'

h = 'h'

i = 'i'

j = 'j'

k = 'k'

l = 'l'

m = 'm'

n = 'n'

o = 'o'

p = 'p'

q = 'q'

r = 'r'

s = 's'

t = 't'

u = 'u'

v = 'v'

w = 'w'

x = 'x'

y = 'y'

z = 'z'

LEFT_CURLY_BRACKETS = '{'

VERTICAL_BAR = '|'

RIGHT_CURLY_BRACKETS = '}'

TILDE = '~'
#end: ASCII printable code chart 

#end:

#start: String

UNKNOW = "--"

NULL_STRING = ""

NULL = "null"

ok = "ok"
Ok = "Ok"
OK = "OK"

FORMAT_ZERO_DECIMAL_PLACES = "%.0f"

FORMAT_ONE_DECIMAL_PLACES = "%.1f"

FORMAT_TWO_DECIMAL_PLACES = "%.2f"

FORMAT_THREE_DECIMAL_PLACES = "%.3f"

FORMAT_FOUR_DECIMAL_PLACES = "%.4f"

INT_TWO_DECIMAL_PLACES = "%02d"

#end: String 

# start:  int

PERCENT_NUMBER = 100

TEN_THOUSAND = 10000

ZERO_OF_INTEGER = 0

ONE_OF_INTEGER = 1

TWO_OF_INTEGER = 2

THREE_OF_INTEGER = 3

FOUR_OF_INTEGER = 4

FIVE_OF_INTEGER = 5

SIX_OF_INTEGER = 6

SEVEN_OF_INTEGER = 7

EIGHT_OF_INTEGER = 8

NINE_OF_INTEGER = 9

TEN_OF_INTEGER = 10


HUNDRED_OF_INTEGER = 100

THOUSAND_OF_INTEGER = 1000

TEN_THOUSAND_OF_INTEGER = 10000

ONE_HUNDRED_MILLION_OF_INTEGER = 100000000

TRUE = 1

FALSE = 0
# end: int

#start: Double 


#小数点后8位
ZERO_OF_DOUBLE_BOUNDARY = float(0.00000001)

ZERO_OF_FLOAT_BOUNDARY = float(0.00000001)

ZERO_OF_DOUBLE = 0.0

ONE_PERCENT = 0.01

HUNDRED_OF_DOUBLE = 100.0

THOUSAND_OF_DOUBLE = 1000.0

TEN_THOUSAND_OF_DOUBLE = 10000.0
#end: Double

#start:  long
ZERO_OF_LONG = 0

#start: others
#Byte掩码
BYTE_MASK = 0xFF

#每字节bit数
BIT_COUNT_PER_BYTE = 8


#Bit掩码
BIT_MASK = 0x01

#short类型掩码
SHORT_MASK = 0xFFFF

#类型掩码
INT_MASK = 0xFFFFFFFF
#end: others


#start: str constant
__file__="__file__"
text="text"
command="command"
csv="csv"
#end: str constant