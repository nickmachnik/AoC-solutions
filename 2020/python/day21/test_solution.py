from solution import part_one, part_two, load_data


def test_part_one():
    data = load_data('test_input.txt')
    assert part_one(data) == 5


def test_part_two():
    data = load_data('test_input.txt')
    assert part_two(data) == "mxmxvkd,sqjhc,fvjkl"
