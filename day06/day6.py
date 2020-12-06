def custom_scan(group_data):
    return len(set(group_data))


def custom_scan_every(group_data):
    data = {}
    sum = 0
    length = len(group_data)
    for person in group_data:
        for char in person:
            if char in data:
                data[char] += 1
            else:
                data[char] = 1

    for key, value in data.items():
        if value == length:
            sum += 1
    return sum


if __name__ == "__main__":
    with open("input.txt") as file:
        any_yes = []
        every_yes = []
        input = file.read().split("\n\n")

        for answer in input:
            any_yes.append(custom_scan("".join(answer.split("\n"))))
            every_yes.append(custom_scan_every(answer.split("\n")))

        print("Problem 1: ", sum(any_yes))
        print("Problem 2: ", sum(every_yes))