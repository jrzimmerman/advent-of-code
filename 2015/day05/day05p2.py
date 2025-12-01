"""
It contains a pair of any two letters that appears at least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
"""
def pair_two_letters(s: str):
    if len(s)<3:
        return False

    se = set()
    for i in range(0,len(s),2):
        se.add(s[i:i+1])
    return True

assert pair_two_letters("xyxy")
assert pair_two_letters("aabcdefgaa")
assert not pair_two_letters("aaa")

def char_repeat(s: str):
    for i in range(1, len(s) - 1):
        prev = s[i - 1]
        nex = s[i + 1]
        if prev == nex:
            return True
    return False


assert char_repeat("xyx")
assert char_repeat("abcdefeghi")
assert char_repeat("aaa")


def is_nice(s: str) -> bool:
    return pair_two_letters(s) and char_repeat(s)


assert is_nice("qjhvhtzxzqqjkmpb")
assert is_nice("xxyxx")
assert not is_nice("uurcxstgmygtbstg")
assert not is_nice("ieodomkazucvgmuy")


with open("./input.txt", "r") as file:
    lines = file.readlines()


def calc_part2(lines):
    nice_count = 0
    for line in lines:
        if is_nice(line):
            nice_count += 1
    return nice_count


part2 = calc_part2(lines)
print(f"part2: {part2}")
