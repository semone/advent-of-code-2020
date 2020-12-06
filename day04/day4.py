# --- Day 4: Passport Processing ---
import re


def has_required_fields(fields):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return set(required_fields).issubset(fields)


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return False


def is_valid_field(field):
    key, value = field
    valid_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def hgt(value):
        match = re.match(r"([0-9]+)([a-z]+)", value, re.I)
        if match:
            items = match.groups()
            return (
                items[1] == "cm" and int(items[0]) >= 150 and int(items[0]) <= 193
            ) or (items[1] == "in" and int(items[0]) >= 59 and int(items[0]) <= 76)

        else:
            return False

    valid = {
        "byr": lambda value: int(value) >= 1920 and int(value) <= 2002,
        "iyr": lambda value: int(value) >= 2010 and int(value) <= 2020,
        "eyr": lambda value: int(value) >= 2020 and int(value) <= 2030,
        "hcl": lambda value: value[0] == "#"
        and len(value[1:]) == 6
        and bool(re.match("^[a-f0-9]*$", value[1:])),
        "hgt": lambda value: hgt(value),
        "ecl": lambda value: value in valid_eyes,
        "pid": lambda value: intTryParse(value) and len(value) == 9,
        "cid": lambda value: True,
    }[key](value)

    return valid


def has_valid_fields(fields):
    return all(is_valid_field(field) for field in fields)


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().split("\n\n")
        sum_required_fields = 0
        sum_valid_fields = 0

        for entries in input:
            fields = re.split("\s|\n", entries)
            sets = list(map(lambda ent: (ent.split(":", 1)), fields))
            keys = list(map(lambda ent: ent[0], sets))

            if has_required_fields(keys):
                sum_required_fields += 1

                if has_valid_fields(sets):
                    sum_valid_fields += 1

        print("Problem 1: ", sum_required_fields)
        print("Problem 2: ", sum_valid_fields)