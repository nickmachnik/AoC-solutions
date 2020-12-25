#!/usr/bin/env python

from collections import deque

def main():
    directions = load_directions('puzzleinput.txt')
    print("Answer part one: ", part_one(directions))
    print("Answer part two: ", part_two(directions))


def part_one(directions):
    black_tiles = initiate_board(directions)
    return len(black_tiles)


def initiate_board(directions):
    black_tiles = set()
    for direction in directions:
        target_tile = read_direction(direction)
        if target_tile in black_tiles:
            black_tiles.remove(target_tile)
        else:
            black_tiles.add(target_tile)
    return black_tiles


def part_two(directions):
    black_tiles = initiate_board(directions)
    for i in range(100):
        q = deque()
        for tile in black_tiles:
            q.appendleft(tile)
        queued = black_tiles.copy()
        new_black_tiles = set()
        while len(q) != 0:
            tile = q.pop()
            black_adjacent = 0
            for neighbor in adjacent_tiles(*tile):
                if neighbor in black_tiles:
                    black_adjacent += 1
                if tile in black_tiles and neighbor not in queued:
                    queued.add(neighbor)
                    q.appendleft(neighbor)
            if tile in black_tiles and 1 <= black_adjacent <= 2:
                new_black_tiles.add(tile)
            elif tile not in black_tiles and black_adjacent == 2:
                new_black_tiles.add(tile)
        black_tiles = new_black_tiles
    return len(black_tiles)


def adjacent_tiles(x, y):
    return [
        (x - 2, y), (x + 2, y), (x + 1, y + 1),
        (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]


def load_directions(path):
    directions = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            directions.append(line)
    return directions


def read_direction(line):
    x, y = 0, 0
    pos = 0
    while pos < len(line):
        char = line[pos]
        if char == 'e':
            x += 2
            pos += 1
        elif char == 'w':
            x -= 2
            pos += 1
        else:
            nxt_char = line[pos + 1]
            x = x + 1 if nxt_char == 'e' else x - 1
            y = y + 1 if char == 'n' else y - 1
            pos += 2
    return x, y


if __name__ == '__main__':
    main()
