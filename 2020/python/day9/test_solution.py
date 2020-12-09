from solution import part_one, part_two


def test_part_one():
    assert part_one("test_input.txt", preamble_length=5) == 127


def test_part_two():
    assert part_two("test_input.txt", preamble_length=5) == 62
