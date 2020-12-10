# --- Day 10: Adapter Array ---
from itertools import groupby
import math


def connect_all(jolts):
    built_in_joltage_adapter = max(jolts) + 3
    effective_rating = 0
    differences = []

    paths = {
        4: 7,
        3: 4,
        2: 2,
        1: 1,
    }

    for jolt in jolts:
        valid_jolts = list(
            filter(
                lambda x: x
                in [effective_rating + 1, effective_rating + 2, effective_rating + 3],
                jolts,
            )
        )
        differences.append(min(valid_jolts) - effective_rating)
        effective_rating = min(valid_jolts)

    differences.append(built_in_joltage_adapter - effective_rating)

    groups = [
        list(group) for k, group in groupby(differences, lambda x: x == 3) if not k
    ]

    group_sums = list(map(lambda x: paths[x], (map(lambda x: sum(x), groups))))

    return (
        sum(1 for i in differences if i == 1) * sum(1 for i in differences if i == 3),
        math.prod(group_sums),
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        jolts = list(map(int, file.read().splitlines()))
        part1, part2 = connect_all(jolts)
        print("Problem 1: ", part1)
        print("Problem 2: ", part2)
