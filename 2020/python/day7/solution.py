#!/usr/bin/env python

from queue import Queue


class Graph:
    class Node:
        def __init__(self):
            # [(node_name, weight)]
            self.in_edges = []
            self.out_edges = []

    def __init__(self):
        # node_name -> Node
        self.nodes = {}

    def add_line_info(self, line):
        parent, rest = line.split(" bags contain ")
        children = []
        for child_string in rest.split(","):
            child_string = child_string.strip().strip('.')
            if child_string == "no other bags":
                continue
            child_string = child_string.split(" bag")[0]
            children.append((int(child_string[0]), child_string[2:]))
        if parent not in self.nodes:
            self.nodes[parent] = Graph.Node()
        for edge_weight, child_name in children:
            self.nodes[parent].out_edges.append((child_name, edge_weight))
            if child_name not in self.nodes:
                self.nodes[child_name] = Graph.Node()
            self.nodes[child_name].in_edges.append((parent, edge_weight))

    def find_all_ancestors(self, start="shiny gold"):
        # we will to bfs, so we need a queue
        q = Queue(maxsize=len(self.nodes))
        q.put(start)
        seen = set()
        while not q.empty():
            curr_node_name = q.get()
            seen.add(curr_node_name)
            curr_node = self.nodes[curr_node_name]
            for (node_name, _) in curr_node.in_edges:
                if node_name not in seen:
                    q.put(node_name)
        return seen

    def sum_inner_bags(self, start_bag):
        if len(self.nodes[start_bag].out_edges) == 0:
            return 0
        return sum(
            weight + weight * self.sum_inner_bags(bag)
            for bag, weight in self.nodes[start_bag].out_edges)


def main():
    pass
    data = load_data("puzzleinput.txt")
    print("Answer part one:", part_one(data))
    print("Answer part two:", part_two(data))


def part_one(graph):
    anc = graph.find_all_ancestors(start="shiny gold")
    return len(anc) - 1


def part_two(graph):
    return graph.sum_inner_bags("shiny gold")


def load_data(path):
    graph = Graph()
    with open(path, 'r') as fin:
        for line in fin:
            line.strip()
            graph.add_line_info(line)
    return graph


if __name__ == '__main__':
    main()
