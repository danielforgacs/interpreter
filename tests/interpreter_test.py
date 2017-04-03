import os
import pytest

sys = os.sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import source.interpreter as itpr



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}*{1}'.format(k, i), k*i] for k in range(10) for i in range(10)
])
def test_interpreter_multiplies_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0} + {1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   +     {1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_with_whitespace_2(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0} + {1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   +   {1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_with_whitespace_2(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   *   {1}'.format(k, i), k*i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_multiplies_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   /   {1}'.format(k, i), k/i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_divides_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



def test_10():
    text = '6*5'
    assert 6*5 == itpr.Interpreter(itpr.Lexer(text)).expr()



if __name__ == '__main__':
    args = [
        os.path.basename(__file__),
        # '-s'
    ]
    pytest.main(args)