from dz_9 import score


def test_1():
    sc = score(17)
    test_score = 18
    assert test_score == sc


def test_2():
    sc = score(18)
    test_score = 18
    assert test_score == sc


def test_3():
    sc = score(100)
    test_score = 20
    assert test_score == sc


test_1()
test_2()
test_3()
