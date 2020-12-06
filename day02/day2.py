# --- Day 2: Password Philosophy ---

if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().splitlines()
        valid_1 = 0
        valid_2 = 0
        for x in input:
            [min_max, value, password] = x.split()
            val = value.replace(":", "")
            min, max = map(int, min_max.split("-"))

            if password.count(val) >= min and password.count(val) <= max:
                valid_1 += 1

            if (
                password[min - 1] == val
                and password[max - 1] != val
                or password[max - 1] == val
                and password[min - 1] != val
            ):
                valid_2 += 1

        print("Problem 1: ", valid_1)
        print("Problem 2: ", valid_2)
