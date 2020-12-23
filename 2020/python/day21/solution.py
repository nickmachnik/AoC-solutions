#!/usr/bin/env python


def main():
    data = load_data('puzzleinput.txt')
    print("Answer part one: ", part_one(data))
    print("Answer part two: ", part_two(data))


def part_one(data):
    alg_to_ingr = {}
    ingr_counts = {}
    for ingredients, allergens in data:
        for allergen in allergens:
            if allergen not in alg_to_ingr:
                alg_to_ingr[allergen] = ingredients
            else:
                alg_to_ingr[allergen] = alg_to_ingr[allergen] & ingredients
        for ingredient in ingredients:
            if ingredient not in ingr_counts:
                ingr_counts[ingredient] = 0
            ingr_counts[ingredient] += 1

    ingredients_to_avoid = set().union(*alg_to_ingr.values())

    res = 0
    for ingredient, count in ingr_counts.items():
        if ingredient not in ingredients_to_avoid:
            res += count

    return res


def part_two(data):
    alg_to_ingr = {}
    ingr_counts = {}
    for ingredients, allergens in data:
        for allergen in allergens:
            if allergen not in alg_to_ingr:
                alg_to_ingr[allergen] = ingredients
            else:
                alg_to_ingr[allergen] = alg_to_ingr[allergen] & ingredients
        for ingredient in ingredients:
            if ingredient not in ingr_counts:
                ingr_counts[ingredient] = 0
            ingr_counts[ingredient] += 1

    # sieve
    ingr_to_alg = {}
    algs = list(alg_to_ingr.keys())
    curr_ix = -1
    while len(algs) != 0:
        curr_ix = (curr_ix + 1) % len(algs)
        curr_alg = algs[curr_ix]
        curr_ingr = alg_to_ingr[curr_alg] - ingr_to_alg.keys()
        if len(curr_ingr) == 1:
            ingr_to_alg[curr_ingr.pop()] = curr_alg
            algs.remove(curr_alg)

    return ",".join(sorted(ingr_to_alg, key=lambda x: ingr_to_alg[x]))


def load_data(path):
    data = []
    with open(path, 'r') as fin:
        for line in fin:
            line = line.strip()
            ingredients, allergens = line.split(' (contains ')
            ingredients = ingredients.split()
            allergens = allergens[:-1].split(', ')
            data.append([set(ingredients), set(allergens)])
    return data


if __name__ == '__main__':
    main()
