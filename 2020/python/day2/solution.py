#!/usr/bin/env python

def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(data):
    valid_count = 0
    for cmin, cmax, char, pw in data:
        ccount = pw.count(char)
        if ccount >= cmin and ccount <= cmax:
            valid_count += 1
    return valid_count


def part_two(data):
    valid_count = 0
    for p1, p2, char, pw in data:
        p1 -= 1
        p2 -= 1
        at1, at2 = pw[p1] == char, pw[p2] == char
        if at1 ^ at2:
            valid_count += 1
    return valid_count


def load_data(path):
    input_data = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            fields = line.split()
            cmin, cmax = fields[0].split("-")
            char = fields[1].replace(":", "")
            input_data.append([int(cmin), int(cmax), char, fields[2]])
    return input_data


if __name__ == '__main__':
    main()
