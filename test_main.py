import pytest
from main import menu

@pytest.mark.parametrize("input_str, expected_output", [
    ("XML", 0),
    ("HtMl", 1),
    ("C u    S   t  Om", 2),
    ("notaccept", -1)
])
def test_get_command(input_str, expected_output):
    output = menu.get_command(input_str)
    assert output == expected_output

@pytest.fixture
def sample_input_string():
    return '<root> treterteter     \n</root>\n\t<root>'

def test_format_string2(sample_input_string):
    output = menu.format_string2(sample_input_string)
    assert output == "<root>treterteter</root><root>"

@pytest.fixture
def sample_input_string2():
    return 'not respect space {not respect space } not respect space (respect space )\n\t\n'

def test_format_string3(sample_input_string2):
    output = menu.format_string3(sample_input_string2)
    assert output == "notrespectspace{notrespectspace}notrespectspace(respect space )"
