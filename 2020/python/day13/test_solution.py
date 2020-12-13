from solution import part_one, part_two, load_data


def test_part_one():
    assert part_one(*load_data('test_input.txt')) == 295


def test_part_two():
    assert part_two(load_data('test_input.txt')[1]) == 1068781
