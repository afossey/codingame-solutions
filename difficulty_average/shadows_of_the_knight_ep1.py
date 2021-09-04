import sys
import math

# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x1,y1=x0,y0

# game borders
startX,startY=0,0
endX,endY=w-1,h-1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print("w=" + str(w) + " h=" + str(h), file=sys.stderr, flush=True)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if 'U' in bomb_dir:
        endY = y1
        y1 = y1 - math.ceil((y1 - startY)/2)
    if 'D' in bomb_dir:
        startY = y1
        y1 = y1 + math.ceil((endY - y1)/2)
    if 'R' in bomb_dir:
        startX = x1
        x1 = x1 + math.ceil((endX - x1)/2)
    if 'L' in bomb_dir:
        endX = x1
        x1 = x1 - math.ceil((x1 - startX)/2)

    # the location of the next window Batman should jump to.
    print(str(x1) + " " + str(y1))

