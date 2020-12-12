from solution import part_one, part_two, rotate_ship, load_data


def test_ship_rotation():
    assert rotate_ship("E", "R", 360) == "E"
    assert rotate_ship("E", "L", 360) == "E"
    assert rotate_ship("E", "L", 180) == "W"


def test_part_one():
    data = load_data("test_input.txt")
    assert part_one(data) == 25


def test_part_two():
    data = load_data("test_input.txt")
    assert part_two(data) == 286
