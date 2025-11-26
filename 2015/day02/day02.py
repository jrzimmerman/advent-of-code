def get_lwh(s: str):
    slist = s.split("x")
    return [int(x) for x in slist]


assert get_lwh("2x3x4") == [2, 3, 4]
assert get_lwh("1x1x10") == [1, 1, 10]


def calc_paper(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


assert calc_paper(2, 3, 4) == 58
assert calc_paper(1, 1, 10) == 43


def calc_ribbon(l, w, h):
    return min(2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l)


assert calc_ribbon(2, 3, 4) == 10
assert calc_ribbon(1, 1, 10) == 4


def calc_bow(l, w, h):
    return l * w * h


assert calc_bow(2, 3, 4) == 24
assert calc_bow(1, 1, 10) == 10

with open("./input.txt", "r") as file:
    lines = file.readlines()


def calc_part1(lines):
    res = 0
    for line in lines:
        lwh_list = get_lwh(line)
        res += calc_paper(lwh_list[0], lwh_list[1], lwh_list[2])
    return res


part1 = calc_part1(lines)
print(f"part1: {part1}")


def calc_part2(lines):
    res = 0
    for line in lines:
        lwh_list = get_lwh(line)
        res += calc_ribbon(lwh_list[0], lwh_list[1], lwh_list[2])
        res += calc_bow(lwh_list[0], lwh_list[1], lwh_list[2])
    return res


part2 = calc_part2(lines)
print(f"part2: {part2}")
