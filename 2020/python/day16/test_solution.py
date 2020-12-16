from solution import part_one, part_two, load_data, find_valid_tickets


def test_part_one():
    field_rules, my_ticket, other_tickets = load_data('test_input.txt')
    assert part_one(field_rules, other_tickets) == 71


def test_find_valid_tickets():
    field_rules, my_ticket, other_tickets = load_data('test_input.txt')
    exp = [
        [7, 3, 47]]
    assert find_valid_tickets(field_rules, other_tickets) == exp
