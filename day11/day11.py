# --- Day 11: Seating System ---

OCCUPIED_SEAT = "#"
FREE_SEAT = "L"
FLOOR = "."

directions = [
    {"x": -1, "y": 0},
    {"x": -1, "y": -1},
    {"x": 0, "y": -1},
    {"x": 1, "y": 1},
    {"x": 1, "y": 0},
    {"x": 1, "y": -1},
    {"x": 0, "y": 1},
    {"x": -1, "y": 1},
]


def adjecent_occupied_seats(seats, seat, line, width, height):
    adjecent_occupied = 0

    for direction in directions:
        if is_occupied(seats, (line + direction["y"], seat + direction["x"])):
            adjecent_occupied += 1
    return adjecent_occupied


def is_out_of_range(seats, seat_index):
    line, seat = seat_index
    return (line < 0 or line > len(seats) - 1) or (seat < 0 or seat > len(seats[0]) - 1)


def is_occupied(seats, seat_index):
    line, seat = seat_index
    return (
        not is_out_of_range(seats, (line, seat)) and seats[line][seat] == OCCUPIED_SEAT
    )


def can_see_occupied(seats, seat_index, dirx, diry):
    line, seat = seat_index

    if is_out_of_range(seats, (line, seat)) or seats[line][seat] == FREE_SEAT:
        return False
    elif seats[line][seat] == OCCUPIED_SEAT:
        return True
    else:
        return can_see_occupied(seats, (line + diry, seat + dirx), dirx, diry)


def visible_occupied_seats(seats, seat, line, width, height):

    count = 0

    for direction in directions:
        if can_see_occupied(
            seats,
            (line + direction["y"], seat + direction["x"]),
            direction["x"],
            direction["y"],
        ):
            count += 1

    return count


def move_around_adjecent(seats):
    changed = False
    seat_copy = [x[:] for x in seats]
    height = len(seats)
    for line_index, line in enumerate(seats):
        width = len(line)
        for seat_index, seat in enumerate(line):
            number_of_occupied_adjecent_seats = adjecent_occupied_seats(
                seats, seat_index, line_index, width, height
            )

            if seats[line_index][seat_index] == FREE_SEAT:
                if number_of_occupied_adjecent_seats == 0:
                    seat_copy[line_index][seat_index] = OCCUPIED_SEAT
                    changed = True
            elif seats[line_index][seat_index] == OCCUPIED_SEAT:
                if number_of_occupied_adjecent_seats >= 4:
                    seat_copy[line_index][seat_index] = FREE_SEAT
                    changed = True

    if changed:
        return move_around_adjecent(seat_copy)
    else:
        s = 0
        for line in seat_copy:
            s += line.count("#")
        return s


def move_around_visible(seats):
    changed = False
    seat_copy = [x[:] for x in seats]
    for line_index, line in enumerate(seats):
        for seat_index, seat in enumerate(line):
            visible = visible_occupied_seats(
                seats, seat_index, line_index, len(line), len(seats)
            )
            if seats[line_index][seat_index] == FREE_SEAT:
                if visible == 0:
                    seat_copy[line_index][seat_index] = OCCUPIED_SEAT
                    changed = True
            elif seats[line_index][seat_index] == OCCUPIED_SEAT:
                if visible >= 5:
                    seat_copy[line_index][seat_index] = FREE_SEAT
                    changed = True

    if changed:
        return move_around_visible(seat_copy)
    else:
        s = 0
        for line in seat_copy:
            s += line.count("#")
        return s


if __name__ == "__main__":
    with open("input.txt") as file:
        seats = list(map(lambda x: list(x), file.read().splitlines()))

        print("Problem 1: ", move_around_adjecent(seats))
        print("Problem 2: ", move_around_visible(seats))
