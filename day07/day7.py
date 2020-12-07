# --- Day 7: Handy Haversacks ---

import math


def valid_colors(rules):
    master_keys = set(["shiny gold"])
    sum = len(master_keys)
    prevsum = 0
    bags = 0

    while sum != prevsum:
        prevsum = sum
        for key, val in rules.items():
            if (
                any(a in list(map(lambda x: x[1], val)) for a in list(master_keys))
                and key not in master_keys
            ):
                master_keys.add(key)
                sum = len(master_keys)

    filtered_dict = {
        k: v
        for (k, v) in rules.items()
        if any(a in master_keys for a in list(map(lambda x: x[1], v)))
    }

    return len(filtered_dict)


def count_all(rules, master_key):
    bag_count = 1

    for bag in rules[master_key]:
        if not bag[0] == "no":
            bag_count += int(bag[0]) * count_all(rules, bag[1])
    return bag_count


def number_of_bags(rules):
    master_key = "shiny gold"
    return count_all(rules, master_key) - 1


def parse(line):
    clean = line.replace("bags", "").replace("bag", "")
    keyval = clean.split("contain")
    key = keyval[0].strip()
    val = list(map(str.strip, keyval[1].replace(".", "").split(",")))
    val = list(
        map(
            lambda x: x.split(" ", 1),
            val,
        )
    )
    return [key, val]


if __name__ == "__main__":
    with open("input.txt") as file:
        rules = dict(map(parse, file.read().splitlines()))

        colors = valid_colors(rules)
        bags = number_of_bags(rules)
        print("Problem 1: ", colors)
        print("Problem 2: ", bags)
