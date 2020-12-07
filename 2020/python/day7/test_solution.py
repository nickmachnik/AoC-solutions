from solution import part_one, load_data, part_two


def test_part_one():
    graph = load_data("test_input.txt")
    for node_name, node in graph.nodes.items():
        print(node_name, node.in_edges)
    assert part_one(graph) == 4


def test_part_two():
    graph = load_data("test_input.txt")
    for node_name, node in graph.nodes.items():
        print(node_name, node.out_edges)
    assert part_two(graph) == 32

    graph = load_data("test_input2.txt")
    for node_name, node in graph.nodes.items():
        print(node_name, node.out_edges)
    assert part_two(graph) == 126
