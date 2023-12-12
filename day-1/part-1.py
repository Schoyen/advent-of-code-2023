def find_first_digit(line):
    return next(filter(lambda x: x.isdigit(), line))


def test_word_forward(line, start, word):
    if len(line) < start + len(word):
        return False

    return line[start : start + len(word)] == word


def test_word_backward(line, start, word):
    if start - len(word) < 0:
        return False

    return line[start - len(word) + 1 : start + 1] == word


WORD_MAP = dict(
    zero="0",
    one="1",
    two="2",
    three="3",
    four="4",
    five="5",
    six="6",
    seven="7",
    eight="8",
    nine="9",
)


def find_first_word_or_digit(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for word in WORD_MAP:
            if test_word_forward(line, i, word):
                return WORD_MAP[word]
    assert False


def find_last_word_or_digit(line):
    for i in reversed(range(len(line))):
        if line[i].isdigit():
            return line[i]
        for word in WORD_MAP:
            if test_word_backward(line, i, word):
                return WORD_MAP[word]
    assert False


with open("input.dat", "r") as f:
    dat = f.read().split()


print(
    sum(
        [int(find_first_digit(line) + find_first_digit(reversed(line))) for line in dat]
    )
)


print(
    sum(
        [
            int(find_first_word_or_digit(line) + find_last_word_or_digit(line))
            for line in dat
        ]
    )
)
