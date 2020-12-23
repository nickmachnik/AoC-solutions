#!/usr/bin/env python

class CircularArray:
    class Node:
        def __init__(self):
            self.nxt = None
            self.val = None

        def set_val(self, val):
            self.val = val

        def set_nxt(self, nxt):
            self.nxt = nxt

    def __init__(self, numstr):
        prev = None
        for num in numstr:
            prev = self.insert_after(prev, int(num))

    def insert_after(self, prev, val):
        new = CircularArray.Node()
        new.set_val(val)
        if prev is None:
            new.set_nxt(new)
            self.curr_cup = new
        else:
            new.set_nxt(prev.nxt)
            prev.set_nxt(new)
        return new

    def __repr__(self):
        res = [str(self.curr_cup.val)]
        curr_cup = self.curr_cup.nxt
        while curr_cup.val != self.curr_cup.val:
            res.append(str(curr_cup.val))
            curr_cup = curr_cup.nxt
        return "".join(res)


def main():
    mystr = "523764819"
    print("Answer part one: ", part_one(mystr))
    print("Answer part two: ", part_two(mystr))


def part_one(numstr):
    carr = CircularArray(numstr)
    for i in range(100):
        dest_val = 9 if carr.curr_cup.val == 1 else carr.curr_cup.val - 1
        pu_start = carr.curr_cup.nxt
        pu_mid = pu_start.nxt
        pu_end = pu_mid.nxt
        pu_vals = set([pu_start.val, pu_mid.val, pu_end.val])
        while dest_val in pu_vals:
            dest_val -= 1
            if dest_val == 0:
                dest_val = 9
        # find destination cup
        dest_cup = pu_end.nxt
        while dest_cup.val != dest_val:
            dest_cup = dest_cup.nxt
        carr.curr_cup.nxt = pu_end.nxt
        pu_end.nxt = dest_cup.nxt
        dest_cup.nxt = pu_start
        carr.curr_cup = carr.curr_cup.nxt

    # find cup one
    curr_cup = carr.curr_cup
    while curr_cup.val != 1:
        curr_cup = curr_cup.nxt

    order = []
    curr_cup = curr_cup.nxt
    while curr_cup.val != 1:
        order.append(str(curr_cup.val))
        curr_cup = curr_cup.nxt

    return "".join(order)


def part_two(data):
    pass


if __name__ == '__main__':
    main()
