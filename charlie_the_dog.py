from itertools import permutations
from math import sqrt

def count_dist(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return abs(x2 - x1) + abs(y2 - y1)


def main(strArr): # strArr = ["____", "____", "____", "____"]
    min_path = 10000
    food_locs = []
    
    for row in range(4):
        for col in range(4):
            if strArr[row][col] == "F":
                food_locs.append((row, col))
            elif strArr[row][col] == "C":
                start = (row, col)
            elif strArr[row][col] == "H":
                home = (row, col)

    # permute food
    foods_permuted = [
        list(path) for path in list(permutations(food_locs))
    ]

    # add start to start of path and home to end of path
    full_paths = []
    for path in foods_permuted:
        path = [start] + path + [home]
        full_paths.append(path)

    for path in full_paths:
        cur_steps = 0
        for i in range(4):
            cur_steps += count_dist(
                path[i][0], path[i][1], path[i+1][0], path[i+1][1]
            )

        min_path = min(cur_steps, min_path)

    return int(min_path)


print(main(["FOOF", "OCOO", "OOOH", "FOOO"]))
print(main(["OOOO", "OOFF", "OCHO", "OFOO"]))