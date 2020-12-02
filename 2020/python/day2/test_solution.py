from solution import part_one, part_two, load_data


def test_loading():
    test_input = load_data("testdata.txt")
    expected = [
        [1, 3, "a", "abcde"], [1, 3, "b", "cdefg"], [2, 9, "c", "ccccccccc"]]
    assert test_input == expected


def test_part_one():
    assert part_one(load_data("testdata.txt")) == 2


def test_part_two():
    assert part_two(load_data("testdata.txt")) == 1
