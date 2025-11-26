with open("./input.txt", "r") as file:
    f = file.read()

# print(f)


def find_floor(parens: str) -> int:
    floor = 0
    for i in range(len(parens)):
        p = parens[i]
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1
    return floor


assert find_floor("(())") == 0
assert find_floor("()()") == 0
assert find_floor("(((") == 3
assert find_floor("(()(()(") == 3
assert find_floor("))(((((") == 3
assert find_floor("())") == -1
assert find_floor("))(") == -1
assert find_floor(")))") == -3
assert find_floor(")())())") == -3

part1 = find_floor(f)
print(f"part 1: {part1}")


def position_to_basement(parens: str) -> int:
    floor = 0
    for i in range(len(parens)):
        p = parens[i]
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1

        if floor == -1:
            return i + 1


assert position_to_basement(")") == 1
assert position_to_basement("()())") == 5

part2 = position_to_basement(f)
print(f"part 2: {part2}")
