#!/usr/bin/env python


def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(data):
    jolts = sorted(data)
    one_diff = 0
    three_diff = 1
    prev_jolt = 0
    for pos, jolt in enumerate(jolts):
        delta_jolt = jolt - prev_jolt
        if delta_jolt == 1:
            one_diff += 1
        elif delta_jolt == 3:
            three_diff += 1
        prev_jolt = jolt
    return one_diff * three_diff


def part_two(data):
    jolts = [0] + sorted(data)
    path_counts = [0] * (len(jolts))
    path_counts[0] = 1
    for node_index in range(len(jolts)):
        curr_jolt = jolts[node_index]
        incoming_count = path_counts[node_index]
        for upstream_index in range(node_index + 1, node_index + 4):
            if (upstream_index >= len(jolts)
                    or jolts[upstream_index] - curr_jolt > 3):
                break
            path_counts[upstream_index] += incoming_count
    return path_counts[-1]


def load_data(path):
    data = []
    with open(path, 'r') as fin:
        for line in fin:
            data.append(int(line.strip()))
    return data


if __name__ == '__main__':
    main()
