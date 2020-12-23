#!/usr/bin/env python

from collections import deque
import itertools


def main():
    data = load_data('puzzleinput.txt')
    print("Answer part one: ", part_one(data))
    data = load_data('puzzleinput.txt')
    print("Answer part two: ", part_two(data))


def play_combat(deck1, deck2):
    while True:
        if len(deck1) == 0:
            return deck2
        elif len(deck2) == 0:
            return deck1
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)
        else:
            ValueError("Tie in combat, oh no!")


def play_recursive_combat(deck1, deck2):
    mem = [set(), set()]
    while True:
        if tuple(deck1) in mem[0] or tuple(deck2) in mem[1]:
            return 0, deck1
        elif len(deck1) == 0:
            return 1, deck2
        elif len(deck2) == 0:
            return 0, deck1
        mem[0].add(tuple(deck1))
        mem[1].add(tuple(deck2))
        card1, card2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner, _deck = play_recursive_combat(
                deque(itertools.islice(deck1, 0, card1)),
                deque(itertools.islice(deck2, 0, card2))
                )
            if winner == 0:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        elif card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)
        else:
            ValueError("Tie in combat, oh no!")


def score_deck(deck):
    mul = len(deck)
    score = 0
    while not len(deck) == 0:
        score += deck.popleft() * mul
        mul -= 1
    return score


def part_one(data):
    return score_deck(play_combat(*data))


def part_two(data):
    _winner, winner_deck = play_recursive_combat(*data)
    return score_deck(winner_deck)


def load_data(path):
    data = [deque()]
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line.startswith("Player"):
                continue
            elif line == "":
                data.append(deque())
            else:
                data[-1].append(int(line))
    return data


if __name__ == '__main__':
    main()
