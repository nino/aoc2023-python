import day3

lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

def test_find_numbers():
    assert str(day3._find_numbers(lines)) == "[Number(line: 0, start: 0, end: 2, value: 467), Number(line: 0, start: 5, end: 7, value: 114), Number(line: 2, start: 2, end: 3, value: 35), Number(line: 2, start: 6, end: 8, value: 633), Number(line: 4, start: 0, end: 2, value: 617), Number(line: 5, start: 7, end: 8, value: 58), Number(line: 6, start: 2, end: 4, value: 592), Number(line: 7, start: 6, end: 8, value: 755), Number(line: 9, start: 1, end: 3, value: 664), Number(line: 9, start: 5, end: 7, value: 598)]"

def test_sample_input():
    assert day3._part1(lines) == 4361
