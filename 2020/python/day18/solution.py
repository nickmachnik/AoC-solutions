#!/usr/bin/env python

import operator as op
import math


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    s = 0
    with open(path, 'r') as fin:
        for line in fin:
            s += evaluate_expression_basic(line.strip())
    return s


def part_two(path):
    s = 0
    with open(path, 'r') as fin:
        for line in fin:
            s += evaluate_expression_advanced(line.strip())
    return s


def evaluate_expression_basic(expr_str, index=0):
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
            par_value, index = evaluate_expression_basic(expr_str, index + 1)
            value = operator(value, par_value)
        elif char == ')':
            return value, index
        elif char == ' ':
            pass
        else:
            raise ValueError("Unexpected char in input: {}".format(char))
        index += 1
    return value


def evaluate_expression_advanced(expr_str, index=0):
    new_expression = []
    operator = op.mul
    while index < len(expr_str):
        char = expr_str[index]
        if char.isdigit():
            if operator is op.add:
                new_expression[-1] += int(char)
            else:
                new_expression.append(int(char))
        elif char == '+':
            operator = op.add
        elif char == '*':
            operator = op.mul
        elif char == '(':
            par_value, index = evaluate_expression_advanced(
                expr_str, index + 1)
            if operator is op.add:
                new_expression[-1] += par_value
            else:
                new_expression.append(par_value)
        elif char == ')':
            return math.prod(new_expression), index
        elif char == ' ':
            pass
        else:
            raise ValueError("Unexpected char in input: {}".format(char))
        index += 1
    return math.prod(new_expression)


if __name__ == '__main__':
    main()
