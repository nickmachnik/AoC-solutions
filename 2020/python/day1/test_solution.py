from solution import part_one, part_two, load_data


def test_part_one():
    test_numbers = load_data("testdata.txt")
    assert test_numbers == [1721, 979, 366, 299, 675, 1456]
    assert 1 == 2


def test_part_two():
    pass