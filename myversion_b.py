"""
"""

INT = 'INT'
LPAREN = '('
RPAREN = ')'
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'
EOF = 'EOF'



import pytest


class Token:
    def __init__(self, typ, value):
        self.typ = typ
        self.value = value


def get_integer(text, pos):
  result = ''

  while text[pos] in '0123456789':
      result += text[pos]
      if pos == len(text)-1:
          break
      pos += 1

  return Token(INT, int(result)), pos


def skip_space(text, pos):
    while text[pos] == ' ':
        pos += 1

    return pos





def get_next_token(source, pos):
    token = Token(typ=EOF, value='EOF')

    while pos < len(source):
        pos = skip_space(text=source, pos=pos)

        if source[pos] in '0123456789':
            token, pos = get_integer(text=source, pos=pos)

        elif source[pos] in '+':
            token = Token(PLUS, '+')

        elif source[pos] in '-':
            token = Token(MINUS, '-')

        pos += 1

    return token, pos


def calculator(source):
    """
    expr   : term ((PLUS | MINUS) term)*
    term   : factor ((MUL | DIV) factor)*
    factor : INTEGER | LPAREN expr RPAREN
    """
    result = ''
    pos = 0
    token, pos = get_next_token(source=source, pos=pos)

    if token.typ == INT:
        result = 0


    while token.typ != EOF:
        token, pos = get_next_token(source=source, pos=pos)

        if token.typ == INT:
            result += expr(text=source, pos=pos)






    return result



def expr(text, pos):
    pos = skip_space(text=text, pos=pos)
    token, pos = get_integer(text=text, pos=pos)
    result = token.value

    while pos < len(text)-1:
        pos = skip_space(text=text, pos=pos)
        op = text[pos]
        pos += 1
        pos = skip_space(text=text, pos=pos)
        token, pos = get_integer(text=text, pos=pos)

        if op == '+':
            result += token.value
        elif op == '-':
            result -= token.value

    return result

@pytest.mark.parametrize('args, expected', (
    (('1', 0, 1), Token(INT, 1)),
    (('123', 0, 3), Token(INT, 123)),
    (('    123', 4, 7), Token(INT, 123)),
    (('    123', 5, 7), Token(INT, 23)),
    (('    +', 0, 5), Token(PLUS, '+')),
    (('    +', 4, 5), Token(PLUS, '+')),
    (('    -', 4, 5), Token(MINUS, '-')),
    ))
def test_get_next_token(args, expected):
    token, pos = get_next_token(*args[:2])
    assert token.typ == expected.typ
    assert token.value == expected.value
    assert pos == args[2]


@pytest.mark.parametrize('kwargs, expected', (
    ({'text': 'a', 'pos': 0}, 0),
    ({'text': ' a', 'pos': 0}, 1),
    ({'text': '   a', 'pos': 0}, 3),
    ({'text': '   a', 'pos': 2}, 3),
    ({'text': 's   a', 'pos': 2}, 4),
    ))
def test_skip_space(kwargs, expected):
    pos = skip_space(**kwargs)
    assert pos == expected


@pytest.mark.parametrize('text, expected', (
    ('', ''),
    # ('1', 1),
    ))
def test_calculator(text, expected):
    assert calculator(source=text) == expected



if __name__ == '__main__':
    pass

    pytest.main([
        __file__,
    ])