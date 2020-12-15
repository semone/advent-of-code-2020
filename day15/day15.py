# --- Day 15: Rambunctious Recitation ---


def get_value_at_round(value_list, target_round):
    input = list(map(int, value_list.split(",")))
    memory = dict(zip(input, list(range(1, len(input)))))
    last = input[len(input) - 1]

    for turn in range(len(input) + 1, target_round + 1):
        if last in memory:
            prev = memory[last]
            memory[last] = turn - 1
            last = (turn - 1) - prev
        else:
            memory[last] = turn - 1
            last = 0
    return last


if __name__ == "__main__":
    value_list = "14,1,17,0,3,20"
    print("Problem 1: ", get_value_at_round(value_list, 2020))
    print("Problem 2: ", get_value_at_round(value_list, 30000000))
