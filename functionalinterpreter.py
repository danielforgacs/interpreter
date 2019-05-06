"""
EXPR: FACTOR
FACTOR: INTEGER
"""

DIGITS = '0123456789'

# Tokens:
EOF = 'EOF'
INTEGER = 'INTEGER'



class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        return '<%s:%s>' % (self.type_, self.value)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def find_integer(src, idx):
    result_char = ''
    char = src[idx]

    while char in DIGITS:
        result_char += char
        idx += 1
        if idx == len(src):
            break
        char = src[idx]

    result = int(result_char)

    return result, idx


def find_token(src, idx):
    token = Token(EOF, EOF)

    while idx < len(src):
        if src[idx] in DIGITS:
            number, idx = find_integer(src, idx)
            token = Token(INTEGER, number)
        else:
            raise Exception('UNEXPECTED CHARACTER')

        return token, idx

    return token, idx


def eat(type_, src, idx):
    token = find_token(src, idx)
    if token.type_ == type_:
        return token
    else:
        raise Exception('UNEXPECTED TOKEN')


def factor(src, idx):
    result = eat(INTEGER, src, idx)
    return result, idx


def expr(src, idx=0):
    result, idx = factor(src, idx)



if __name__ == '__main__':
    pass

