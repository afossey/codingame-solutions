import sys
import math

# https://www.codingame.com/ide/puzzle/aneo

speed = int(input())
light_count = int(input())
distances = []
durations = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    distances.append(distance)
    durations.append(duration)
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(str(speed) + " " + str(light_count) + " " + str(distances) + " " + str(durations), file=sys.stderr, flush=True)

def isLightGreen(i, seconds):
    lightIsGreen = True
    for second in range(1, seconds + 1):
        if (second % durations[i]) == 0:
            lightIsGreen = not lightIsGreen
    return lightIsGreen

def allLightsGreen(s):
    for light in range(light_count):
        d = (distances[light] * 3600) / (s * 1000)
        if not isLightGreen(light, math.floor(d)):
            return False
    return True

for s in reversed(range(1, speed + 1)):
    if allLightsGreen(s):
        print(str(s))
        break
