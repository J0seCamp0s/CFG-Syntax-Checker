import pytest
from main import menu

def test_get_command1():
    output = menu.get_command(input: "XML")
    assert output == 0

def test_get_command2():
    output = menu.get_command(input: "HtMl")
    assert output == 1

def test_get_command3():
    output = menu.get_command(input: "C u    S   t  Om")
    assert output == 2

def test_get_command3():
    output = menu.get_command(input: "notaccept")
    assert output == -1
