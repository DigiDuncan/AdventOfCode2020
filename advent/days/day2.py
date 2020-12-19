import re

from advent.lib.utils import read_puzzle

data = read_puzzle(2)


def part1():
    passwords = []

    for entry in data:
        passwords.append(Password.parse(entry))

    return sum([p.is_good_sled() for p in passwords])


def part2():
    passwords = []

    for entry in data:
        passwords.append(Password.parse(entry))

    return sum([p.is_good_toboggan() for p in passwords])


class Password:
    def __init__(self, required_char: str, min_count: int, max_count: int, password: str):
        self.required_char: str = required_char
        self.min_count: int = int(min_count)
        self.max_count: int = int(max_count)
        self.password: str = password

    def is_good_sled(self) -> bool:
        return self.min_count <= self.password.count(self.required_char) <= self.max_count

    def is_good_toboggan(self) -> bool:
        return (self.password[self.min_count - 1] == self.required_char) ^ (self.password[self.max_count - 1] == self.required_char)

    @classmethod
    def parse(cls, s: str):
        re_password = r"(\d+)-(\d+) (\w): (.*)"
        if match := re.match(re_password, s):
            min_c, max_c, req, pword = match.groups()
            return Password(req, min_c, max_c, pword)
        raise ValueError(f"{s!r} is not a valid password string.")
