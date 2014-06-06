def shortPath(map, src, dest, max):
	path = []
	checked = []
	rows = len(map)
	cols = len(map[0])
	for row in xrange(rows):
		checked.append([])
		for col in xrange(cols):
			checked[row].append(-1)

	#for row in xrange(rows):
	#	print checked[row]


# Recursively call minNode on each surrounding unchecked (checked starts as a 2d array initialized to -1 which are then set to the lowest path to given tile)

def minNode(map, checked, src, dest, max, path):
	pass


map = [[1, 1, 1, 1, 1, 1, 1, 1], 
	   [.5, 1, 1, 1, 1, 1, 1, 1],
	   [.5, .5, 1, 1, 1, 1, 1, 1],
	   [.5, .5, .5, .5, 2, 2, 1, 1],
	   [.5, .5, .5, .5, .5, 2, 1.5, 1],
	   [1, 1, 1, 1, 1, 1, 1, 1]]

shortPath(map, (0, 0), (5, 5), 8)
