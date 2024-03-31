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

@pytest.fixture
def sample_grammar2():
    grammar = {
        'S': ['NPVP'],
        'VP': ['VBGNNS', 'VBZVP'],
        'NP': ['DTNN', 'JJNNS'],
        'DT': ['an'],
        'NN': ['engineer'],
        'VBZ': ['likes'],
        'VBG': ['building'],
        'JJ': ['building'],
        'NNS': ['solutions', 'w'],
    }
    return grammar

@pytest.fixture
def sample_input_string():
    return 'anengineerwwlikesbuildingwsolutionsww'

def test_find_substring(sample_input_string, sample_grammar2):
    idxs = CFG.find_substring(sample_input_string, sample_grammar2)
    assert idxs == [[0, 2], [2, 10], [12, 17], [17, 25], [26, 35]]

@pytest.fixture
def sample_arr():
    return ([[0, 2], [2, 10], [12, 17], [17, 25], [26, 35]])

def test_get_substring_numb(sample_input_string, sample_arr):
    n = CFG.get_substring_numb(sample_input_string, sample_arr)
    assert n == 10

def test_initialize_table2(sample_grammar2, sample_input_string):

    table = CFG.initialize_table(sample_input_string, sample_grammar2)
    idxs = CFG.find_substring(sample_input_string, sample_grammar2)
    n = CFG.get_substring_numb(sample_input_string, idxs)
    # Assert that the table is initialized correctly
    assert len(table) == n

    # Check specific entries in the table based on the grammar
    assert table[0][0] == {'DT'}
    assert table[1][1] == {'NN'}
    assert table[2][2] == {'NNS'}
    assert table[3][3] == {'NNS'}
    assert table[4][4] == {'VBZ'}
    assert table[5][5] == {'VBG','JJ'}
    assert table[6][6] == {'NNS'}
    assert table[7][7] == {'NNS'}
    assert table[8][8] == {'NNS'}
    assert table[9][9] == {'NNS'}

    # Check that non-terminals not derivable from input symbols are empty sets
    assert table[0][1] == set()
    assert table[1][2] == set()
    assert table[2][3] == set()
    assert table[3][4] == set()
    assert table[4][5] == set()