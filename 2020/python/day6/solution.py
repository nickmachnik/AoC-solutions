#!/usr/bin/env python


def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(data):
    distinct_counts = 0
    for group in data:
        yes_answered = set()
        for person in group:
            for answer in person:
                yes_answered.add(answer)
        distinct_counts += len(yes_answered)
    return distinct_counts


def part_two(data):
    everyone_yes = 0
    for group in data:
        yes_answered = {}
        for person in group:
            for answer in person:
                if answer not in yes_answered:
                    yes_answered[answer] = 0
                yes_answered[answer] += 1
        everyone_yes += sum(
            1 for v in yes_answered.values() if v == len(group))
        print(everyone_yes)
    return everyone_yes


def load_data(path):
    input_data = [[]]
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == "" and input_data[-1] != []:
                input_data.append([])
            else:
                input_data[-1].append(line)
    return input_data


if __name__ == '__main__':
    main()
