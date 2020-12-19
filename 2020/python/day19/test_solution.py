from solution import load_data, resolve_dependencies, part_one, part_two


def test_resolving():
    graph, messages = load_data("test_input.txt")
    resolve_dependencies(graph)
    assert graph[0].is_independent()


def test_part_one():
    assert part_one("test_input.txt") == 2


def test_part_two():
    assert part_one("test_input2.txt") == 3
    assert part_two("test_input2.txt") == 12
    # graph, messages = load_data("test_input2.txt")
    # resolve_dependencies(graph)
    # print(graph[8].data.replace(' ', ''))
    # print(graph[11].data.replace(' ', ''))
    # print(graph[0].data.replace(' ', ''))
    # assert None is not None
