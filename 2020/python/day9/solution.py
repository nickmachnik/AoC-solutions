#!/usr/bin/env python

from queue import Queue


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path, preamble_length=25):
    with open(path, 'r') as fin:
        q = Queue(maxsize=preamble_length)
        q_vals = set()
        for line in fin:
            new_val = int(line.strip())
            if len(q_vals) < preamble_length:
                q.put(new_val)
                q_vals.add(new_val)
                continue
            # validate
            if any((new_val - val) in q_vals for val in q_vals):
                rem = q.get()
                q.put(new_val)
                q_vals.add(new_val)
                q_vals.remove(rem)
            else:
                return new_val
    return None


def part_two(path, preamble_length=25):
    target_sum = part_one(path, preamble_length)
    with open(path, 'r') as fin:
        q = Queue()
        curr_sum = 0
        for line in fin:
            new_val = int(line.strip())
            if curr_sum < target_sum:
                q.put(new_val)
                curr_sum += new_val
            while curr_sum > target_sum:
                curr_sum -= q.get()
            if curr_sum == target_sum:
                return min_max_sum(q)
    return False


def min_max_sum(q):
    v = q.get()
    min_val = v
    max_val = v
    while not q.empty():
        v = q.get()
        max_val = max(max_val, v)
        min_val = min(min_val, v)
    return min_val + max_val


if __name__ == '__main__':
    main()
