def run(inputFile):
	contents = open(inputFile, "r")
	totalFuelReq = calcSpacecraftFuel(contents.read().split("\n"))

	print(totalFuelReq)


def calcSpacecraftFuel(moduleMasses):
	totalFuel = 0;

	for mass in moduleMasses:
		totalFuel += calcModuleFuel(mass)

	return totalFuel

def calcModuleFuel(massString):
	mass = int(massString)

	return mass//3 - 2

run("day1_input.txt")