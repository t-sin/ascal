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

def _read_integer(s):
    int_token = StringIO()
    tail_pos = 0
    for i in range(len(s)):
        if s[i] in "0123456789":
            int_token.write(s[i])
            tail_pos = i
        else:
            break

    token = int_token.getvalue()
    if token is "":
        return None, s
    else:
        return token, s[i:]

def tokenize(s):
    return []

def parse(tokens):
    return []

if __name__ == "__main__":
    print("Hi!")
