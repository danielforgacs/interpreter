INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        return '[%s][%s]' % (self.type_, self.value)



def integer(src, idx):
    result = ''

    while True:
        result += src[idx]
        idx += 1

        if idx == len(src):
            break

        if not src[idx] in '0123456789':
            break


    return int(result), idx


def skip_whitespace(src, idx):
    while src[idx] == ' ':
        idx += 1
    return idx


def get_next_token(src, idx):
    idx = skip_whitespace(src, idx)
    char = src[idx]

    if char in '0123456789':
        number, idx = integer(src, idx)
        token = Token(INTEGER, number)

    elif char in '+':
        idx += 1
        token = Token(PLUS, '+')

    elif char in '-':
        idx += 1
        token = Token(MINUS, '-')

    else:
        raise

    print('{:<5}{}'.format(idx, token))
    return token, idx



def exp(src, idx=0):
    left, idx = get_next_token(src=src, idx=idx)

    if not left.type_ == INTEGER:
        raise Exception('EXPERRION LEFT ERROR')

    operator, idx = get_next_token(src=src, idx=idx)

    if not operator.type_ in [PLUS, MINUS]:
        raise Exception('EXPERRION OP ERROR')

    right, idx = get_next_token(src=src, idx=idx)

    if not right.type_ == INTEGER:
        raise Exception('EXPERRION RIGHT ERROR')

    if operator.type_ == PLUS:
        result = left.value + right.value
    else:
        result = left.value - right.value

    return result


if __name__ == '__main__':
    pass

    assert exp(src='3+5') == 3+5
    assert exp(src='0+0') == 0
    assert exp(src='9+9') == 9+9
    assert exp(src='100+100') == 100+100
    assert exp(src=' 3+5') == 3+5
    assert exp(src='    3+5') == 3+5
    assert exp(src='    3   +     5') == 3+5
    assert exp(src='3-5') == 3-5
    assert exp(src='0-0') == 0
    assert exp(src='9-9') == 9-9
    assert exp(src='100-100') == 100-100
    assert exp(src=' 3-5') == 3-5
    assert exp(src='    3-5') == 3-5
    assert exp(src='    3   -     5') == 3-5
