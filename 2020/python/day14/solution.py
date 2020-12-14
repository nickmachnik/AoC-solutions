#!/usr/bin/env python

from itertools import product


def main():
    instructions = load_data('puzzleinput.txt')
    print("Answer part one:", part_one(instructions))
    print("Answer part two:", part_two(instructions))


def make_zero_and_one_bitmasks(mask_string):
    set_zero = (1 << 36) - 1
    set_one = 0
    for i, s in enumerate(mask_string):
        v = 35 - i
        if s == '1':
            set_one += 1 << v
        if s == '0':
            set_zero -= 1 << v
    return set_zero, set_one


def make_floating_bitmasks(mask_string):
    base_mask = 0
    floating_bits = []
    for i, s in enumerate(mask_string):
        v = 35 - i
        if s == 'X':
            floating_bits.append(v)
        if s == '1':
            base_mask += 1 << v
    floating_masks = []
    for bit_combination in product([0, 1], repeat=len(floating_bits)):
        one_mask = base_mask
        zero_mask = (1 << 36) - 1
        for bit_position, bit in zip(floating_bits, bit_combination):
            if bit == 1:
                one_mask |= 1 << bit_position
            else:
                zero_mask -= 1 << bit_position
        floating_masks.append((zero_mask, one_mask))
    return floating_masks


def part_one(instructions):
    zero_mask = 0
    one_mask = 0
    mem = {}
    for instruction in instructions:
        if type(instruction) is tuple:
            k, v = instruction
            v = (v & zero_mask) | one_mask
            mem[k] = v
        else:
            zero_mask, one_mask = make_zero_and_one_bitmasks(instruction)
    return sum(mem.values())


def part_two(instructions):
    floating_masks = []
    mem = {}
    for instruction in instructions:
        if type(instruction) is tuple:
            k, v = instruction
            for zero_mask, one_mask in floating_masks:
                new_address = (k & zero_mask) | one_mask
                mem[new_address] = v
        else:
            floating_masks = make_floating_bitmasks(instruction)
    return sum(mem.values())


def load_data(path):
    instructions = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line.startswith('mem'):
                mem_loc, value = line[4:].split('] = ')
                instructions.append((int(mem_loc), int(value)))
            else:
                instructions.append(line[7:])
    return instructions


if __name__ == '__main__':
    main()
