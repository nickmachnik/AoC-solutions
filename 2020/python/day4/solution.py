#!/usr/bin/env python

import re

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_keys = ['cid']

key_constraints = {
    'byr': re.compile('^(19[2-9][0-9]|200[0-2])$'),
    'iyr': re.compile('^(201[0-9]|2020)$'),
    'eyr': re.compile('^(202[0-9]|2030)$'),
    'hgt': re.compile('^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$'),
    'hcl': re.compile('^#[0-9a-f]{6}$'),
    'ecl': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
    'pid': re.compile('^[0-9]{9}$')
}


def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(data):
    valid_entries = 0
    for entry in data:
        if all(k in entry for k in required_keys):
            valid_entries += 1
    return valid_entries


def part_two(data):
    valid_entries = 0
    for entry in data:
        if not all(k in entry for k in required_keys):
            continue
        if all(re.match(pattern, entry[k]) is not None
                for k, pattern in key_constraints.items()):
            valid_entries += 1
    return valid_entries


def load_data(path):
    input_data = [{}]
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == "":
                input_data.append({})
            fields = line.split()
            for field in fields:
                k, v = field.split(":")
                input_data[-1][k] = v
    return input_data


if __name__ == '__main__':
    main()
