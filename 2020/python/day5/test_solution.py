from solution import find_seat


def test_find_seat():
    assert find_seat("BFFFBBFRRR") == (70, 7, 567)
    assert find_seat("FFFBBBFRRR") == (14, 7, 119)
    assert find_seat("BBFFBBFRLL") == (102, 4, 820)
