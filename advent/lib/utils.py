import importlib.resources as pkg_resources

import advent.data


def read_puzzle(i: int, keepends = False) -> list:
    return (pkg_resources.read_text(advent.data, f"input_{i}.txt")).splitlines(keepends)


def tryInt(val):
    """Try to cast `val` to an `int`, if it can't, just return `val`."""
    try:
        val = int(val)
    except ValueError:
        pass
    return val
