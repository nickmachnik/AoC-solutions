#!/usr/bin/env python

from itertools import product


class PocketDimension:
    def __init__(self, path, dimensionality):
        self.ndim = dimensionality
        self.load_initial_state(path)

    def load_initial_state(self, path):
        self.active_cubes = set()
        with open(path, 'r') as fin:
            for y, line in enumerate(fin):
                line = line.strip()
                for x, symbol in enumerate(line):
                    if symbol == '#':
                        self.active_cubes.add(
                            tuple([x, y] + [0] * (self.ndim - 2)))

    def cycle(self):
        inactive_candidates = set()
        active_in_next_cycle = set()

        for cube in self.active_cubes:
            active_neighbors = 0
            for neighbor in self.neighbors(cube):
                if neighbor == cube:
                    continue
                elif neighbor in self.active_cubes:
                    active_neighbors += 1
                else:
                    inactive_candidates.add(neighbor)
            if active_neighbors == 2 or active_neighbors == 3:
                active_in_next_cycle.add(cube)

        for cube in inactive_candidates:
            active_neighbors = 0
            for neighbor in self.neighbors(cube):
                if neighbor in self.active_cubes:
                    active_neighbors += 1
            if active_neighbors == 3:
                active_in_next_cycle.add(cube)

        self.active_cubes = active_in_next_cycle

    def neighbors(self, cube):
        return product(
            *[
                [cube[i] - 1, cube[i], cube[i] + 1]
                for i in range(self.ndim)]
            )

    def num_active_cubes(self):
        return len(self.active_cubes)


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    pd = PocketDimension(path, 3)
    for i in range(6):
        pd.cycle()
    return pd.num_active_cubes()


def part_two(path):
    pd = PocketDimension(path, 4)
    for i in range(6):
        pd.cycle()
    return pd.num_active_cubes()


if __name__ == '__main__':
    main()
