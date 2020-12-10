from solution import part_one, part_two, load_data


def test_part_one():
    assert part_one(load_data("test_input.txt")) == 35
    assert part_one(load_data("test_input2.txt")) == 220


def test_part_two():
    assert part_two(load_data("test_input.txt")) == 8
    assert part_two(load_data("test_input2.txt")) == 19208
