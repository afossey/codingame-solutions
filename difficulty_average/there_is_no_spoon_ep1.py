import sys
import math

# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1

def isReachable(grid, x, y):
    try:
        return "yes" if grid[y][x] == "0" else "continue"
    except IndexError: 
        return "no"

def appendCoord(vector, x, y):
    vector.append(str(x))
    vector.append(str(y))

def appendNeighbourCoord(vector, grid, _x, _y, onTheRight):
    x = _x
    y = _y
    while(True):
        if onTheRight: x += 1
        if not onTheRight: y += 1
        print("try reach x=" + str(x) + " y=" + str(y), file=sys.stderr, flush=True)
        reachable = isReachable(grid, x, y)
        print(reachable, file=sys.stderr, flush=True)
        if (reachable == "no"):
            appendCoord(vector, -1, -1)
            break
        elif reachable == "yes":
            appendCoord(vector, x, y)
            break

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# pour chaque ligne et pour chaque node de la ligne
# vérifier si un voisin de droite existe, vérifier si un voisin de dessous existe
# si oui, ajoute le node au vecteur à print

grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(list(line))

print(grid, file=sys.stderr, flush=True)

results = []
for y, row in enumerate(grid):
    for x, node in enumerate(row):
        if node == '0':
            vector = []
            appendCoord(vector, x, y)
            appendNeighbourCoord(vector, grid, x, y, True)
            appendNeighbourCoord(vector, grid, x, y, False)
            results.append(" ".join(vector))

print("\n".join(results))




# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor

