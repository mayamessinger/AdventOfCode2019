import re

# start and end points are "oriented" such that start coordiate will always be
# smaller than end coordinate (smaller == closer to (0, 0))
class Path:
	def __init__(self, x1, y1, x2, y2):
		self.start = Coordinate(min(x1, x2), min(y1, y2))
		self.end = Coordinate(max(x1, x2), max(y1, y2))

	def __eq__(self, obj):
		return isinstance(obj, Path) and self.start == obj.start and self.end == obj.end

# all x and y values are relative to the central port (0, 0)
class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, obj):
		return isinstance(obj, Coordinate) and self.x == obj.x and self.y == obj.y

	def distanceFromCenter(self):
		return abs(self.x) + abs(self.y)

def run(inputFile):
	contents = open(inputFile, "r")
	wireMoves = contents.read().split("\n")
	contents.close()

	allPaths = mapAllWires(wireMoves)
	intersections = getIntersections(allPaths)

	print(getClosestIntersection(intersections).distanceFromCenter())

# returns an array of arrays, each subarray represents one wire's paths
# paths are objects with absolute start and end points
def mapAllWires(wires):
	wirePaths = []

	for wire in wires:
		wireDirections = wire.split(",")
		wirePaths.append(mapWire(wireDirections))

	return wirePaths

# converts the given commands into Paths that have absolute start and end points
def mapWire(wireMoves):
	pathCoords = []

	startX = 0
	startY = 0
	currX = startX
	currY = startY

	for move in wireMoves:
		moveDir = re.search("^[RLUD]", move).group()
		moveLength = int(re.search("[0-9]+$", move).group())

		if (moveDir == "L"):
			pathCoords.append(Path(currX, currY, currX - moveLength, currY))
			currX -= moveLength
		if (moveDir == "R"):
			pathCoords.append(Path(currX, currY, currX + moveLength, currY))
			currX += moveLength
		if (moveDir == "U"):
			pathCoords.append(Path(currX, currY, currX, currY + moveLength))
			currY += moveLength
		if (moveDir == "D"):
			pathCoords.append(Path(currX, currY, currX, currY - moveLength))
			currY -= moveLength

	return pathCoords

def getIntersections(paths):
	intersections = []

	wireA = paths[0]
	wireB = paths[1]

	for a in range(0, len(wireA)):
		for b in range(0, len(wireB)):
			cross = crosses(wireA[a], wireB[b])
			if (cross is not None):
				intersections.append(cross)

	return intersections

def crosses(pathA, pathB):
	if (pathA.start.x <= pathB.start.x <= pathA.end.x
		and pathB.start.y <= pathA.start.y <= pathB.end.y):
			return Coordinate(pathB.start.x, pathA.start.y)

	if (pathA.start.y <= pathB.start.y <= pathA.end.y
		and pathB.start.x <= pathA.start.x <= pathB.end.x):
			return Coordinate(pathA.start.x, pathB.start.y)

def getClosestIntersection(intersections):
	intersections.remove(Coordinate(0, 0))

	return min(intersections, key=lambda coord: coord.distanceFromCenter())


run("day3_input.txt")