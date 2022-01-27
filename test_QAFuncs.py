import QACommsTestFunc

def test_fact():
    assert QACommsTestFunc.fact(3) == 6

def test_list_of_squares():
    assert QACommsTestFunc.list_of_squares(2) == 7

def vowels():
    assert QACommsTestFunc.vowels("letter") == "e"
