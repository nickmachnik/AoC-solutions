#!/usr/bin/env python


def main():
    field_rules, my_ticket, other_tickets = load_data('puzzleinput.txt')
    print("Answer part one:", part_one(field_rules, other_tickets))
    print("Answer part two:", part_two(field_rules, my_ticket, other_tickets))


def part_one(field_rules, other_tickets):
    merged_ranges = make_global_ranges(field_rules)
    invalid_values = []
    for ticket in other_tickets:
        for value in ticket:
            is_invalid = True
            for lo, hi in merged_ranges:
                if value <= hi and value >= lo:
                    is_invalid = False
                    break
            if is_invalid:
                invalid_values.append(value)
    return sum(invalid_values)


def make_global_ranges(field_rules):
    single_ranges = set()
    for ranges in field_rules.values():
        for r in ranges:
            single_ranges.add(r)
    merged_ranges = []
    while len(single_ranges) > 0:
        start_a, end_a = single_ranges.pop()
        to_remove = []
        for r in single_ranges:
            start_b, end_b = r
            if not (start_a > end_b + 1 or start_b > end_a + 1):
                start_a = min(start_a, start_b)
                end_a = max(end_a, end_b)
                to_remove.append(r)
        for r in to_remove:
            single_ranges.remove(r)
        merged_ranges.append((start_a, end_a))
    return merged_ranges


def find_valid_tickets(field_rules, tickets):
    merged_ranges = make_global_ranges(field_rules)
    valid_tickets = []
    for ticket in tickets:
        if is_valid_ticket(merged_ranges, ticket):
            valid_tickets.append(ticket)
    return valid_tickets


def is_valid_ticket(merged_ranges, ticket):
    return all(is_valid_value(merged_ranges, value) for value in ticket)


def is_valid_value(merged_ranges, value):
    for lo, hi in merged_ranges:
        if value <= hi and value >= lo:
            return True
    return False


def find_possible_field_names(field_rules, tickets):
    valid_tickets = find_valid_tickets(field_rules, tickets)
    possible_field_names = []
    for i in range(len(tickets[0])):
        possible_field_names.append(set(field_rules.keys()).copy())
    for ticket in valid_tickets:
        for field_index, value in enumerate(ticket):
            to_remove = []
            for remaining_option in possible_field_names[field_index]:
                if all(
                    (value > hi or value < lo)
                        for lo, hi in field_rules[remaining_option]):
                    to_remove.append(remaining_option)
            for field_name in to_remove:
                possible_field_names[field_index].remove(field_name)
    return possible_field_names


def resolve_field_names(possible_field_names):
    resolved = {}
    while len(resolved) < len(possible_field_names):
        for field_index, names in enumerate(possible_field_names):
            if len(names) == 1:
                resolved[names.pop()] = field_index
            elif len(names) > 1:
                for e in [e for e in names if e in resolved]:
                    names.remove(e)
    return resolved


def part_two(field_rules, my_ticket, other_tickets):
    possible_field_names = find_possible_field_names(
        field_rules, other_tickets)
    field_names = resolve_field_names(possible_field_names)
    product = 1
    for field_name, field_index in field_names.items():
        if field_name.startswith('departure'):
            product *= my_ticket[field_index]
    return product


def load_data(path):
    field_rules = {}
    other_tickets = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == "":
                # skip 'your ticket'
                next(fin)
                break
            field, raw_values = line.split(": ")
            field_rules[field] = []
            for r in raw_values.split(" or "):
                a, b = r.split('-')
                field_rules[field].append((int(a), int(b)))
        my_ticket = [int(e) for e in next(fin).strip().split(',')]
        next(fin)
        next(fin)
        for line in fin:
            other_tickets.append([int(e) for e in line.strip().split(',')])
    return field_rules, my_ticket, other_tickets


if __name__ == '__main__':
    main()
