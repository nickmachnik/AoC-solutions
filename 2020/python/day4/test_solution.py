from solution import part_one, part_two, load_data, key_constraints
import re


def test_loading():
    test_input = load_data("testdata.txt")
    assert len(test_input) == 4


def test_part_one():
    assert part_one(load_data("testdata.txt")) == 2


def test_matching():
    # byr
    assert re.match(key_constraints['byr'], "2020") is None
    assert re.match(key_constraints['byr'], "2002") is not None

    # iyr
    assert re.match(key_constraints['iyr'], "1900") is None
    assert re.match(key_constraints['iyr'], "2010") is not None

    # eyr
    assert re.match(key_constraints['eyr'], "2031") is None
    assert re.match(key_constraints['eyr'], "2030") is not None

    # hgt
    assert re.match(key_constraints['hgt'], "3in") is None
    assert re.match(key_constraints['hgt'], "60in") is not None
    assert re.match(key_constraints['hgt'], "100cm") is None
    assert re.match(key_constraints['hgt'], "150cm") is not None

    # hgt
    assert re.match(key_constraints['hcl'], "dab227") is None
    assert re.match(key_constraints['hcl'], "#a97842") is not None

    assert re.match(key_constraints['byr'], "2002") is not None
    assert re.match(key_constraints['byr'], "2003") is None
    assert re.match(key_constraints['hgt'], "60in") is not None
    assert re.match(key_constraints['hgt'], "190cm") is not None
    assert re.match(key_constraints['hgt'], "190in") is None
    assert re.match(key_constraints['hgt'], "190") is None
    assert re.match(key_constraints['hcl'], "#123abc") is not None
    assert re.match(key_constraints['hcl'], "#123abz") is None
    assert re.match(key_constraints['hcl'], "123abc") is None
    assert re.match(key_constraints['ecl'], "brn") is not None
    assert re.match(key_constraints['ecl'], "wat") is None
    assert re.match(key_constraints['pid'], "000000001") is not None
    assert re.match(key_constraints['pid'], "0123456789") is None


def test_part_two():
    assert part_two(load_data("invalid_test.txt")) == 0
    assert part_two(load_data("valid_test.txt")) == 4
