import utils
import re
import numpy as np


def process_line(line):
    digits = re.sub(r"\D", "", line)
    return int(digits[0] + digits[-1])


def run():
    lines = utils.load_lines("data/day1.txt")
    calibration_values = map(process_line, lines)
    calibration_sum = np.sum(list(calibration_values))
    print(f"Part 1: The total calibration value is {calibration_sum}.")
