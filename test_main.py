import pytest
from main import menu

def test_get_command1():
    output = menu.get_command("XML")
    assert output == 0

def test_get_command2():
    output = menu.get_command("HtMl")
    assert output == 1

def test_get_command3():
    output = menu.get_command("C u    S   t  Om")
    assert output == 2

def test_get_command3():
    output = menu.get_command("notaccept")
    assert output == -1
