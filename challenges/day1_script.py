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

	fuelReq = mass//3 - 2;

	if (fuelReq <= 0):
		return 0;

	return fuelReq + calcModuleFuel(fuelReq)

run("../inputs/day1_input.txt")