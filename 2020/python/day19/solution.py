#!/usr/bin/env python

import re


class Node:
    def __init__(self):
        self.prerequisites = set()
        self.data = None
        self.children = set()

    def add_prerequisite(self, key):
        self.prerequisites.add(key)

    def remove_prerequisite(self, key):
        self.prerequisites.remove(key)

    def is_independent(self):
        return len(self.prerequisites) == 0

    def add_child(self, key):
        self.children.add(key)

    def overwrite_data(self, data):
        self.data = data

    def replace_key_in_data(self, key, replacement):
        spl = self.data.split()
        for pos, val in enumerate(spl):
            if val == key:
                spl[pos] = replacement
        self.data = " ".join(spl)


def main():
    print("Answer part one:", part_one("puzzleinput.txt"))
    print("Answer part two:", part_two("puzzleinput.txt"))


def part_one(path):
    graph, messages = load_data(path)
    resolve_dependencies(graph)
    if not graph[0].is_independent():
        raise RuntimeError
    pattern = re.compile('^' + graph[0].data.replace(" ", '') + '$')
    valid = 0
    for message in messages:
        if re.match(pattern, message) is not None:
            valid += 1
    return valid


def part_two(path):
    # this part adds potential infinite strings of 42 rules
    # or n 42 + n 32 rules (by rule 8 and 11).
    # fortunately, it seems that 8 and 11 are the direct prerequisites for 0.
    graph, messages = load_data(path)
    resolve_dependencies(graph)
    if not graph[0].is_independent():
        raise RuntimeError
    p42 = re.compile('^([' + graph[42].data.replace(" ", '') + ']{2,})')
    p31 = re.compile('([' + graph[31].data.replace(" ", '') + ']+)$')
    fullp = re.compile(p42.pattern + p31.pattern)
    print(fullp.pattern)
    valid = 0
    for message in messages:
        if re.match(fullp, message) is not None:
            valid += 1
    return valid


def load_data(path):
    with open(path, 'r') as fin:
        graph_lines = []
        for line in fin:
            line = line.strip()
            if line == "":
                break
            graph_lines.append(line)
        messages = []
        for line in fin:
            line = line.strip()
            messages.append(line)
    return load_dependency_graph(graph_lines), messages


def load_dependency_graph(lines):
    graph = {}
    for line in lines:
        key, rule_str = line.split(':')
        key = int(key)
        if key not in graph:
            graph[key] = Node()
        for e in rule_str.split():
            isroot = True
            if e.isdigit():
                isroot = False
                e = int(e)
                graph[key].add_prerequisite(e)
                if e not in graph:
                    graph[e] = Node()
                graph[e].add_child(key)
        if isroot:
            graph[key].overwrite_data(rule_str.replace('"', ''))
        else:
            graph[key].overwrite_data('( ' + rule_str + ' )')
    return graph


def resolve_dependencies(graph):
    independent = [
        (key, node) for key, node in graph.items() if node.is_independent()]
    while len(independent) > 0:
        curr_key, curr_node = independent.pop()
        for child_key in curr_node.children:
            child = graph[child_key]
            child.replace_key_in_data(str(curr_key), curr_node.data)
            child.remove_prerequisite(curr_key)
            if child.is_independent():
                independent.append((child_key, child))
    if not graph[0].is_independent():
        return False
    return True


if __name__ == '__main__':
    main()
