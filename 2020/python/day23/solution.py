#!/usr/bin/env python

class CircularArray:
    class Node:
        def __init__(self, arr):
            self.arr = arr
            self.nxt = None
            self.prv = None
            self.val = None
            self.dst = None

        def set_val(self, val):
            self.val = val

        def set_nxt(self, nxt):
            self.nxt = nxt

        def set_prv(self, prv):
            self.prv = prv

        def set_dst(self, dst):
            self.dst = dst

        def find_dest(self):
            dest_val = self.arr.max if self.val == 1 else self.val - 1
            cand_down = self.prv
            cand_up = self.nxt
            while cand_down.val != dest_val and cand_up.val != dest_val:
                cand_down = cand_down.prv
                cand_up = cand_up.nxt
            self.dst = cand_down if cand_down.val == dest_val else cand_up

    def __init__(self, numstr):
        self.curr_cup = None
        self.cycled = 0
        self.max = 0
        prev = None
        for num in numstr:
            prev = self.insert_after(prev, int(num))

    def find_dests(self):
        curr_cup = self.curr_cup
        curr_cup.find_dest()
        curr_cup = curr_cup.nxt
        while curr_cup != self.curr_cup:
            curr_cup.find_dest()
            curr_cup = curr_cup.nxt

    def insert_after(self, prev, val):
        new = CircularArray.Node(self)
        new.set_val(val)
        if prev is None:
            new.set_nxt(new)
            new.set_prv(new)
            self.curr_cup = new
            self.prev_dest = new
        else:
            new.set_nxt(prev.nxt)
            new.nxt.set_prv(new)
            new.set_prv(prev)
            prev.set_nxt(new)
        if val == 1:
            self.one = new
        if self.max < val:
            self.max = val
        return new

    def __repr__(self):
        res = [str(self.curr_cup.val)]
        curr_cup = self.curr_cup.nxt
        while curr_cup.val != self.curr_cup.val:
            res.append(str(curr_cup.val))
            curr_cup = curr_cup.nxt
        return "".join(res)

    def cycle(self):
        pu_start = self.curr_cup.nxt
        pu_mid = pu_start.nxt
        pu_end = pu_mid.nxt
        pu = set([pu_start, pu_mid, pu_end])
        dest = self.curr_cup.dst
        while dest in pu:
            for node in pu:
                if node is dest:
                    dest = node.dst

        self.curr_cup.set_nxt(pu_end.nxt)
        pu_end.nxt.set_prv(self.curr_cup)

        pu_end.set_nxt(dest.nxt)
        dest.nxt.set_prv(pu_end)

        dest.set_nxt(pu_start)
        pu_start.set_prv(dest)

        self.prev_dest = dest
        self.curr_cup = self.curr_cup.nxt

        self.cycled += 1


def main():
    mystr = "523764819"
    print("Answer part one: ", part_one(mystr))
    print("Answer part two: ", part_two(mystr))


def part_one(numstr):
    carr = CircularArray(numstr)
    carr.find_dests()

    for i in range(100):
        carr.cycle()

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


def part_two(numstr):
    max_num = 10 ** 6
    carr = CircularArray(numstr)
    prev = carr.curr_cup
    for i in range(8):
        prev = prev.nxt
    for num in range(10, max_num + 1):
        prev = carr.insert_after(prev, num)
    carr.find_dests()

    for i in range(max_num * 10):
        carr.cycle()

    return carr.one.nxt.val * carr.one.nxt.nxt.val


if __name__ == '__main__':
    main()
