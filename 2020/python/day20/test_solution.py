from solution import part_one, load_data, Tile, arrange_tiles, part_two


def test_part_one():
    tiles = [
        Tile(int(lines[0].split()[1][:-1]), lines[1:])
        for lines in load_data('test_input.txt')]
    tiles = arrange_tiles(tiles)
    assert part_one(tiles) == 20899048083289


def test_part_two():
    tiles = [
        Tile(int(lines[0].split()[1][:-1]), lines[1:])
        for lines in load_data('test_input.txt')]
    tiles = arrange_tiles(tiles)
    assert part_two(tiles) == 273
