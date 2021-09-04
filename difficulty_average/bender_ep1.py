import sys
import math

# https://www.codingame.com/ide/puzzle/bender-episode-1

l, c = [int(i) for i in input().split()]
_map = []
for i in range(l):
    row = input()
    _map.append(list(row))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

DIRECTION_CODES = {"S": "SOUTH", "E": "EAST", "W": "WEST", "N": "NORTH"}
SOUTH, EAST, WEST, NORTH = ["SOUTH", "EAST", "WEST", "NORTH"]

def init():
    teleporters = []
    suicide_booth = start_pos = None
    for i, row in enumerate(_map):
        for j, zone in enumerate(row):
            if zone == "@":
                start_pos = [i,j]
            elif zone == "$":
                suicide_booth = [i,j]
            elif zone == "T":
                teleporters.append([i, j])
    return [start_pos, teleporters, suicide_booth]

# rules
def zone(x,y):
    return _map[x][y]

def next_pos(direction, x, y):
    if direction == NORTH:
        return [x-1, y]
    elif direction == SOUTH:
        return [x+1, y]
    elif direction == EAST:
        return [x, y+1]
    elif direction == WEST:
        return [x, y-1]

def is_breakable_obstacle(zone):
    return zone == "X"
def is_obstacle(zone):
    return zone == "#" or is_breakable_obstacle(zone)

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)

def avoid_obstacle(direction, x, y):
    _x, _y = next_pos(direction, x, y)
    if not is_obstacle(zone(_x, _y)):
        return direction
    for obs_dir in obs_dir_priorities:
        if obs_dir != direction:
            _x, _y = next_pos(obs_dir, x, y)
            if not is_obstacle(zone(_x, _y)):
                return obs_dir
    raise ValueError("found no direction to avoid obstacle. " + str(direction))

def is_path_modifier(zone):
    return zone in ["S", "E", "W", "N"]
def is_circuit_inverter(zone):
    return zone == "I"
def is_beer(zone):
    return zone == "B"
def is_teleporter(zone):
    return zone == "T"
        
        
start_pos, teleporters, suicide_booth = init()
x,y = start_pos
direction = SOUTH
obs_dir_priorities = [SOUTH, EAST, NORTH, WEST]
rampage_mode = False
output_seq = ""
output = []

while(True):
    # suicide booth
    if zone(x,y) == "$":
        break
    if not suicide_booth or len(output_seq) > 2*l*c and output_seq.count(output_seq[2*l*c:3*l*c])>1:
        output_seq = "LOOP"
        break

    # check current zone
    if is_path_modifier(zone(x,y)):
        direction = DIRECTION_CODES[zone(x,y)]
    elif is_circuit_inverter(zone(x,y)):
        obs_dir_priorities.reverse()
    elif is_beer(zone(x,y)):
        rampage_mode = not rampage_mode
    elif is_teleporter(zone(x,y)):
        x,y = next(filter(lambda tp: tp != [x,y], teleporters))
    
    # check beer mode
    _x,_y = next_pos(direction, x, y)
    if rampage_mode and is_breakable_obstacle(zone(_x, _y)):
        _map[_x][_y] = " "

    # go forward avoiding obstacles
    direction = avoid_obstacle(direction, x, y)
    x,y = next_pos(direction, x, y)
    output_seq += direction # seq for infinite loop detection
    output.append(direction) # list for printing

if output_seq == "LOOP":
    print("LOOP")
else: 
    for d in output:
        print(d)



