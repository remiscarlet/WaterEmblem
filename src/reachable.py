def reachable(terrain, cur_x, cur_y, spd):
    ugokeru = []
    spdLeft = []
    rows = len(terrain)
    cols = len(terrain[0])
    for row in xrange(rows):
        ugokeru.append([])
        spdLeft.append([])
        for col in xrange(cols):
            ugokeru[row].append(0)
            spdLeft[row].append(-1)

    isReachable(terrain, ugokeru, cur_x, cur_y, spd, spdLeft, rows, cols)

    for row in xrange(rows):
        print ugokeru[row]

    return ugokeru

    # Insert current speed into spdLeft and compare each time: If movement remaining is higher than what is listed there, check that tile.


def isReachable(terrain, ugokeru, x, y, spd, spdLeft, rows, cols):

    ugokeru[y][x] = 1 # I'm assuming if they're already standing there, they can probably reach that square.
    spdLeft[y][x] = spd

    # -1 in terrain assumed to be "unreachable"

    # Upper edge (y - 1)
    if y > 0 and spd > spdLeft[y-1][x]:
        up_dist = terrain[y-1][x]
        if up_dist != -1 and (spd - up_dist) >= 0:
            isReachable(terrain, ugokeru, x, y-1, spd-up_dist, spdLeft, rows, cols)

    # Left edge (x - 1)
    if x > 0 and spd > spdLeft[y][x-1]:
        left_dist = terrain[y][x-1]
        if left_dist != -1 and (spd - left_dist) >= 0:
            isReachable(terrain, ugokeru, x-1, y, spd-left_dist, spdLeft, rows, cols)

    # Right edge (x + 1)
    if x < cols - 1 and spd > spdLeft[y][x+1]:
        right_dist = terrain[y][x+1]
        if right_dist != -1 and (spd - right_dist) >= 0:
            isReachable(terrain, ugokeru, x+1, y, spd-right_dist, spdLeft, rows, cols)

    # Lower edge (y + 1)
    if y < rows - 1 and spd > spdLeft[y+1][x]:
        down_dist = terrain[y+1][x]
        if down_dist != -1 and (spd - down_dist) >= 0:
            isReachable(terrain, ugokeru, x, y+1, spd-down_dist, spdLeft, rows, cols)


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
