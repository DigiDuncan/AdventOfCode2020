from advent.lib.utils import read_puzzle

data = read_puzzle(3)


def part1():
    tm = TreeMap(data)
    print(f"right 3, down 1: {tm.slope(3, 1)}")
    return tm.slope(3, 1)


def part2():
    tm = TreeMap(data)
    print(f"right 1, down 1: {tm.slope(1, 1)}")
    print(f"right 3, down 1: {tm.slope(3, 1)}")
    print(f"right 5, down 1: {tm.slope(5, 1)}")
    print(f"right 7, down 1: {tm.slope(7, 1)}")
    print(f"right 1, down 2: {tm.slope(1, 2)}")
    print(tm.slope(1, 1) * tm.slope(3, 1) * tm.slope(5, 1) * tm.slope(7, 1) * tm.slope(1, 2))
    return tm.slope(1, 1) * tm.slope(3, 1) * tm.slope(5, 1) * tm.slope(7, 1) * tm.slope(1, 2)


class TreeMap:
    def __init__(self, lines):
        self.lines = lines

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, key):
        return self.lines.__getitem__(key)

    def __iter__(self):
        return self.lines.__iter__()

    def read_tile(self, row, col):
        return self[row][col % len(self[row])]

    def slope(self, right, down):
        treecount = 0
        for i in range(len(self)):
            y = i * down
            x = i * right
            if y > len(self) - 1:
                break
            if self.read_tile(y, x) == "#":
                treecount += 1

        return treecount
