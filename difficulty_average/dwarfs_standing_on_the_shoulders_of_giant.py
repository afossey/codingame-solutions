import sys
import math

# https://www.codingame.com/ide/puzzle/dwarfs-standing-on-the-shoulders-of-giants

influences = {}
n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x not in influences:
        influences[x] = [y]
    else:
        influences[x] += [y]

def influence_paths(person):
    visited = [person]
    if person in influences:
        for influenced in influences[person]:
            visited += [influence_paths(influenced)]
    return visited

def longest_path_len(paths):
    result = 1
    branches = list(filter(lambda p : isinstance(p, list), paths))
    if len(branches) > 0:
        selected = max(branches, key = lambda p : len(p))
        result += longest_path_len(selected)
    return result
            
output = max(longest_path_len(influence_paths(person)) for person in influences)
print(str(output))

