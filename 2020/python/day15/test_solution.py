from solution import part_one, part_two


def test_part_one():
    assert part_one([0, 3, 6]) == 436
    assert part_one([1, 3, 2]) == 1
    assert part_one([2, 1, 3]) == 10
    assert part_one([1, 2, 3]) == 27
    assert part_one([2, 3, 1]) == 78
    assert part_one([3, 2, 1]) == 438
    assert part_one([3, 1, 2]) == 1836


def test_part_two():
    assert part_two([0, 3, 6]) == 175594
