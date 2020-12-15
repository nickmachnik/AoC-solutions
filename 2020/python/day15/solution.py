#!/usr/bin/env python


def main():
    starting_numbers = load_data('puzzleinput.txt')
    print("Answer part one:", part_one(starting_numbers))
    print("Answer part two:", part_two(starting_numbers))


def play_game(starting_numbers, dinner_time):
    spoken_numbers = {}
    t = 1
    for number in starting_numbers:
        say_number(t, number, spoken_numbers)
        t += 1
    last_number = starting_numbers[-1]
    for turn in range(t, dinner_time + 1):
        _last_time_said, turn_interval = spoken_numbers[last_number]
        if turn_interval is None:
            say_number(turn, 0, spoken_numbers)
            last_number = 0
        else:
            say_number(turn, turn_interval, spoken_numbers)
            last_number = turn_interval
    return last_number


def say_number(turn, number, spoken_numbers):
    num_info = spoken_numbers.get(number)
    if num_info is None:
        spoken_numbers[number] = (turn, None)
    else:
        spoken_numbers[number] = (turn, turn - num_info[0])


def part_one(starting_numbers):
    return play_game(starting_numbers, dinner_time=2020)


def part_two(starting_numbers):
    return play_game(starting_numbers, dinner_time=30000000)


def load_data(path):
    with open(path, 'r') as fin:
        return [int(e) for e in next(fin).strip().split(',')]


if __name__ == '__main__':
    main()
