# --- Day 17: Conway Cubes ---


def three_dim_directions():
    directions = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if not x == y == z == 0:
                    directions.append({"x": x, "y": y, "z": z})

    return directions


def four_dim_directions():
    directions = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if not x == y == z == w == 0:
                        directions.append({"x": x, "y": y, "z": z, "w": w})

    return directions


def pad(values, directions):
    pad_values = values.copy()
    for key, value in values.items():
        for direction in directions:
            dir_key = get_key(direction, key)

            if dir_key not in values:
                pad_values[dir_key] = "."

    return pad_values


def get_key(direction, key):
    if len(direction.values()) == 3:
        return (
            key[0] + direction["x"],
            key[1] + direction["y"],
            key[2] + direction["z"],
        )
    else:
        return (
            key[0] + direction["x"],
            key[1] + direction["y"],
            key[2] + direction["z"],
            key[3] + direction["w"],
        )


def check_neighbors(values, dim):
    directions = three_dim_directions() if dim == 3 else four_dim_directions()

    padded_values = pad(values, directions)
    values_copy = padded_values.copy()

    for key, value in padded_values.items():
        active_neighbors = 0
        for direction in directions:
            dir_key = get_key(direction, key)
            if dir_key in padded_values:
                if padded_values[dir_key] == "#":
                    active_neighbors += 1

        if padded_values[key] == "." and active_neighbors == 3:
            values_copy[key] = "#"

        if padded_values[key] == "#" and (
            active_neighbors != 3 and active_neighbors != 2
        ):
            values_copy[key] = "."

    return values_copy


def parse(input, dim):
    values = {}
    for y, line in enumerate(input):
        for x, value in enumerate(line.strip()):
            key = (x, y, 0) if dim == 3 else (x, y, 0, 0)
            values[key] = value.strip()
    return values


def active_cubes(values, dim):
    val = parse(values, dim)
    for i in range(0, 6):
        val = check_neighbors(val, dim)

    return len(list(filter(lambda x: x == "#", val.values())))


if __name__ == "__main__":
    with open("input.txt") as file:
        input = list(file.read().splitlines())
        print("Problem 1: ", active_cubes(input, 3))
        print("Problem 2: ", active_cubes(input, 4))
