from solution import part_one, part_two, load_directions


def test_part_one():
    assert part_one(load_directions("test_input.txt")) == 10


def test_part_two():
    assert part_two(load_directions("test_input.txt")) == 2208
