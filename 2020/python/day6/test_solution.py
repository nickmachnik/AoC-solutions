from solution import part_one, load_data, part_two


def test_part_one():
    data = load_data("test_input.txt")
    assert part_one(data) == 11


def test_part_two():
    data = load_data("test_input.txt")
    assert part_two(data) == 6
