# Depreciated

def shortPath(terrain, src, dest, spd):
    path = []
    distMap = []
    rows = len(terrain)
    cols = len(terrain[0])
    for row in xrange(rows):
        distMap.append([])
        for col in xrange(cols):
            distMap[row].append(255)

    minNode(terrain, distMap, src, dest, spd, rows, cols, 0)

    for row in xrange(rows):
                print distMap[row]


# Recursively call minNode on each surrounding undistMap (distMap starts as a 2d array initialized to 255 which are then set to the lowest path to given tile)

def minNode(terrain, distMap, src, dest, spd, rows, cols, srcDir):
    # Base case
    # !! Doesn't handle if direct path is not optimal. To be fixed later.
    x_dist = abs(src[0] - dest[0]) 
    y_dist = abs(src[1] - dest[1])
    if (x_dist == 1 and y_dist == 0) or (x_dist == 0 and y_dist == 1): # If src and dest are adjacent
        distMap[dest[1]][dest[0]] = terrain[dest[1]][dest[0]] # distMap at dest becomes terrain at dest

    upper = 255
    left = 255
    lower = 255
    right = 255

    # 1 2 3 4 up left down right

    # Upper edge (y - 1)
    if dest[1] > 0 and distMap[dest[1] - 1][dest[0]] == 255 and terrain[dest[1] - 1][dest[0]] != -1 and srcDir != 1 :
        upper = minNode(terrain, distMap, src, (dest[0], dest[1] - 1), spd, rows, cols, 3) 

    # Left edge (x - 1)
    if dest[0] > 0 and distMap[dest[1]][dest[0] - 1] == 255 and terrain[dest[1]][dest[0] - 1] != -1 and srcDir != 2:
        left = minNode(terrain, distMap, src, (dest[0] - 1, dest[1]), spd, rows, cols, 4)  

    # Lower edge (y + 1)
    if dest[1] < rows - 1 and distMap[dest[1] + 1][dest[0]] == 255 and terrain[dest[1] + 1][dest[0]] != -1 and srcDir != 3:
        lower = minNode(terrain, distMap, src, (dest[0], dest[1] + 1), spd, rows, cols, 1) 

    # Right edge (x + 1)
    if dest[0] < cols - 1 and distMap[dest[1]][dest[0] + 1] == 255 and terrain[dest[1]][dest[0] + 1] != -1 and srcDir != 4:
        right = minNode(terrain, distMap, src, (dest[0] + 1, dest[1]), spd, rows, cols, 2) 

    distMap[dest[1]][dest[0]] = min(upper, left, lower, right)



### Tests ###
terrain = [[1, 1, 1, 1, 1, 1, 1, 1], 
       [.5, 1, 1, 1, 1, 1, 1, 1],
       [.5, .5, 1, 1, 1, 1, 1, 1],
       [.5, .5, .5, .5, 2, 2, 1, 1],
       [.5, .5, .5, .5, .5, 2, 1.5, 1],
       [1, 1, 1, 1, 1, 1, 1, 1]] #third from last

shortPath(terrain, (0, 0), (5, 5), 8)


#if dest == adjacent to src:
#   distMap[dest] = terrain[dest]
#
#if distMap[adjacent tiles] == 255 and is not edge or terrain[adjacent tile] == -1:
#   minNode(that tile)
#
#distMap[dest] = min(distMap[adjacent tiles])
