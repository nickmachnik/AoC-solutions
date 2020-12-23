from solution import part_one, part_two, load_data, score_deck
from collections import deque


def test_part_one():
    data = load_data('test_input.txt')
    assert part_one(data) == 306


def test_scoring():
    q = deque()
    for num in [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]:
        q.append(num)
    assert score_deck(q) == 291


def test_part_two():
    data = load_data('test_input.txt')
    assert part_two(data) == 291
