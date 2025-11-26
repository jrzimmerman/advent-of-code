"""
Approach: Build a map tracking cells relative to 0,0 starting position
use a map that has a tuple (x, y) as the key and the count of visits
"""


def distinct_houses_visited(path: str) -> int:
    visited = {(0, 0): 1}

    directions = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}

    curr = (0, 0)
    distinct_count = 1
    for p in range(len(path)):
        dir = path[p]
        new_dir = directions[dir]
        curr = (curr[0] + new_dir[0], curr[1] + new_dir[1])
        if curr not in visited:
            visited[curr] = 1
            distinct_count += 1
        else:
            visited[curr] += 1

    return distinct_count


assert distinct_houses_visited(">") == 2
assert distinct_houses_visited("^>v<") == 4
assert distinct_houses_visited("^v^v^v^v^v") == 2

with open("./input.txt", "r") as file:
    path = file.read()

path = path.strip()
part1 = distinct_houses_visited(path)
print(f"part1: {part1}")
