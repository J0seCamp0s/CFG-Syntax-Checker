import pytest
from cyk import CFG

@pytest.fixture
def sample_grammar():
    grammar = {
        'S': {'a'},
        'A': {'b'},
        'B': {'c'},
        'C': {'d'},
        'D': {'e'},
        'E': {'f'}
    }
    return grammar

def test_initialize_table(sample_grammar):
    input_string = 'abcdef'
    table = CFG.initialize_table(input_string, sample_grammar)

    # Assert that the table is initialized correctly
    assert len(table) == len(input_string)

    # Check specific entries in the table based on the grammar
    assert table[0][0] == {'S'}
    assert table[1][1] == {'A'}
    assert table[2][2] == {'B'}
    assert table[3][3] == {'C'}
    assert table[4][4] == {'D'}
    assert table[5][5] == {'E'}

    # Check that non-terminals not derivable from input symbols are empty sets
    assert table[0][1] == set()
    assert table[1][2] == set()
    assert table[2][3] == set()
    assert table[3][4] == set()
    assert table[4][5] == set()