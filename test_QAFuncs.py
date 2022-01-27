import QACommsTestFunc

def test_fact():
    assert QACommsTestFunc.fact(3) == 6

def test_list_of_squares():
    assert QACommsTestFunc.list_of_squares(2) == {1: 1, 2: 4}

def test_vowels():
    assert QACommsTestFunc.vowels("letter") == 2
