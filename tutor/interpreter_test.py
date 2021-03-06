import interpreter
import pytest


cases_01 = [
    ['3+5', 3+5],
    ['0+0', 0],
    ['9+9', 18],
]

cases_02 = [
    ['3-5', 3-5],
    ['0-0', 0],
    ['9-9', 9-9],
    ['5-3', 5-3],
]

cases_03 = [
    ['31+5', 31+5],
    ['12+0', 12],
    ['5+32', 5+32],
    ['12345+54321', 12345+54321],
]

cases_04 = [
    ['   31+5', 31+5],
    ['   31   +5', 31+5],
    ['   31   +   5', 31+5],
    ['   31   +   5   ', 31+5],
    ['   31-5', 31-5],
    ['   31   -5', 31-5],
    ['   31   -   5', 31-5],
    ['   31   -   5   ', 31-5],
]

cases_05 = [
    ['0*0', 0*0],
    ['1*0', 1*0],
    ['0*1', 0*1],
    ['1*1', 1*1],
    ['123*321', 123*321],
    ['   31*5', 31*5],
    ['   31   *5', 31*5],
    ['   31   *   5', 31*5],
    ['   31   *   5   ', 31*5],
]

cases_06 = [
    ['0/1', 0/1],
    ['1/1', 1/1],
    ['123/321', 123/321],
    ['   31/5', 31/5],
    ['   31   /5', 31/5],
    ['   31   /   5', 31/5],
    ['   31   /   5   ', 31/5],
]

cases_07 = [
    ['1+2+3', 1+2+3],
    ['1+2+3+2+1', 1+2+3+2+1],
    ['12+23+34+25+16', 12+23+34+25+16],
    [' 12  +  23  +    34  +25 + 16  ', 12+23+34+25+16],
    [' 1  + 1  -  1  /  1 * 1 +  1 + 1 - 1  ', 1+1-1/1*1+1+1-1],
]

cases_08 = [
    ['(1)', 1],
    ['((1))', 1],
    ['(((1)))', 1],
    ['(((1+1)))', 1+1],
    ['(1+1)', (1+1)],
    ['(1+1)+1', (1+1)+1],
    [' ( 1 + 1  )  +   1', (1+1)+1],
    ['(1*1)+1', (1*1)+1],
    ['(1*1)/1', (1*1)/1],
    ['(1*(2+3))/1+(4+(5*6))', (1*(2+3))/1+(4+(5*6))],
]



# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_01)
def test_calculator_can_add_single_digits_without_space(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected



# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_02)
def test_calculator_can_subtract_single_digits_without_space(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected



# @pytest.mark.skip('')
def test_get_next_token_add():
    interp = interpreter.Lexer(text='3+5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.PLUS, '+')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)



# @pytest.mark.skip('')
def test_get_next_token_subtract():
    interp = interpreter.Lexer(text='3-5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.MINUS, '-')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_03)
def test_calculator_can_add_adny_digits_without_space(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected



@pytest.mark.skip('')
def test_emtpy_string_does_not_crash():
    assert not interpreter.Interpreter(interpreter.Lexer('')).expr()




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_04)
def test_space_is_ok(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_05)
def test_multiply(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_06)
def test_div(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_07)
def test_multiple_op_01(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_08)
def test_parentheses(src, expected):
    compiler = interpreter.Interpreter(interpreter.Parser(interpreter.Lexer(src)))
    result = compiler.interpret()
    assert result == expected




def test_AST_basics_2_MULT_7_PLUS_3():
    tkn_int_2 = interpreter.Token(interpreter.INTEGER, 2)
    tkn_int_3 = interpreter.Token(interpreter.INTEGER, 3)
    tkn_int_7 = interpreter.Token(interpreter.INTEGER, 7)

    tkn_mult = interpreter.Token(interpreter.MUL, '*')
    tkn_plus = interpreter.Token(interpreter.MUL, '+')

    num_node_2 = interpreter.Num(token=tkn_int_2)
    num_node_3 = interpreter.Num(token=tkn_int_3)
    num_node_7 = interpreter.Num(token=tkn_int_7)


    node_mult = interpreter.BinOp(
        left=num_node_2,
        op=tkn_mult,
        right=num_node_3,
    )
    node_plus = interpreter.BinOp(
        left=node_mult,
        op=tkn_plus,
        right=num_node_7,
    )




if __name__ == '__main__':
    pytest.main([
        __file__,
        # __file__+'::test_AST_basics_2_MULT_7_PLUS_3',
    ])
