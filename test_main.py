import pytest
from main import menu

@pytest.mark.parametrize("input_str, expected_output", 
[("XML", 0),("HtMl", 1),("C u    S   t  Om", 2),("notaccept", -1)])

def test_get_command(input_str, expected_output, monkeypatch):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: input_str)
    
    # Call the function
    output = menu.get_command()
    
    # Assert the result
    assert output == expected_output
