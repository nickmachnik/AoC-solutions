from solution import part_one, part_two, load_data


def test_part_one():
    instructions = load_data("test_input.txt")
    assert part_one(instructions) == 165


def test_part_two():
    instructions = load_data("test_input2.txt")
    assert part_two(instructions) == 208
