# --- Day 18: Operation Order ---
import operator
import re

ops = {
    "+": operator.add,
    "*": operator.mul,
}


def parantheses(values, advanced=False):
    e = values.find(")")
    c = None
    for i in reversed(range(0, values.find(")"))):
        if values[i] == "(":
            c = i + 1
            break

    if advanced and "+" in values[c:e]:
        new_val = evaluate_addition(re.split(r"(\D+)", values[c:e]))
        if len(new_val) > 1:
            if isinstance(new_val, str):
                tmp = re.split(r"(\D+)", new_val)
            else:
                tmp = new_val
            new_val = evaluate(tmp)

    else:
        new_val = evaluate(re.split(r"(\D+)", values[c:e]))

    return values[0 : c - 1] + str(new_val[0]) + values[e + 1 :]


def evaluate(values):
    result = ""
    first_val = values[0]

    for index, value in enumerate(values):
        if value in ops:
            first_val = ops[value](int(values[index - 1]), int(values[index + 1]))
            result = values[0 : index - 1] + [str(first_val)] + values[(index + 2) :]
            return result if len(result) == 1 else evaluate(result)


def evaluate_addition(values):
    result = ""
    first_val = values[0]

    for index, value in enumerate(values):
        if value == "+":
            first_val = ops[value](int(values[index - 1]), int(values[index + 1]))
            result = values[0 : index - 1] + [str(first_val)] + values[(index + 2) :]
            return (
                result
                if len(result) == 1 or not "+" in result
                else evaluate_addition(result)
            )


def calculate_expression(input):
    if "(" in input:
        new_input = parantheses(input)
    else:
        values = re.split(r"(\D+)", input)
        new_input = evaluate(values)

    return int(new_input[0]) if len(new_input) == 1 else calculate_expression(new_input)


def calculate_expression_advanced(input):
    if "(" in input:
        new_input = parantheses(input, True)
    elif "+" in input:
        if isinstance(input, str):
            values = re.split(r"(\D+)", input)
        else:
            values = input
        new_input = evaluate_addition(values)
    else:
        if isinstance(input, str):
            values = re.split(r"(\D+)", input)
        else:
            values = input

        new_input = evaluate(values)

    return (
        int(new_input[0])
        if len(new_input) == 1
        else calculate_expression_advanced(new_input)
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        all_expressions = []
        all_expressions_advanced = []

        for line in file:
            expression = line.strip().replace(" ", "")
            all_expressions.append(calculate_expression(expression))
            all_expressions_advanced.append(calculate_expression_advanced(expression))

        print("Problem 1: ", sum(all_expressions))
        print("Problem 2: ", sum(all_expressions_advanced))