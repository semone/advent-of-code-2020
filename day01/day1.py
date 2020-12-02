# --- Day 1: Report Repair ---
from itertools import combinations
import math


def fix_report(expenses, numbers_adding_up):
    return math.prod(
        [
            combo
            for combo in combinations(expenses, numbers_adding_up)
            if sum(combo) == 2020
        ][0]
    )


def day1():
    with open("input.txt") as file:
        expenses = list(map(int, file.read().splitlines()))

        print("Problem 1: ", fix_report(expenses, 2))
        print("Problem 2: ", fix_report(expenses, 3))


day1()
