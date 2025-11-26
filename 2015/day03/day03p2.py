"""
Approach: Build a map tracking cells relative to 0,0 starting position
use a map that has a tuple (x, y) as the key and the count of visits
"""


def distinct_houses_visited(path: str) -> int:
    visited = {(0, 0): 2}

    directions = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}

    santa_curr = (0, 0)
    robo_curr = (0, 0)
    distinct_count = 1
    for p in range(len(path)):
        dir = path[p]
        new_dir = directions[dir]
        if p % 2 == 0:
            santa_curr = (santa_curr[0] + new_dir[0], santa_curr[1] + new_dir[1])
            if santa_curr not in visited:
                visited[santa_curr] = 1
                distinct_count += 1
            else:
                visited[santa_curr] += 1
        else:
            robo_curr = (robo_curr[0] + new_dir[0], robo_curr[1] + new_dir[1])
            if robo_curr not in visited:
                visited[robo_curr] = 1
                distinct_count += 1
            else:
                visited[robo_curr] += 1

    return distinct_count


assert distinct_houses_visited("^v") == 3
assert distinct_houses_visited("^>v<") == 3
assert distinct_houses_visited("^v^v^v^v^v") == 11

with open("./input.txt", "r") as file:
    path = file.read()

path = path.strip()
part2 = distinct_houses_visited(path)
print(f"part1: {part2}")
