from dataclasses import dataclass
import re
from advent.lib.utils import read_puzzle

data = read_puzzle(4, True)
data = ''.join(data)


def part1():
    passports = generate_passports(data)
    for passport in passports:
        if passport.valid() != passport.naivevalid():
            print(f"This isn't valid but should be: {passport.original!r}")
    valids = [passport.valid() for passport in passports]
    print(f"Valid Passports: {valids.count(True)}")
    return valids.count(True)


def part2():
    passports = generate_passports(data)
    valids = [passport.very_valid() for passport in passports]
    print(f"Valid Passports: {valids.count(True)}")
    return valids.count(True)


def generate_passports(s: str):
    passports = []
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for chunk in s.split("\n\n"):
        passport = Passport()
        passport.original = chunk
        for field in fields:
            match = re.search(field + r":([^\s]+)\s*", chunk)
            if match is not None:
                g = match.group(1)
                setattr(passport, field, g)
        passports.append(passport)
    return passports


@dataclass
class Passport:
    original = None
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def naivevalid(self):
        return (
            "byr" in self.original
            and "iyr" in self.original
            and "eyr" in self.original
            and "hgt" in self.original
            and "hcl" in self.original
            and "ecl" in self.original
            and "pid" in self.original
        )

    def valid(self):
        return (
            self.byr is not None
            and self.iyr is not None
            and self.eyr is not None
            and self.hgt is not None
            and self.hcl is not None
            and self.ecl is not None
            and self.pid is not None
        )

    def very_valid(self):
        try:
            b = bool(
                # Birth year, four digits, 1920-2002
                self.byr is not None
                and len(self.byr) == 4
                and 1920 <= int(self.byr) <= 2002
                # Issue year, four digits, 2010-2020
                and self.iyr is not None
                and len(self.iyr) == 4
                and 2010 <= int(self.iyr) <= 2020
                # Expiry year, four digits, 2020-2030
                and self.eyr is not None
                and len(self.eyr) == 4
                and 2020 <= int(self.eyr) <= 2030
                # Height, 150-193cm or 59-76in
                and self.hgt is not None
                and (m := re.match(r"(\d+)(cm|in)", self.hgt))
                and (
                    (m.group(2) == "cm" and 150 <= int(m.group(1)) <= 193)
                    or (m.group(2) == "in" and 59 <= int(m.group(1)) <= 76)
                )
                # Hair color, lowercase hexcode starting with #
                and self.hcl is not None
                and re.match(r"#[a-f0-9]{6}", self.hcl)
                # Eye color, is in the list of colors
                and self.ecl is not None
                and self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                # PID, nine-digit number
                and self.pid is not None
                and re.match(r"\d{9}", self.pid)
            )
        except Exception:
            raise
        return b
