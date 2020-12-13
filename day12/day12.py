# --- Day 12: Rain Risk ---

DIRECTIONS = [
    [1, 0],  # East
    [0, -1],  # South
    [-1, 0],  # West
    [0, 1],  # North
]


def take_instruction(intstuction, current_state, waypoint):
    val = int(intstuction[1:])
    key = intstuction[0]
    if key == "F":
        if waypoint:
            current_state["ship_x"] = current_state["ship_x"] + (
                current_state["x"] * val
            )
            current_state["ship_y"] = current_state["ship_y"] + (
                current_state["y"] * val
            )
        else:
            dx, dy = DIRECTIONS[int(current_state["direction"] / 90 % 4)]
            current_state["x"] += dx * val
            current_state["y"] += dy * val
    if key == "N":
        current_state["y"] += val
    if key == "S":
        current_state["y"] -= val
    if key == "E":
        current_state["x"] += val
    if key == "W":
        current_state["x"] -= val
    if key == "R":
        if waypoint:
            for _ in range(int(val / 90)):
                current_state["x"], current_state["y"] = (
                    current_state["y"],
                    -current_state["x"],
                )
        else:
            current_state["direction"] += val

    if key == "L":
        if waypoint:
            for _ in range(int(val / 90)):
                current_state["x"], current_state["y"] = (
                    -current_state["y"],
                    current_state["x"],
                )
        else:
            current_state["direction"] -= val

    return current_state


def follow_instructions(instructions, state, waypoint=False):

    for instruction in instructions:
        state = take_instruction(instruction, state, waypoint)

    return (
        abs(state["x"]) + abs(state["y"])
        if not waypoint
        else abs(state["ship_x"]) + abs(state["ship_y"])
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()
        state = {
            "x": 0,
            "y": 0,
            "direction": 0,
        }

        state_2 = {
            "x": 10,
            "y": 1,
            "ship_x": 0,
            "ship_y": 0,
        }
        print("Problem 1: ", follow_instructions(input, state))
        print("Problem 2: ", follow_instructions(input, state_2, waypoint=True))
