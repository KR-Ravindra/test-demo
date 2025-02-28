from hello import *

def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"

# when the function func_sum() is ran, it should take two inputs and return sum of the two numbers

def test_func_sum():
    assert func_sum(1, 2) == 3

def test_func_sum_fail():
    assert func_sum(1, 2) != 4