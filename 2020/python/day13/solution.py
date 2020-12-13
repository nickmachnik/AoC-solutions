#!/usr/bin/env python


def main():
    arrival_time, bus_times = load_data('puzzleinput.txt')
    print("Answer part one:", part_one(arrival_time, bus_times))
    print("Answer part two:", part_two(bus_times))


def part_one(arrival_time, bus_times):
    bus_id = None
    waiting_time = None
    for bus_time in bus_times:
        if bus_time == 'x':
            continue
        curr_waiting_time = bus_time - (arrival_time % bus_time)
        if waiting_time is None or waiting_time > curr_waiting_time:
            bus_id = bus_time
            waiting_time = curr_waiting_time
    return bus_id * waiting_time


def part_two(bus_times):
    time = 0
    step = 1
    for offset, bus_period in enumerate(bus_times):
        if bus_period == 'x':
            continue
        # increase time until we satisfy the offset for the current bus.
        while (time + offset) % bus_period != 0:
            time += step
        # make step a multiple of the current bus period;
        # this ensures that all following time increments will also satisfy
        # the modulo condition.
        step *= bus_period
    return time


def load_data(path):
    with open(path, 'r') as fin:
        arrival_time = int(next(fin).strip())
        bus_times = [int(e) if e != 'x' else 'x' for e in next(fin).split(',')]
    return arrival_time, bus_times


if __name__ == '__main__':
    main()
