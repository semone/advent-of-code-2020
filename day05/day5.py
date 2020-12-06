import math


def scan_boarding_pass(seat_number, rows, seats):
    min_row, max_row = rows
    min_seat, max_seat = seats
    row = 0
    seat = 0

    for char in seat_number:
        diff_row = math.floor((max_row - min_row) / 2)
        diff_seat = math.floor((max_seat - min_seat) / 2)
        max_row = min_row + diff_row if char == "F" else max_row
        min_row = max_row - diff_row if char == "B" else min_row

        max_seat = min_seat + diff_seat if char == "L" else max_seat
        min_seat = max_seat - diff_seat if char == "R" else min_seat

        if diff_row == 0:
            row = max_row
        if diff_seat == 0:
            seat = max_seat

    id = row * 8 + seat
    return (row, seat, id)


def find_my_seat(seats):
    sorted_seats = sorted(seats)
    return [
        x for x in range(sorted_seats[0], sorted_seats[-1] + 1) if x not in sorted_seats
    ][0]


if __name__ == "__main__":
    with open("input.txt") as file:
        rows = (0, 127)
        seats = (0, 7)
        max = 0
        ids = []
        for line in file:
            row, seat, id = scan_boarding_pass(line, rows, seats)
            ids.append(id)
            if max < id:
                max = id

        my_seat = find_my_seat(ids)

        print("Problem 1: ", max)
        print("Problem 2: ", my_seat)
