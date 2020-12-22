#!/usr/bin/env python

from queue import Queue


class SeamonsterFinder:
    pattern = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "]

    def __init__(self):
        self._make_match_rules()
        self.height = len(self.pattern)
        self.length = len(self.pattern[0])

    def _make_match_rules(self):
        self.body_parts = [
            [i for i, e in enumerate(s) if e == '#'] for s in self.pattern]

    def is_seamonster(self, seamap, row, col):
        for inverse_height, height_level in enumerate(self.body_parts):
            if any(
                seamap[row + inverse_height][col + body_part_position] != '#'
                    for body_part_position in height_level):
                return False
        return True

    def remove_seamonster(self, seamap, row, col):
        for inverse_height, height_level in enumerate(self.body_parts):
            for body_part_position in height_level:
                seamap[row + inverse_height][col + body_part_position] = '.'


class Tile:
    class Border:
        def __init__(self, tile):
            self.tile = tile
            self.neighbor = None

        def set_neighbor(self, neighbor):
            self.neighbor = neighbor

        def has_neighbor(self):
            return self.neighbor is not None

        def pattern(self):
            if self.is_top():
                return self.tile.grid[0]
            elif self.is_right():
                return [r[-1] for r in self.tile.grid]
            elif self.is_bottom():
                return self.tile.grid[-1]
            elif self.is_left():
                return [r[0] for r in self.tile.grid]
            else:
                return RuntimeError

        def inverse_pattern(self):
            return self.pattern()[::-1]

        def is_top(self):
            return self is self.tile.top

        def is_left(self):
            return self is self.tile.left

        def is_right(self):
            return self is self.tile.right

        def is_bottom(self):
            return self is self.tile.bottom

        def side(self):
            if self.is_top():
                return 'top'
            elif self.is_right():
                return 'right'
            elif self.is_bottom():
                return 'bottom'
            elif self.is_left():
                return 'left'
            else:
                return RuntimeError

    def __init__(self, tile_id, lines):
        self.id = tile_id
        self.parse_lines(lines)
        self.top = Tile.Border(self)
        self.bottom = Tile.Border(self)
        self.left = Tile.Border(self)
        self.right = Tile.Border(self)

    def __repr__(self):
        return "\n".join(["".join(r) for r in self.grid])

    def parse_lines(self, lines):
        self.grid = [list(line) for line in lines]
        self.dim = len(self.grid)

    def free_borders(self):
        if not self.top.has_neighbor():
            yield self.top
        if not self.right.has_neighbor():
            yield self.right
        if not self.bottom.has_neighbor():
            yield self.bottom
        if not self.left.has_neighbor():
            yield self.left

    def aligned_borders(self):
        if self.top.has_neighbor():
            yield self.top
        if self.right.has_neighbor():
            yield self.right
        if self.bottom.has_neighbor():
            yield self.bottom
        if self.left.has_neighbor():
            yield self.left

    def borders(self):
        yield self.top
        yield self.right
        yield self.bottom
        yield self.left

    def flip_horizontal(self):
        for upper_row_ix in range(self.dim // 2):
            self.grid[upper_row_ix], self.grid[-(upper_row_ix + 1)] = \
                self.grid[-(upper_row_ix + 1)], self.grid[upper_row_ix]
        self.top, self.bottom = self.bottom, self.top

    def flip_vertical(self):
        for row in self.grid:
            for i in range(self.dim // 2):
                row[i], row[-(i + 1)] = row[-(i + 1)], row[i]
        self.left, self.right = self.right, self.left

    def rotate_right(self):
        n = self.dim
        for i in range(n):
            if i >= (n - 1 - i):
                break
            for j in range(i, n - i - 1):
                self._swap_quartet_right(i, j)
        self._rotate_borders_right()

    def _swap_quartet_right(self, i, j):
        n = self.dim - 1
        assert i <= n, j <= n
        tmp = self.grid[i][j]
        self.grid[i][j] = self.grid[n - j][i]
        self.grid[n - j][i] = self.grid[n - i][n - j]
        self.grid[n - i][n - j] = self.grid[j][n - i]
        self.grid[j][n - i] = tmp

    def rotate_left(self):
        n = self.dim
        for i in range(n):
            if i >= (n - 1 - i):
                break
            for j in range(i, n - i - 1):
                self._swap_quartet_left(i, j)
        self._rotate_borders_left()

    def _swap_quartet_left(self, i, j):
        n = self.dim - 1
        assert i <= n, j <= n
        tmp = self.grid[i][j]
        self.grid[i][j] = self.grid[j][n - i]
        self.grid[j][n - i] = self.grid[n - i][n - j]
        self.grid[n - i][n - j] = self.grid[n - j][i]
        self.grid[n - j][i] = tmp

    def _rotate_borders_left(self):
        tmp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = tmp

    def _rotate_borders_right(self):
        tmp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = tmp

    def has_free_borders(self):
        return any(b.has_neighbor() is False for b in self.borders())

    def num_free_borders(self):
        return sum(b.has_neighbor() is False for b in self.borders())

    def align(self, other):
        for border_b in other.free_borders():
            for border_a in self.free_borders():
                if (border_a.pattern() == border_b.pattern()
                        or border_a.inverse_pattern() == border_b.pattern()):
                    border_a.set_neighbor(border_b)
                    border_b.set_neighbor(border_a)
                    return True
        return False

    def inner_grid(self):
        return [r[1:-1] for r in self.grid[1:-1]]


def main():
    tiles = [
        Tile(int(lines[0].split()[1][:-1]), lines[1:])
        for lines in load_data('puzzleinput.txt')]
    tiles = arrange_tiles(tiles)
    print("Answer part one:", part_one(tiles))
    print("Answer part two:", part_two(tiles))


def part_one(arranged_tiles):
    corner_id_product = 1
    corner_count = 0
    for tile in arranged_tiles:
        if tile.num_free_borders() == 2:
            corner_id_product *= tile.id
            corner_count += 1
    if corner_count != 4:
        raise RuntimeError
    return corner_id_product


def part_two(arranged_tiles):
    for tile in arranged_tiles:
        if not tile.top.has_neighbor() and not tile.left.has_neighbor():
            top_left = tile
            break

    tile_ids = [[top_left.id]]
    inner_tiles = [[top_left.inner_grid()]]
    q = Queue(maxsize=len(arranged_tiles))
    seen = set()
    # tile, row
    q.put((top_left, 0))
    seen.add(top_left.id)
    while not q.empty():
        ref_tile, row = q.get()

        if (ref_tile.bottom.has_neighbor()
                and ref_tile.bottom.neighbor.tile.id not in seen):
            lower_neighbor = ref_tile.bottom.neighbor.tile
            if ref_tile.bottom.neighbor.is_left():
                lower_neighbor.rotate_right()
            elif ref_tile.bottom.neighbor.is_bottom():
                lower_neighbor.flip_horizontal()
            elif ref_tile.bottom.neighbor.is_right():
                lower_neighbor.rotate_left()

            if (ref_tile.bottom.pattern()
                    == ref_tile.bottom.neighbor.inverse_pattern()):
                lower_neighbor.flip_vertical()

            if len(inner_tiles) <= row + 1:
                inner_tiles.append([lower_neighbor.inner_grid()])
                tile_ids.append([lower_neighbor.id])
            else:
                inner_tiles[row + 1].append(lower_neighbor.inner_grid())
                tile_ids[row + 1].append(lower_neighbor.id)
            seen.add(lower_neighbor.id)
            q.put((lower_neighbor, row + 1))

        if (ref_tile.right.has_neighbor()
                and ref_tile.right.neighbor.tile.id not in seen):
            right_neighbor = ref_tile.right.neighbor.tile
            if ref_tile.right.neighbor.is_right():
                right_neighbor.flip_vertical()
            elif ref_tile.right.neighbor.is_top():
                right_neighbor.rotate_left()
            elif ref_tile.right.neighbor.is_bottom():
                right_neighbor.rotate_right()

            if (ref_tile.right.pattern()
                    == ref_tile.right.neighbor.inverse_pattern()):
                right_neighbor.flip_horizontal()

            inner_tiles[row].append(right_neighbor.inner_grid())
            tile_ids[row].append(right_neighbor.id)
            seen.add(right_neighbor.id)
            q.put((right_neighbor, row))

    tile_height = len(inner_tiles[0][0])
    inner_tiles_merged = []
    for row_batch, row in enumerate(inner_tiles):
        offset = tile_height * row_batch
        for tile_grid in row:
            for within_batch_ix, tile_row in enumerate(tile_grid):
                map_row_ix = within_batch_ix + offset
                if len(inner_tiles_merged) <= map_row_ix:
                    inner_tiles_merged.append([])
                inner_tiles_merged[map_row_ix].extend(tile_row)

    seamap = Tile('fullmap', inner_tiles_merged)
    monster_finder = SeamonsterFinder()
    found_monsters = False
    orientation = 0
    while not found_monsters:
        for row in range(len(seamap.grid) - monster_finder.height + 1):
            for col in range(len(seamap.grid[0]) - monster_finder.length + 1):
                if monster_finder.is_seamonster(seamap.grid, row, col):
                    found_monsters = True
                    monster_finder.remove_seamonster(seamap.grid, row, col)
        if not found_monsters:
            orientation += 1
            if orientation == 3:
                seamap.flip_vertical()
            elif orientation >= 8:
                raise RuntimeError('No seamonsters in map!')
            else:
                seamap.rotate_right()

    rough_water_count = 0
    for row in seamap.grid:
        rough_water_count += row.count('#')

    return rough_water_count


def arrange_tiles(tiles):
    for ix, ref_tile in enumerate(tiles):
        while ref_tile.has_free_borders() and ix != len(tiles) - 1:
            ix += 1
            other_tile = tiles[ix]
            if other_tile.has_free_borders():
                ref_tile.align(other_tile)
    return tiles


def load_data(path):
    tiles_data = [[]]
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == '':
                tiles_data.append([])
            else:
                tiles_data[-1].append(line)
    return tiles_data


if __name__ == '__main__':
    main()
