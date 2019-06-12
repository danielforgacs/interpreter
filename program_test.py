import program
import pytest


SRC_01 = """
BEGIN
END.
"""

TOKENS_01 = [
    program.BEGIN_TOKEN,
    program.END_TOKEN,
    program.DOT_TOKEN,
]


def test__tokenize_01():
    idx = 0

    for expectedtoken in TOKENS_01:
        token, idx = program.find_token(SRC_01, idx)
        assert token == expectedtoken



if __name__ == '__main__':
    pytest.main([
        __file__,
        # '-s',
        # '-x',
    ])
