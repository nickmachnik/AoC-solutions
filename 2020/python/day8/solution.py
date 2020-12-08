#!/usr/bin/env python


class BootCodeComputer:
    def __init__(self, path):
        self.head = 0
        self.load_instructions(path)
        self.accumulator = 0

    def load_instructions(self, path):
        self.instructions = []
        with open(path, 'r') as fin:
            for line in fin:
                operation, argument = line.strip().split()
                self.instructions.append((operation, int(argument)))

    def execute_cell(self):
        op, arg = self.instructions[self.head]
        if op == "nop":
            self.head += 1
        elif op == "acc":
            self.accumulator += arg
            self.head += 1
        elif op == "jmp":
            self.head += arg
        else:
            raise ValueError(
                "Unknown opcode in instruction: {}".format((op, arg)))
        # code terminates
        if self.head >= len(self.instructions):
            return 0


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    comp = BootCodeComputer(path)
    instr_counter = [0] * len(comp.instructions)
    while True:
        if instr_counter[comp.head] > 0:
            return comp.accumulator
        instr_counter[comp.head] += 1
        comp.execute_cell()


def part_two(path):
    jmp_or_nop = []
    comp = BootCodeComputer(path)
    for i, (op, _) in enumerate(comp.instructions):
        if op == 'jmp' or op == 'nop':
            jmp_or_nop.append(i)

    for swap_pos in jmp_or_nop:
        comp = BootCodeComputer(path)
        instr_counter = [0] * len(comp.instructions)
        # swap instruction
        op, arg = comp.instructions[swap_pos]
        op = 'jmp' if op == 'nop' else 'nop'
        comp.instructions[swap_pos] = (op, arg)
        while True:
            if instr_counter[comp.head] > 0:
                break
            instr_counter[comp.head] += 1
            exit_code = comp.execute_cell()
            if exit_code == 0:
                # we terminated!
                return comp.accumulator


if __name__ == '__main__':
    main()
