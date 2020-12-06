# --- Day 3: Toboggan Trajectory ---
import math


def encountered_trees(slopes, woods_map):
    width = len(woods_map[0])
    trees = [0] * len(slopes)

    for index, slope in enumerate(slopes):
        position = (0, 0)
        right = slope[0]
        down = slope[1]
        while position[1] < len(woods_map) - 1:
            position = ((position[0] + right) % width, position[1] + down)

            if woods_map[position[1]][position[0]] == "#":
                trees[index] += 1

    return trees


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()

        part1 = encountered_trees([(3, 1)], input)[0]
        part2 = math.prod(
            encountered_trees([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], input)
        )

        print("Problem 1: ", part1)
        print("Problem 2: ", part2)