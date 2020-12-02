from advent.lib.utils import read_puzzle

data = read_puzzle(1)


def run_part1():
    num1: int = None
    num2: int = None

    for entry in data:
        one = int(entry)
        for second_entry in data:
            two = int(second_entry)
            if one + two == 2020:
                num1, num2 = one, two

    return num1 * num2


def run_part2():
    num1: int = None
    num2: int = None
    num3: int = None

    for entry in data:
        one = int(entry)
        for second_entry in data:
            two = int(second_entry)
            for third_entry in data:
                three = int(third_entry)
                if one + two + three == 2020:
                    num1, num2, num3 = one, two, three

    return num1 * num2 * num3
