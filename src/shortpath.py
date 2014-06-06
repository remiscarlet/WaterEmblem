def shortPath(terrain, src, dest, max):
	path = []
	distMap = []
	rows = len(terrain)
	cols = len(terrain[0])
	for row in xrange(rows):
		distMap.append([])
		for col in xrange(cols):
			distMap[row].append(255)

	#for row in xrange(rows):
	#print distMap[row]


# Recursively call minNode on each surrounding undistMap (distMap starts as a 2d array initialized to 255 which are then set to the lowest path to given tile)

def minNode(terrain, distMap, src, dest, max, path, rows, cols):
	# Base case
	x_dist = abs(src[0] - dest[0]) 
	y_dist = abs(src[1] - dest[1])
	if (x_dist == 1 and y_dist == 0) or (x_dist == 0 and y_dist == 1): # If src and dest are adjacent
		distMap[dest[1]][dest[0]] = terrain[dest[1]][dest[0]] # distMap at dest becomes terrain at dest


terrain = [[1, 1, 1, 1, 1, 1, 1, 1], 
	   [.5, 1, 1, 1, 1, 1, 1, 1],
	   [.5, .5, 1, 1, 1, 1, 1, 1],
	   [.5, .5, .5, .5, 2, 2, 1, 1],
	   [.5, .5, .5, .5, .5, 2, 1.5, 1],
	   [1, 1, 1, 1, 1, 1, 1, 1]] #third from last

shortPath(terrain, (0, 0), (5, 5), 8)


if dest == adjacent to src:
	distMap[dest] = terrain[dest]

if distMap[adjacent tiles] == 255 and is not edge or terrain[adjacent tile] == -1:
	minNode(that tile)

distMap[dest] = min(distMap[adjacent tiles])