#!/usr/bin/env python

DIVISOR = 20201227
SUBJECT_NUMBER = 7


def main():
    door_pub_key = 12232269
    card_pub_key = 19452773
    print("Answer part one: ", part_one(door_pub_key, card_pub_key))
    print("Answer part two: ", part_two(door_pub_key, card_pub_key))


def part_one(door_pub_key, card_pub_key):
    return transform_number(card_pub_key, determine_loop_size(door_pub_key))


def part_two(door_pub_key, card_pub_key):
    pass


def transform_number(subject_number, loop_size):
    num = 1
    for _i in range(loop_size):
        num = (num * subject_number) % DIVISOR
    return num


def determine_loop_size(pub_key):
    # brute force?
    i = 0
    val = 1
    while val != pub_key:
        val = (val * SUBJECT_NUMBER) % DIVISOR
        i += 1
    return i


if __name__ == '__main__':
    main()
