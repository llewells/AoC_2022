from aoc_utils import funcs

def test_load_text_file():
    assert funcs.load_text_file("input.txt") == ['hello', 'world']