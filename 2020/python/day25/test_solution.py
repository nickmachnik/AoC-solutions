from solution import part_one, part_two, determine_loop_size


def test_determine_loop_size():
    assert determine_loop_size(5764801) == 8
    assert determine_loop_size(17807724) == 11


def test_part_one():
    assert part_one(5764801, 17807724) == 14897079


def test_part_two():
    assert part_two(5764801, 17807724) is None
