from advent import days
from advent.lib.utils import tryInt


def main():
    day = tryInt(input("Day? "))
    part = tryInt(input("Part? "))

    if not isinstance(day, int):
        print(f"{day} is not an integer.")
    if not isinstance(part, int):
        print(f"{part} is not an integer.")

    if not getattr(days, f"day{day}", None):
        print(f"Day {day} has not been coded yet!")
    if part not in [1, 2]:
        print("There is only a part 1 and 2.")

    print("-" * 25 + "\n")
    print(getattr(getattr(days, f"day{day}"), f"part{part}")())
    print("wow")

# This is needed, or else calling `python -m <name>` will mean that main() is called twice.
if __name__ == "__main__":
    main()
