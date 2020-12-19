import importlib.resources as pkg_resources

import advent.data


def read_puzzle(i: int) -> list:
    return (pkg_resources.read_text(advent.data, f"input_{i}.txt")).splitlines()
