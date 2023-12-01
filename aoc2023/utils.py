from io import open


def load_lines(path):
    with open(path) as file:
        return file.readlines()


def load(path):
    with open(path, "r") as file:
        return file.read()
