#!/usr/bin/env python


DIRECTIONS = [
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # down
    (-1, 0),  # up
    (1, 1),  # down right
    (1, -1),  # down left
    (-1, -1),  # up left
    (-1, 1)  # up left
]


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    room = WaitingRoom(path)
    room.fill_and_free_seats(room._get_num_occupied_neighboring_seats, 4)
    return room.num_occupied_seats


def part_two(path):
    room = WaitingRoom(path)
    room.fill_and_free_seats(room._get_num_occupied_in_sight, 5)
    return room.num_occupied_seats


class WaitingRoom:
    def __init__(self, path):
        self._load_layout(path)
        self.num_occupied_seats = 0

    def _load_layout(self, path):
        self.room = []
        with open(path, 'r') as fin:
            for line in fin:
                self.room.append(list(line.strip()))
        self.nrows = len(self.room)
        self.ncols = len(self.room[0])

    def fill_and_free_seats(
        self,
        neighbor_count_function,
        seat_free_thr
    ):
        while True:
            fill = []
            free = []
            for i in range(self.nrows):
                for j in range(self.ncols):
                    curr_state = self.room[i][j]
                    if curr_state == ".":
                        continue
                    full_neighbors = \
                        neighbor_count_function(i, j)
                    if curr_state == "#" and full_neighbors >= seat_free_thr:
                        free.append((i, j))
                    elif curr_state == 'L' and full_neighbors == 0:
                        fill.append((i, j))
            if len(fill) == len(free) == 0:
                return
            for i, j in fill:
                self.room[i][j] = '#'
                self.num_occupied_seats += 1
            for i, j in free:
                self.room[i][j] = 'L'
                self.num_occupied_seats -= 1

    def _get_num_occupied_neighboring_seats(self, row, col):
        occupied_count = 0
        for i in range(row - 1, row + 2):
            if i < 0 or i >= self.nrows:
                continue
            for j in range(col - 1, col + 2):
                if (j < 0 or j >= self.ncols) or (i == row and j == col):
                    continue
                if self.room[i][j] == '#':
                    occupied_count += 1
        return occupied_count

    def _get_num_occupied_in_sight(self, row, col):
        occupied_count = 0
        for di, dj in DIRECTIONS:
            curr_row, curr_col = row + di, col + dj
            while self.is_in_room(curr_row, curr_col):
                if self.room[curr_row][curr_col] == 'L':
                    break
                elif self.room[curr_row][curr_col] == '#':
                    occupied_count += 1
                    break
                else:
                    curr_row += di
                    curr_col += dj
        return occupied_count

    def is_in_room(self, row, col):
        if row < 0 or row >= self.nrows:
            return False
        if col < 0 or col >= self.ncols:
            return False
        return True


if __name__ == '__main__':
    main()
