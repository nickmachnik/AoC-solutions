#!/usr/bin/env python

class PocketDimension:
    def __init__(self, path):
        self.load_initial_state(path)

    def load_initial_state(self, path):
        self.active_cubes = set()
        with open(path, 'r') as fin:
            for y, line in enumerate(fin):
                line = line.strip()
                for x, symbol in enumerate(line):
                    if symbol == '#':
                        self.active_cubes.add((x, y, 0, 0))

    def cycle(self, neighbor_function):
        inactive_candidates = set()
        active_in_next_cycle = set()

        for x, y, z, w in self.active_cubes:
            active_neighbors = 0
            for neighbor in neighbor_function(x, y, z, w):
                if neighbor in self.active_cubes:
                    active_neighbors += 1
                else:
                    inactive_candidates.add(neighbor)
            if active_neighbors == 2 or active_neighbors == 3:
                active_in_next_cycle.add((x, y, z, w))

        for x, y, z, w in inactive_candidates:
            active_neighbors = 0
            for neighbor in neighbor_function(x, y, z, w):
                if neighbor in self.active_cubes:
                    active_neighbors += 1
            if active_neighbors == 3:
                active_in_next_cycle.add((x, y, z, w))

        self.active_cubes = active_in_next_cycle

    @staticmethod
    def neighbors3D(x, y, z, w):
        for nx in [x - 1, x, x + 1]:
            for ny in [y - 1, y, y + 1]:
                for nz in [z - 1, z, z + 1]:
                    if nx == x and ny == y and nz == z:
                        continue
                    yield nx, ny, nz, w

    @staticmethod
    def neighbors4D(x, y, z, w):
        for nx in [x - 1, x, x + 1]:
            for ny in [y - 1, y, y + 1]:
                for nz in [z - 1, z, z + 1]:
                    for nw in [w - 1, w, w + 1]:
                        if nx == x and ny == y and nz == z and nw == w:
                            continue
                        yield nx, ny, nz, nw

    def num_active_cubes(self):
        return len(self.active_cubes)


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    pd = PocketDimension(path)
    for i in range(6):
        pd.cycle(neighbor_function=PocketDimension.neighbors3D)
    return pd.num_active_cubes()


def part_two(path):
    pd = PocketDimension(path)
    for i in range(6):
        pd.cycle(neighbor_function=PocketDimension.neighbors4D)
    return pd.num_active_cubes()


if __name__ == '__main__':
    main()
