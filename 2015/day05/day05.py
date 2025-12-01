def has_three_vowels(s):
    vowel_count = 0
    for ch in s:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            vowel_count += 1

    return vowel_count >= 3


def has_double_char(s):
    prev = s[0]
    for i in range(1, len(s)):
        ch = s[i]
        if prev == ch:
            return True
        prev = ch
    return False


def no_bad_section(s):
    # ab, cd, pq, or xy
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
        return False
    return True


def is_nice(s: str) -> bool:
    return has_three_vowels(s) and has_double_char(s) and no_bad_section(s)


assert is_nice("ugknbfddgicrmopn")
assert is_nice("aaa")
assert not is_nice("jchzalrnumimnmhp")
assert not is_nice("haegwjzuvuyypxyu")
assert not is_nice("dvszwmarrgswjxmb")


with open("./input.txt", "r") as file:
    lines = file.readlines()


def calc_part1(lines):
    nice_count = 0
    for line in lines:
        if is_nice(line):
            nice_count += 1
    return nice_count


part1 = calc_part1(lines)
print(f"part1: {part1}")
