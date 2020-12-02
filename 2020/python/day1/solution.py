#!/usr/bin/env python

def main():
    part_one()
    part_two()


def part_one():
    pass


def part_two():
    pass


def load_data(path):
    input_numbers = []
    with open(path, 'r') as fin:
        for line in fin:
            input_numbers.append(int(line.strip()))
    return input_numbers


if __name__ == '__main__':
    main()
