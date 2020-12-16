# --- Day 16: Ticket Translation ---

import itertools
import math


def strip_dowm(v, taken):
    cp = v

    for key, val in v.items():
        if len(val) == 1:
            taken.append(val[0])
        else:
            j = list(filter(lambda y: y not in taken, val))
            cp[key] = j

    if any(len(x) > 1 for x in cp.values()):
        return strip_dowm(cp, taken)
    else:
        return cp


if __name__ == "__main__":
    with open("input.txt") as file:
        valid = {}
        invalid = []

        prev_line = ""
        check_with = set([])
        my_ticket = ""
        for line in file:
            if ": " in line:
                values = line.strip().split(": ", 1)[1].split(" or ")
                key = line.strip().split(": ", 1)[0]

                tmp_vals_1 = list(map(int, values[0].split("-")))
                tmp_vals_2 = list(map(int, values[1].split("-")))
                v = []
                for i in range(tmp_vals_1[0], tmp_vals_1[1] + 1):
                    v.append(i)

                for i in range(tmp_vals_2[0], tmp_vals_2[1] + 1):
                    v.append(i)

                valid[key] = v
            else:
                if prev_line == "your ticket:":
                    my_ticket = line.strip()
                    prev_line = ""
                if prev_line == "nearby tickets:":
                    vals = list(map(int, line.strip().split(",")))
                    all_valid = set(itertools.chain.from_iterable(list(valid.values())))
                    if all(x in all_valid for x in vals):
                        check_with.add(line.strip())
                    for val in vals:
                        if not val in all_valid:
                            invalid.append(val)
                if "ticket" in line:
                    prev_line = line.strip()

        t = {}
        for ticket in check_with:
            b = {}
            for index, vl in enumerate(map(int, ticket.split(","))):
                for key, val in valid.items():
                    if vl in val:
                        if index in b:
                            b[index].append(key)
                        else:
                            b[index] = [key]

            for key, val in b.items():
                if key in t:
                    h = list(set(val).intersection(t[key]))
                    t[key] = h
                else:
                    t[key] = set(val)

        indicies = []
        l = strip_dowm(t, [])
        for key, val in l.items():
            if "departure" in val[0]:
                indicies.append(key)

        numbers = map(int, [my_ticket.strip().split(",")[i] for i in indicies])

        print("Problem 1: ", sum(invalid))
        print("Problem 2: ", math.prod(numbers))
