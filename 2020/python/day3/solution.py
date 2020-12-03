#!/usr/bin/env python

def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))
    pass


def part_one(data, right=3, down=1):
    rows = len(data)
    cols = len(data[0])
    curr_row, curr_col = 0, 0
    tree_count = 0
    while curr_row < rows:
        if data[curr_row][curr_col] == "#":
            tree_count += 1
        curr_row += down
        curr_col = (curr_col + right) % cols
    return tree_count


def part_two(data):
    prod = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        prod *= part_one(data, right, down)
    return prod


def load_data(path):
    input_data = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            input_data.append(line)
    return input_data


if __name__ == '__main__':
    main()