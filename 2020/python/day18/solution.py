#!/usr/bin/env python

import operator as op


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    s = 0
    with open(path, 'r') as fin:
        for line in fin:
            s += evaluate_expression(line.strip())
    return s


def part_two(path):
    pass


def evaluate_expression(expr_str, index=0):
    value = 0
    operator = op.add
    while index < len(expr_str):
        char = expr_str[index]
        # the expressions have only single digit numbers
        if char.isdigit():
            value = operator(value, int(char))
        elif char == '+':
            operator = op.add
        elif char == '*':
            operator = op.mul
        elif char == '(':
            par_value, index = evaluate_expression(expr_str, index + 1)
            value = operator(value, par_value)
        elif char == ')':
            return value, index
        elif char == ' ':
            pass
        else:
            raise ValueError("Unexpected char in input: {}".format(char))
        index += 1
    return value


if __name__ == '__main__':
    main()
