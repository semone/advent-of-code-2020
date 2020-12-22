# --- Day 19: Monster Messages ---
import re


def parse_input(file):
    return file.read().strip().split("\n\n")


def parse_rules(rules, part2=False):
    rules_dict = {}
    vals = []
    eight = "42 | 42 8"
    eleven = "42 31 | 42 11 31"
    for rule in rules.splitlines():
        key, value = rule.split(": ")
        rules_dict[key] = value.replace('"', "")
        if part2:
            if key == "8":
                rules_dict[key] = eight
            if key == "11":
                rules_dict[key] = eleven

    return rules_dict


def get_regex(rule, rules):
    if rule == "a" or rule == "b":
        return rule
    elif " | " in rule:
        first, second = rule.split(" | ")
        return f"({get_regex(first.strip(),rules)}|{get_regex(second.strip(),rules)})"
    elif " " in rule:
        values = rule.split(" ")
        new_val = ""
        for val in values:
            new_val += get_regex(val, rules)
        return new_val
    else:
        return get_regex(rules[rule], rules)


def with_loops(rules, messages):
    rules = parse_rules(rules, part2=True)

    rule42 = get_regex(rules["42"], rules)
    rule31 = get_regex(rules["31"], rules)

    rule8 = rule42
    matches = set([])
    max_length = 0
    sorted_messages = sorted(messages.split("\n"), key=len)

    for i in range(1, len(sorted_messages[-1])):
        rule11 = f"({rule42}){{{i}}}{rule31}{{{i}}}"
        pattern = f"^({rule8}+)({rule11})$"
        for message in messages.split("\n"):
            if match := re.search(pattern, message):
                matches.add(match)

    return len(matches)


def get_matches(rules, messages):
    rules = parse_rules(rules)

    matches = 0
    match = f"^{get_regex(rules['0'], rules)}$"
    for message in messages.split("\n"):
        if re.search(match, message):
            matches += 1

    return matches


if __name__ == "__main__":
    with open("input.txt") as file:
        rules, messages = parse_input(file)

        print("Problem 1: ", get_matches(rules, messages))
        print("Problem 2: ", with_loops(rules, messages))
