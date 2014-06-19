def reachable(terrain, cur_x, cur_y, spd):
    ugokeru = []
    rows = len(terrain)
    cols = len(terrain[0])
    for row in xrange(rows):
        ugokeru.append([])
        for col in xrange(cols):
            ugokeru[row].append(0)

    isReachable(terrain, ugokeru, cur_x, cur_y, spd, rows, cols)

    for row in xrange(rows):
        print ugokeru[row]

    return ugokeru


def isReachable(terrain, ugokeru, x, y, spd, rows, cols):
    # Base case
    ugokeru[y][x] = 1 # I'm assuming if they're already standing there, they can probably reach that square.

    # -1 in terrain assumed to be "unreachable"

    # Upper edge (y - 1)
    if y > 0:# and ugokeru[y-1][x] == 0:
        up_dist = terrain[y-1][x]
        if up_dist != -1 and (spd - up_dist) >= 0:
            isReachable(terrain, ugokeru, x, y-1, spd-up_dist, rows, cols)

    # Left edge (x - 1)
    if x > 0:# and ugokeru[y][x-1] == 0:
        left_dist = terrain[y][x-1]
        if left_dist != -1 and (spd - left_dist) >= 0:
            isReachable(terrain, ugokeru, x-1, y, spd-left_dist, rows, cols)

    # Right edge (x + 1)
    if x < cols - 1:# and ugokeru[y][x+1] == 0:
        right_dist = terrain[y][x+1]
        if right_dist != -1 and (spd - right_dist) >= 0:
            isReachable(terrain, ugokeru, x+1, y, spd-right_dist, rows, cols)

    # Lower edge (y + 1)
    if y < rows - 1:# and ugokeru[y+1][x] == 0:
        down_dist = terrain[y+1][x]
        if down_dist != -1 and (spd - down_dist) >= 0:
            isReachable(terrain, ugokeru, x, y+1, spd-down_dist, rows, cols)


### Tests ###
terrain = [[1, 1, 1, 1, 1, 1, 1, 1], 
       [1.5, 1, 1, 1, 1, 1, 1, 1],
       [1.5, 1.5, 1, 1, 1, 1, 1, 1],
       [1.5, 1.5, -1, 1.5, 2, -1, 1, 1],
       [1.5, 1.5, 1.5, 1.5, 1.5, 2, 1.5, 1],
       [1, 1, 1, 1, 1, 1, 1, 1]] 

reachable(terrain, 1, 1, 10)
print 

terrain2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

reachable(terrain2, 0, 0, 6)
print
reachable(terrain2, 4, 3, 10)
