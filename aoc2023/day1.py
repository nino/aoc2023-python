import utils
import re
import numpy as np


def _get_digits_for_line(line):
    digits = re.sub(r"\D", "", line)
    return int(digits[0] + digits[-1])


def _get_numbers_for_line(line):
    """
    Process a line for part 2. I was originally just doing re.findall, but that
    didn't deal with overlapping matches, so now we're just iterating character
    by character. This is super duper inefficient, but it technically works, so
    🤷
    """
    numbers = []
    matchers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    for index in range(len(line)):
        remainder = line[index:]
        for key in matchers:
            if remainder.startswith(key):
                numbers.append(matchers[key])

    return int(str(numbers[0]) + str(numbers[-1]))


def _part1(lines):
    """
    Input is lines of text. In each line, find the first and last digit and
    combine them into a 2-digit integer. Return the sum of the numbers from all
    the lines.
    """
    calibration_values = [_get_digits_for_line(line) for line in lines]
    calibration_sum = np.sum(calibration_values)
    return calibration_sum


def _part2(lines):
    """
    Same as part 1, but the words "one" through "nine" also count.
    """
    calibration_values = [_get_numbers_for_line(line) for line in lines]
    calibration_sum = np.sum(calibration_values)
    return calibration_sum


def run():
    print("Day 1")
    lines = utils.load_lines("data/day1.txt")
    print(f"Part 1: The total calibration value is {_part1(lines)}.")
    print(f"Part 2: The total calibration value is {_part2(lines)}.")
