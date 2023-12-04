import utils


def _find_numbers(lines):
    numbers = []
    for line_index in range(len(lines)):
        this_line = lines[line_index]
        number_start = None
        number_end = None
        number_digits = []
        for offset in range(len(this_line)):
            if this_line[offset].isdigit():
                if number_start is None:
                    number_start = offset
                number_end = offset
                number_digits.append(this_line[offset])
            else:
                if number_digits:
                    numbers.append(
                        _Number(
                            digits=number_digits,
                            line=line_index,
                            start=number_start,
                            end=number_end,
                        )
                    )
                number_start = None
                number_end = None
                number_digits = []
        if number_digits:
            numbers.append(
                _Number(
                    digits=number_digits,
                    line=line_index,
                    start=number_start,
                    end=number_end,
                )
            )
    return numbers


def _coordinates_are_in_bounds(coordinates: tuple[int, int], lines: list[str]) -> bool:
    row, col = coordinates
    return row >= 0 and row < len(lines) and col >= 0 and col < len(lines[row])


class _Number:
    value: int
    line: int
    start: int
    end: int

    def __init__(
        self,
        digits,
        line,
        start,
        end,
    ):
        self.value = int("".join(digits))
        self.line = line
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Number(line: {self.line}, start: {self.start}, end: {self.end}, value: {self.value})"

    def is_next_to_symbol(self, lines):
        coordinates_to_check = []
        coordinates_to_check.extend(
            [(self.line - 1, col) for col in range(self.start - 1, self.end + 2)]
        )
        coordinates_to_check.extend(
            [(self.line, col) for col in range(self.start - 1, self.end + 2)]
        )
        coordinates_to_check.extend(
            [(self.line + 1, col) for col in range(self.start - 1, self.end + 2)]
        )
        coordinates_to_check = [
            coords
            for coords in coordinates_to_check
            if _coordinates_are_in_bounds(coords, lines)
        ]
        for coords in coordinates_to_check:
            row, col = coords
            if not (lines[row][col].isdigit() or lines[row][col] == "."):
                return True
        return False


def _part1(lines):
    numbers = _find_numbers(lines)
    total = 0
    for number in numbers:
        if number.is_next_to_symbol(lines):
            total += number.value
    return total


def run():
    print("Day 3")
    lines = utils.load_lines("data/day3.txt")
    print(f"Part 1: The sum of the part numbers is {_part1(lines)}")
