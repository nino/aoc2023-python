import day1


def test_part2_numbers_for_line():
    assert day1._get_numbers_for_line("two1nine") == 29
    assert day1._get_numbers_for_line("eightwothree") == 83
    assert day1._get_numbers_for_line("abcone2threexyz") == 13
    assert day1._get_numbers_for_line("xtwone3four") == 24
    assert day1._get_numbers_for_line("4nineeightseven2") == 42
    assert day1._get_numbers_for_line("zoneight234") == 14
    assert day1._get_numbers_for_line("7pqrstsixteen") == 76
    assert day1._get_numbers_for_line("7pqrstsixteetwonen") == 71


def test_day2_full():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert day1._part2(lines) == 281
