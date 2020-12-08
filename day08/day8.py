# --- Day 8: Handheld Halting ---


def computer(program, index=0, accumolator=0, memory=set([])):
    memory.add(index)
    if index >= len(program):
        return accumolator, True

    if program[index][0] == "acc":
        accumolator += int(program[index][1])
        index += 1
    elif program[index][0] == "jmp":
        index += int(program[index][1])
        index = index % len(program)
        if index == 0:
            return accumolator, True
    elif program[index][0] == "nop":
        index += 1

    if index in memory:
        return accumolator, False

    return computer(program, index, accumolator, memory)


if __name__ == "__main__":
    with open("input.txt") as file:
        program = list(map(lambda x: x.split(" "), file.read().splitlines()))
        accumolator, b = computer(program)
        stopped = False

        swap_indices = list(
            map(
                lambda x: x[0],
                filter(
                    lambda val: val[1][0] == "jmp" or val[1][0] == "nop",
                    enumerate(program),
                ),
            )
        )
        print("Problem 1: ", accumolator)

        for index in swap_indices:
            p = [x[:] for x in program]

            if p[index][0] == "nop":
                p[index][0] = "jmp"
            else:
                p[index][0] = "nop"

            accumolator, correct_termination = computer(
                p, index=0, accumolator=0, memory=set([])
            )

            if correct_termination:
                print("Problem 2: ", accumolator)
