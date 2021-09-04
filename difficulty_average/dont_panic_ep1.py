import sys
import math

# https://www.codingame.com/ide/puzzle/don't-panic-episode-1

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = {key: None for key in range(nb_floors)}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

LEFT, RIGHT = "LEFT", "RIGHT"

def get_direction(a, b):
    return LEFT if a > b else RIGHT

print("Exit: " + str([exit_floor, exit_pos]), file=sys.stderr, flush=True)
print("Elevators: " + str(elevators), file=sys.stderr, flush=True)

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    if clone_floor == -1:
        print("WAIT")
    else:
        print("Clone: " + str([clone_floor, clone_pos]), file=sys.stderr, flush=True)
        target = elevators[clone_floor] if exit_floor > clone_floor else exit_pos 
        if get_direction(clone_pos, target) != direction and not elevators[clone_floor] == clone_pos:
            print("BLOCK")
        else:
            print("WAIT")

