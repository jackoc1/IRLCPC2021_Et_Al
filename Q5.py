'''The first line is N, the dimensionality of the space in which the game is played..
The next line contains a floating point numbers R, the radius of the hyperhoop. There follow N
floats, the N coordinates of the centre of he hoop. The first of these corresponds to its height.

There then comes an integer, M, the number of shots to check. Each of the following M lines
each contain N floats, the coordinates of the centre of the ball for each shot.'''

# READ INPUT
N = int(input())

second_line = list(map(float, input().split(" ")))

R, height, hoop_coords = second_line[0], second_line[1], second_line[2:]

M = int(input())

# List of lists of floats
shots = [list(map(float, input().split(" "))) for i in range(M)]

hoop_circ_vals = []

for i in hoop_coords:
    # Range of values for which the ball will be inside for that dimension
    hoop_circ_vals.append([i-R, i+R])

'''For each of the M cases, output ”HIT”, if the hyperball is in the hyperhoop for that case, and
”MISS” otherwise.'''

miss = "MISS"
hit = "HIT"

matched_coords = []

for i in range(M):
    # Check the ball is exactly that height
    if shots[i][0] != height:
        same_height = False
        print(miss)
        continue

    # Check the ball is within the range of other values
    for j in range(1,N):
        if shots[i][j] >= hoop_circ_vals[j-1][0] and shots[i][j] <= hoop_circ_vals[j-1][1]:
            within_bounds = True
        else:
            within_bounds = False
            print(miss)
            break

    if within_bounds:
        print(hit)
