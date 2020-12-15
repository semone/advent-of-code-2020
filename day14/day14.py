# --- Day 14: Docking Data ---

import re


def decoder_version_1(mask, value):
    val = "{:036b}".format(int(value))
    temp_val = list(val)
    for index, mask_val in enumerate(mask):
        if mask_val != "X":
            temp_val[index] = mask_val

    return int("".join(temp_val), 2)


def get_combinations(result, combinations):
    if not "X" in result:
        combinations.append(result)
    else:
        one = result.replace("X", "1", 1)
        zero = result.replace("X", "0", 1)

        get_combinations(zero, combinations)
        get_combinations(one, combinations)

    return list(map(lambda x: int(x, 2), combinations))


def decoder_version_2(mask, memory_address, value):
    address = "{:036b}".format(int(memory_address))
    tmp_address = list(address)

    for index, mask_val in enumerate(mask):
        if mask_val != "0":
            tmp_address[index] = mask_val

    addresses = get_combinations("".join(tmp_address), [])

    return addresses


if __name__ == "__main__":
    with open("input.txt") as file:
        mask = ""
        memory_1 = {}
        memory_2 = {}
        for line in file:
            if line.startswith("mask"):
                mask = line.split(" = ")[1].strip()
            else:
                memory_address, value = line.split(" = ")
                memory_address = re.sub("[^0-9]", "", memory_address)

                result_value = decoder_version_1(mask, value)
                addresses = decoder_version_2(mask, memory_address, value)

                memory_1[memory_address] = int(result_value)

                for address in addresses:
                    memory_2[address] = int(value)

        print("Problem 1: ", sum(list(memory_1.values())))
        print("Problem 2: ", sum(list(memory_2.values())))