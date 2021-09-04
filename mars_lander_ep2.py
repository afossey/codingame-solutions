import sys
import math

# https://www.codingame.com/ide/puzzle/mars-lander-episode-2

surface = []
surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append([land_x, land_y])

def get_flat_coords():
    result = []
    for i in range(len(surface)):
        if (i+1 < len(surface)):
            if surface[i][1]==surface[i+1][1]:
                result.append(surface[i])
                result.append(surface[i+1])
    return result

def distance(a, b=[0,0]):
    return math.sqrt(math.pow(b[0]-a[0], 2) + math.pow(b[1]-a[1],2))

def closest_point(current, points):
    dist = -1
    result = []
    for point in points:
        point_dist = distance(current, point)
        if dist < 0 or point_dist <= dist:
            dist = point_dist
            result = point
    return result

def sum_vectors(vectors):
    x=y=0
    for vector in vectors:
        magn_vect=vector[0]
        angle_vect=vector[1]
        x += magn_vect * round(math.cos(math.radians(angle_vect)), 3)
        y += magn_vect * round(math.sin(math.radians(angle_vect)), 3)
    return [x, y]

def flight_vector(h_speed, v_speed, r, p):
    vertical_speed = [v_speed, 90]
    horizontal_speed = [h_speed, 0]
    gravity = [-3.711, 90]
    thrust = [p, 90 + r]
    return sum_vectors([vertical_speed, horizontal_speed, gravity, thrust]) 

def possible_flight_vectors(h_speed, v_speed, rotate, power): 
    result = []
    for p in range(max(power-1, 0), min(power+2, 5)):
        for r in range(max(rotate-15, -90), min(rotate+16, 91)):
            v = flight_vector(h_speed, v_speed, r, p)
            v += [p, r]
            result.append(v)
    return result

def travel_safe(vectors, current, target):
    result = []
    is_up = current[1] - target[1] < 0
    is_right = current[0] - target[0] < 0
    x=y=0
    if not flat_ground_below(current):
        x = 60 if is_right else -60
        y = 15 if is_up else -10
    optimal_v = [x,y]
    
    no_optimal_dist = True
    d = distance(vectors[0], optimal_v)
    for vector in vectors:
        if distance(vector, optimal_v) < d:
            no_optimal_dist = False
            break
    if no_optimal_dist:
        print("cannot travel safely, rotating..", file=sys.stderr, flush=True)
        return [0,0,0,0]

    for vector in vectors:
        if len(result) == 0:
            result = vector
        v_dist = distance(vector, optimal_v)
        r_dist = distance(result, optimal_v)
        if v_dist < r_dist:
            result = vector
    return result

def flat_ground_below(current): 
    return current[0] > flat_coords[0][0] and current[0] < flat_coords[1][0]

init_height = 0
flat_coords = get_flat_coords()

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if init_height == 0:
        init_height = y 
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    current = [x,y]
    landing_point = closest_point(current, flat_coords)
    descent_point = [landing_point[0], init_height]
    vectors = possible_flight_vectors(h_speed, v_speed, rotate, power)
    v = travel_safe(vectors, current, descent_point)
    print(str(v[3]) + " " + str(v[2]))

