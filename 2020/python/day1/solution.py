#!/usr/bin/env python

from itertools import combinations


def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(data):
    for a, b in combinations(data, 2):
        if a + b == 2020:
            return a * b


def part_two(data):
    for a, b, c in combinations(data, 3):
        if a + b + c == 2020:
            return a * b * c


def load_data(path):
    input_numbers = []
    with open(path, 'r') as fin:
        for line in fin:
            input_numbers.append(int(line.strip()))
    return input_numbers


if __name__ == '__main__':
    main()
