"""
Ascal is an toy calculator.

## goals

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

## formal grammer

### nonterminal symbols

<expression> ::= <exp3>
<exp3> ::= <exp2> | <exp2> + <exp2> | <exp2> - <exp2>
<exp2> ::= <exp1> | <exp1> * <exp1> | <exp1> / <exp1>
<exp1> ::= <exp> | <exp> ** <exp>
<exp> ::= <integer> | <expression>

### terminal symbols

<integer> ::= <num> | <num>*

### alphabets

<num> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<op> ::= + | - | * | / | **
<space> ::= ` `
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
            raise Exception("Tokenize error: Unexpected char '{}'".format(ch))
        if token:
            tokens.append(token)
        str = rest

    return tokens

def parse(tokens):
    """Parse tokens with recursive descent parsing"""

    def parse_integer(tokens):
        try:
            return int(tokens[0]), tokens[1:]
        except ValueError:
            raise Exception("Parse error: parser except integer, but there is no token")

    def parse_exp(tokens):
        token = tokens[0]
        if token.isdigit():
            return parse_integer(tokens)
        else:
            return parse_expression(tokens)

    def parse_exp1(tokens):
        stree, rest = parse_exp(tokens)
        if rest:
            token = rest[0]
        else:
            return stree, rest
        while token == "**":
            tree, rest = parse_exp(rest[1:])
            stree = [token, stree, tree]
            if not rest:
                break
            else:
                token = rest[0]

        return stree, rest

    def parse_exp2(tokens):
        stree, rest = parse_exp1(tokens)
        if rest:
            token = rest[0]
        else:
            return stree, rest
        while token == "*" or token == "/":
            tree, rest = parse_exp1(rest[1:])
            stree = [token, stree, tree]
            if not rest:
                break
            else:
                token = rest[0]

        return stree, rest

    def parse_exp3(tokens):
        stree, rest = parse_exp2(tokens)
        if rest:
            token = rest[0]
        else:
            return stree, rest
        while token == "+" or token == "-":
            tree, rest = parse_exp2(rest[1:])
            stree = [token, stree, tree]
            if not rest:
                break
            else:
                token = rest[0]

        return stree, rest

    def parse_expression(tokens):
        return parse_exp3(tokens)

    stree = parse_expression(tokens)
    return stree

if __name__ == "__main__":
    while True:
        print(parse(tokenize(input("?> "))))
