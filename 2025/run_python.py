import argparse
import importlib
import os
import re


AOCPY_MOD = "aocpy"
AOCPY_DIR = os.path.join(os.path.dirname(__file__), AOCPY_MOD)
days_solved = [
    m.group() for f in os.listdir(AOCPY_DIR) if (m := re.match(r"\d+", f))
]

parser = argparse.ArgumentParser("Runs Python AoC solutions")
parser.add_argument("day", choices=days_solved)
args = parser.parse_args()

selected_day = importlib.import_module(f"{AOCPY_MOD}.{args.day}")
selected_day.solve()
