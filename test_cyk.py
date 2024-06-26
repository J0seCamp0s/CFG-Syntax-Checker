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
    assert table[5][6] == set()
    assert table[6][7] == set()
    assert table[8][9] == set()

@pytest.fixture
def sample_grammar3():
    grammar = {
        'S': ['NPVP'],
        'VP': ['VBGNNS', 'VBZVP'],
        'NP': ['DTNN', 'JJNNS'],
        'DT': ['an'],
        'NN': ['engineer'],
        'VBZ': ['likes'],
        'VBG': ['building'],
        'JJ': ['building'],
        'NNS': ['solutions'],
    }
    return grammar

@pytest.fixture
def sample_input_string2():
    return 'anengineerlikesbuildingsolutions'

def test_fill_table(sample_grammar3, sample_input_string2):
    table = CFG.initialize_table(sample_input_string2, sample_grammar3)
    CFG.fill_table(table, sample_grammar3)
    assert table == [[{'DT'}, {'NP'}, set(), set(), {'S'}],
                    [set(), {'NN'}, set(), set(), set()],
                    [set(), set(), {'VBZ'}, set(), {'VP'}],
                    [set(), set(), set(), {'JJ', 'VBG'}, {'VP', 'NP'}],
                    [set(), set(), set(), set(), {'NNS'}]]

def test_parse_print(sample_grammar3,sample_input_string2,capsys):
    expected_ouput1 = """-----------------------
   VP
S--|
   NP
-----------------------
------------------------
    VP
VP--|
    VBZ
------------------------
------------------------
    NN
NP--|
    DT
------------------------
------------------------
    NNS
VP--|
    VBG
------------------------
------------------------
    NNS
NP--|
    JJ
------------------------
------------------------
DT--an
------------------------
------------------------
NN--engineer
------------------------
------------------------
VBZ--likes
------------------------
------------------------
VBG--building
------------------------
------------------------
JJ--building
------------------------
------------------------
NNS--solutions
------------------------
[{'DT'}, {'NP'}, set(), set(), {'S'}]
[set(), {'NN'}, set(), set(), set()]
[set(), set(), {'VBZ'}, set(), {'VP'}]
[set(), set(), set(), {'VBG', 'JJ'}, {'VP', 'NP'}]
[set(), set(), set(), set(), {'NNS'}]
"""
    expected_ouput2 = """-----------------------
   VP
S--|
   NP
-----------------------
------------------------
    VP
VP--|
    VBZ
------------------------
------------------------
    NN
NP--|
    DT
------------------------
------------------------
    NNS
NP--|
    JJ
------------------------
------------------------
    NNS
VP--|
    VBG
------------------------
------------------------
DT--an
------------------------
------------------------
NN--engineer
------------------------
------------------------
VBZ--likes
------------------------
------------------------
JJ--building
------------------------
------------------------
VBG--building
------------------------
------------------------
NNS--solutions
------------------------
[{'DT'}, {'NP'}, set(), set(), {'S'}]
[set(), {'NN'}, set(), set(), set()]
[set(), set(), {'VBZ'}, set(), {'VP'}]
[set(), set(), set(), {'JJ', 'VBG'}, {'NP', 'VP'}]
[set(), set(), set(), set(), {'NNS'}]
"""
    sample_idxs = [[0, 2], [2, 10], [10, 15], [15, 23], [23, 32]]
    sample_table =  [[{'DT'}, {'NP'}, set(), set(), {'S'}],
                    [set(), {'NN'}, set(), set(), set()],
                    [set(), set(), {'VBZ'}, set(), {'VP'}],
                    [set(), set(), set(), {'JJ', 'VBG'}, {'VP', 'NP'}],
                    [set(), set(), set(), set(), {'NNS'}]]
    CFG.print_parse(sample_table,sample_grammar3,sample_input_string2,sample_idxs)
    captured = capsys.readouterr()
    assert captured.out == expected_ouput1 or captured.out == expected_ouput2
