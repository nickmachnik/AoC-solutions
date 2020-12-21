#!/usr/bin/env python

import math


class Tile:
    class Border:
        def __init__(self, pattern):
            self.pattern = pattern
            self.neighbor = None

        def set_neighbor(self, key):
            self.neighbor = key

        def set_pattern(self, pattern):
            self.pattern = pattern

        def has_neighbor(self):
            return self.neighbor is not None

        def invert(self):
            self.pattern = self.pattern[::-1]

    def __init__(self, lines):
        self.parse_lines(lines)
        self.top = Tile.Border(self.grid[0])
        self.bottom = Tile.Border(self.grid[-1])
        self.left = Tile.Border([r[0] for r in self.grid])
        self.right = Tile.Border([r[-1] for r in self.grid])

    def _parse_data(self, lines):
        if not lines[0].startswith('Tile'):
            raise ValueError
        self.id = int(lines[0].split()[1][:-1])
        self.grid = [list(line) for line in lines[1:]]
        self.dim = len(self.grid)
        self._update_borders()

    def _rotate_borders(self):
        """
        Rotates clockwise.
        """
        tmp = self.top
        self.top = self.left
        self.top.invert()
        self.left = self.bottom
        self.bottom = self.right
        self.bottom.invert()
        self.right = tmp

    def borders(self):
        yield self.top
        yield self.right
        yield self.bottom
        yield self.left

    def _flip_borders_horizontal(self):
        self.top, self.bottom = self.bottom, self.top
        self.left.invert()
        self.right.invert()

    def _flip_borders_vertical(self):
        self.left, self.right = self.right, self.left
        self.top.invert()
        self.bottom.invert()

    def _flip_horizontal(self):
        for upper_row_ix in range(self.dim // 2):
            self.grid[upper_row_ix], self.grid[-(upper_row_ix + 1)] = \
                self.grid[-(upper_row_ix + 1)], self.grid[upper_row_ix]
        self._flip_borders_horizontal()

    def _flip_vertical(self):
        for row in self.grid:
            for i in range(self.dim // 2):
                row[i], row[-(i + 1)] = row[-(i + 1)], row[i]
        self._flip_borders_vertical

    def _rotate(self):
        n = self.dim
        for i in range(n):
            if i >= (n - 1 - i):
                return
            for j in range(i, n - i - 1):
                self.swap_quartet(i, j)
        self._rotate_borders()

    def _swap_quartet(self, i, j):
        # this has to be -1.
        # otherwise we would never get to n == i or n == j,
        # because the len is always the largest index + 1
        n = self.dim - 1
        assert i <= n, j <= n
        tmp = self.grid[i][j]
        self.grid[i][j] = self.grid[j][n - i]
        self.grid[j][n - i] = self.grid[n - i][n - j]
        self.grid[n - i][n - j] = self.grid[n - j][i]
        self.grid[n - j][i] = tmp

    def has_free_borders(self):
        return any(b.has_neighbor() is False for b in self.borders)

    def align(self, other):
        pass


def main():
    tiles = [Tile(lines) for lines in load_data('puzzleinput.txt')]
    print("Answer part one:", part_one(tiles))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(tiles):
    """
    The borders of adjacent tiles have to match.
    Tiles can be rotated or even flipped.

    Pick a tile, go through the remaining tiles, try to match somewhere.
    When the match is found, connect them.
    """
    for ref_tile in tiles:
        for other_tile in tiles:
            if ref_tile is other_tile or not other_tile.has_free_borders():
                continue


def part_two(path):
    pass


def load_data(path):
    tiles_data = [[]]
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == '':
                tiles_data.append([])
            tiles_data[-1].append(line)
    return tiles_data


if __name__ == '__main__':
    main()
