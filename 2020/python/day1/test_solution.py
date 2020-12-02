from solution import part_one, part_two, load_data


def test_loading():
    test_numbers = load_data("testdata.txt")
    assert test_numbers == [1721, 979, 366, 299, 675, 1456]


def test_part_one():
    assert part_one(load_data("testdata.txt")) == 514579


def test_part_two():
    assert part_two(load_data("testdata.txt")) == 241861950