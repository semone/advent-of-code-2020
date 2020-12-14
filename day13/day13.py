# --- Day 13: Shuttle Search ---

import math


def get_closest_departure(earliest, bus):
    max = earliest / bus
    return math.ceil(max) * bus


def get_earliest_departure(input):
    earliest = input[0]
    buses = input[1].replace("x,", "").split(",")

    times = []

    for bus in buses:
        surr = get_closest_departure(int(earliest), int(bus))
        times.append(surr)

    time_differences = list(map(lambda x: x - int(earliest), times))

    minimum_time_difference = int(min(time_differences))
    return minimum_time_difference * int(
        buses[time_differences.index(minimum_time_difference)]
    )


def get_earliest_timestamp(buses):
    relevant_buses = map(int, (buses.replace("x,", "").split(",")))
    relevant_buses_index = [
        index for index, value in enumerate(buses.split(",")) if value != "x"
    ]

    t = 0
    step = 1
    for bus, index in zip(relevant_buses, relevant_buses_index):
        while (t + index) % bus:
            t += step
        step *= bus

    return t


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()

        print("Problem 1: ", get_earliest_departure(input))
        print("Problem 2: ", get_earliest_timestamp(input[1]))
