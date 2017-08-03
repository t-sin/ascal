"""
Ascal is an associative calculator.
It's just a toy calculator program with simple operation. This project's goal
 is, understanding how to parse the grammer such that:

1. the language has both left/right-associative operators
2. the language has the order of operators

There I think simple languages that has characterisities above. Concretely,
 this code parses and evaluates simple arithmatic operations, that is:

- left associative operations
    - addition `+` and substruction `-`, low priority operations
    - multiply `*` and division `/`, high priority operations
- right associative operations
    - exponential `**`,
- association order changing by parenthesis `(`, `)`

and integer operands (interpreter may prints float number as result, but user
can not input float but integer).
"""

from io import StringIO

def _read_token(chars, s):
    sio = StringIO()
    tail_pos = 0
    for i in range(len(s)):
        if s[i] in chars:
            sio.write(s[i])
            tail_pos = i
        else:
            break

    token = sio.getvalue()
    if token is "":
        return None, s
    else:
        return token, s[tail_pos+1:]

INTEGER_CHARS = "0123456789"
def _read_integer(s):
    return _read_token(INTEGER_CHARS, s)

OPERATOR_CHARS = "+-*/"
def _read_operator(s):
    return _read_token(OPERATOR_CHARS, s)

PARENTHESIS_CHARS = "()"
def _read_parenthesis(s):
    return _read_token(PARENTHESIS_CHARS, s)

WHITESPACE_CHARS = " "
def tokenize(s):
    tokens = []
    str = s

    while str is not "":
        ch = str[0]
        if ch in INTEGER_CHARS:
            token, rest = _read_integer(str)
        elif ch in OPERATOR_CHARS:
            token, rest = _read_operator(str)
        elif ch in PARENTHESIS_CHARS:
            token, rest = _read_parenthesis(str)
        elif ch in WHITESPACE_CHARS:
            token, rest = None, str[1:]
        else:
            raise Exception("Unexpected char: '{}'".format(ch))
        if token:
            tokens.append(token)
        str = rest

    return tokens

def parse(tokens):
    return []

if __name__ == "__main__":
    print("Hi!")
