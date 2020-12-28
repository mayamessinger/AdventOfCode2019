import re

# start and end points are "oriented" such that start coordiate will always be
# smaller than end coordinate (smaller == lower/further left)
class Path:
	def __init__(self, x1, y1, x2, y2):
		self.start = Coordinate(x1, y1)
		self.end = Coordinate(x2, y2)
		self.low = Coordinate(min(x1, x2), min(y1, y2))
		self.high = Coordinate(max(x1, x2), max(y1, y2))

	def __eq__(self, obj):
		return isinstance(obj, Path) and self.low == obj.low and self.high == obj.high

	def distance(self):
		return max(abs(self.high.x - self.low.x), abs(self.high.y - self.low.y))

# all x and y values are relative to the central port (0, 0)
class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, obj):
		return isinstance(obj, Coordinate) and self.x == obj.x and self.y == obj.y

	def distanceFromCenter(self):
		return abs(self.x) + abs(self.y)

class Intersection:
	def __init__(self, coordinate, pathLengths):
		self.coordinate = coordinate
		self.steps = pathLengths

def run(inputFile):
	contents = open(inputFile, "r")
	wireMoves = contents.read().split("\n")
	contents.close()

	allPaths = mapAllWires(wireMoves)
	intersections = getIntersections(allPaths)

	print(getClosestIntersection(intersections).steps)

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

	aSteps = 0
	bSteps = 0
	for a in range(0, len(wireA)):
		for b in range(0, len(wireB)):
			cross = crosses(wireA[a], wireB[b])
			if (cross is not None):
				intersections.append(Intersection(cross, aSteps + bSteps + intersectionDistance(cross, wireA[a], wireB[b])))

			bSteps += wireB[b].distance()

		aSteps += wireA[a].distance()
		bSteps = 0

	return intersections

def crosses(pathA, pathB):
	if (pathA.low.x <= pathB.low.x <= pathA.high.x
		and pathB.low.y <= pathA.low.y <= pathB.high.y):
			return Coordinate(pathB.low.x, pathA.low.y)

	if (pathA.low.y <= pathB.low.y <= pathA.high.y
		and pathB.low.x <= pathA.low.x <= pathB.high.x):
			return Coordinate(pathA.low.x, pathB.low.y)

def intersectionDistance(intersection, pathA, pathB):
	return max(abs(intersection.x - pathA.start.x), abs(intersection.y - pathA.start.y)) + max(abs(intersection.x - pathB.start.x), abs(intersection.y - pathB.start.y))


def getClosestIntersection(intersections):
	intersections = list(filter(lambda i: i.coordinate != Coordinate(0, 0), intersections))

	return min(intersections, key=lambda inter: inter.steps)


run("../inputs/day3_input.txt")