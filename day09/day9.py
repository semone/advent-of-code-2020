# --- Day 9: Encoding Error ---

from itertools import combinations


def check(preamble_length, series):
    start = 0
    preamble = series[:preamble_length]
    for i in range(preamble_length, len(series)):

        preamble = series[start:i]
        start += 1

        if (
            len(
                [
                    combo
                    for combo in combinations(preamble, 2)
                    if sum(combo) == series[i]
                ]
            )
            == 0
        ):
            return series[i]


def contiguous_sequece(goal_number, series):
    total_numbers = len(series)
    for i in range(total_numbers):
        total_sum = series[i]
        for index in range(i + 1, total_numbers):
            if total_sum == goal_number:
                sub_list = series[i:index]
                return min(sub_list) + max(sub_list)
            if total_sum > goal_number:
                continue
            total_sum += series[index]

    print("No sequence found")
    return 0


if __name__ == "__main__":
    with open("input.txt") as file:
        series = list(map(int, file.read().splitlines()))

        goal_number = check(25, series)

        print("Problem 1: ", goal_number)
        print("Problem 2: ", contiguous_sequece(goal_number, series))
