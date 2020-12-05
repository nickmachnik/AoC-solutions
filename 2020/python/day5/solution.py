#!/usr/bin/env python

import math


def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def find_seat(code):
    rlo, rhi = 0, 127
    clo, chi = 0, 7
    for sym in code:
        if sym == "F":
            rhi = math.floor((rlo + rhi) / 2)
        elif sym == "B":
            rlo = math.ceil((rlo + rhi) / 2)
        elif sym == "L":
            chi = math.floor((clo + chi) / 2)
        elif sym == "R":
            clo = math.ceil((clo + chi) / 2)
        else:
            raise ValueError
    if rhi != rlo or clo != chi:
        raise RuntimeError
    return (rlo, clo, rlo * 8 + clo)


def part_one(data):
    max_seat = 0
    for entry in data:
        max_seat = max(max_seat, find_seat(entry)[2])
    return max_seat


def part_two(data):
    all_seats = [0] * 127 * 8
    for entry in data:
        all_seats[find_seat(entry)[2]] = 1

    for i in range(1, len(all_seats) - 1):
        if all_seats[i-1:i+2] == [1, 0, 1]:
            return i


def load_data(path):
    input_data = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            input_data.append(line)
    return input_data


if __name__ == '__main__':
    main()
