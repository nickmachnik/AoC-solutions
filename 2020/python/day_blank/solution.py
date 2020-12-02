#!/usr/bin/env python

def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(data):
    pass


def part_two(data):
    pass


def load_data(path):
    input_numbers = []
    with open(path, 'r') as fin:
        for line in fin:
            input_numbers.append(int(line.strip()))
    return input_numbers


if __name__ == '__main__':
    main()
