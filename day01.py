import os
import re
import time

t1 = time.perf_counter()
INPUTS_DIR = os.path.join(os.path.dirname(__file__), "inputs")

# Part #1
with open(os.path.join(INPUTS_DIR, "day1.txt")) as f:
    calibration_values = f.readlines()
numbers_from_values = [
    re.findall(r"\d", calibration_value)
    for calibration_value in calibration_values
]
first_and_last_concat = [int(num[0] + num[-1]) for num in numbers_from_values]
print(f"Answer #1: {sum(first_and_last_concat)}")

# Part #2
number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
account_for_overlap_regex = f"(\\d)|(?=({'|'.join(number_words)}))"
all_numbers_from_values = [
    re.findall(account_for_overlap_regex, calibration_value)
    for calibration_value in calibration_values
]
cleaned_up = [
    [digit or number_word for digit, number_word in matches]
    for matches in all_numbers_from_values
]
translated = [
    [number_words.get(num, num) for num in found_nums]
    for found_nums in cleaned_up
]
real_calibration_values = [int(num[0] + num[-1]) for num in translated]
print(f"Answer #2: {sum(real_calibration_values)}")
t2 = time.perf_counter()

print(f"Execution time: {t2 - t1}")
