with open("./test.txt", "r") as testfile:
    testlines = testfile.readlines()

with open("./input.txt", "r") as f:
    lines = f.readlines()


def split_rotation(s: str) -> {str, int}:
    return s[:1], int(s[1:])


def calc_part1(lines):
    dial = 50
    times_at_zero = 0

    for line in lines:
        rotation, num = split_rotation(line)
        print("rotation")
        print(rotation)
        print("num")
        print(num)

        if rotation == "R":
            dial = (dial + num) % 100
        elif rotation == "L":
            dial = (dial - num) % 100

        # print("dial")
        # print(dial)
        if dial == 0:
            times_at_zero += 1
            print("times at zero")
            print(times_at_zero)

    return times_at_zero


test1 = calc_part1(testlines)
assert test1 == 3

part1 = calc_part1(lines)
print(f"part1: {part1}")


def calc_part2_brute_force(lines):
    dial = 50
    times_at_zero = 0

    for line in lines:
        rotation, num = split_rotation(line)

        # brute force - modify dial 1 increment at a time
        for _ in range(num):
            if rotation == "R":
                dial = (dial + 1) % 100
            elif rotation == "L":
                dial = (dial - 1) % 100

            if dial == 0:
                times_at_zero += 1

    return times_at_zero


test2 = calc_part2_brute_force(testlines)
assert test2 == 6

part2 = calc_part2_brute_force(lines)
print(f"part2: {part2}")
