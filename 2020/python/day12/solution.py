#!/usr/bin/env python


DIRECTIONS = ["N", "E", "S", "W"]


def main():
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def rotate_ship(
    current_direction,
    rotation_direction,
    rotation_amount
):
    curr_ix = DIRECTIONS.index(current_direction)
    steps = rotation_amount // 90
    if rotation_direction == 'R':
        new_ix = (curr_ix + steps) % 4
    else:
        new_ix = (curr_ix - steps) % 4
    return DIRECTIONS[new_ix]


def part_one(instructions):
    ship_direction = "E"
    # horizontal position
    x_pos = 0
    # vertical position
    y_pos = 0
    for direction, amount in instructions:
        if direction == 'F':
            direction = ship_direction

        if direction == 'E':
            x_pos += amount
        elif direction == 'W':
            x_pos -= amount
        elif direction == 'N':
            y_pos -= amount
        elif direction == 'S':
            y_pos += amount
        elif direction == 'L' or direction == 'R':
            if amount % 90 != 0:
                raise ValueError(
                    "Received turn amount: {}".format(amount))
            ship_direction = rotate_ship(ship_direction, direction, amount)
        else:
            raise ValueError("Unknown input instruction: {}".format(direction))
    return abs(x_pos) + abs(y_pos)


def rotate_waypoint(waypoint_x, waypoint_y, direction, amount):
    waypoint = [0, 0, 0, 0]
    if waypoint_y > 0:
        waypoint[2] = waypoint_y
    else:
        waypoint[0] = abs(waypoint_y)
    if waypoint_x > 0:
        waypoint[1] = waypoint_x
    else:
        waypoint[3] = abs(waypoint_x)
    new_waypoint = [0, 0, 0, 0]
    steps = amount // 90
    if direction == 'R':
        for i, e in enumerate(waypoint):
            new_waypoint[(i + steps) % 4] = e
    else:
        for i, e in enumerate(waypoint):
            new_waypoint[(i - steps) % 4] = e
    new_x = new_waypoint[1] if new_waypoint[3] == 0 else -new_waypoint[3]
    new_y = -new_waypoint[0] if new_waypoint[2] == 0 else new_waypoint[2]
    return new_x, new_y


def part_two(instructions):
    # N, E, S, W
    waypoint_x, waypoint_y = 10, -1
    x_pos, y_pos = 0, 0
    for instruction, amount in instructions:
        if instruction == 'F':
            # move ship in waypoint direction
            y_pos += waypoint_y * amount
            x_pos += waypoint_x * amount
        elif instruction == 'E':
            waypoint_x += amount
        elif instruction == 'W':
            waypoint_x -= amount
        elif instruction == 'N':
            waypoint_y -= amount
        elif instruction == 'S':
            waypoint_y += amount
        elif instruction == 'L' or instruction == 'R':
            if amount % 90 != 0:
                raise ValueError(
                    "Received turn amount: {}".format(amount))
            waypoint_x, waypoint_y = rotate_waypoint(
                waypoint_x, waypoint_y, instruction, amount)
        else:
            raise ValueError(
                "Unknown input instruction: {}".format(instruction))
    return abs(x_pos) + abs(y_pos)


def load_data(path):
    instructions = []
    with open(path, 'r') as fin:
        for line in fin:
            line.strip()
            direction, amount = line[0], int(line[1:])
            instructions.append((direction, amount))
    return instructions


if __name__ == '__main__':
    main()
