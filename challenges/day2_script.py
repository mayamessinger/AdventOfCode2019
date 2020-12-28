def run(inputFile):
	contents = open(inputFile, "r")
	intcode = contents.read().split(",")

	finishedProgram = findParameters(intcode)

	contents.close()

	print(finishedProgram)

def findParameters(intcode):
	intcode = [int(i) for i in intcode]

	goal = 19690720
	for n in range(0, 99):
		intcode[1] = n

		for v in range(0, 99):
			intcode[2] = v

			if (runIntcode(intcode)[0] == goal):
				return [n, v];

def runIntcode(intcode):
	intcode = [int(i) for i in intcode]

	for i in range(0, len(intcode), 4):
		if (intcode[i] == 1):
			intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
		elif (intcode[i] == 2):
			intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
		elif (intcode[i] == 99):
			return intcode
			

def reverseIntcode(intcode):
	intcode = [int(i) for i in intcode]

	lastCommandIndex = getLastCommandIndex(intcode, 4)
	for i in range(lastCommandIndex, 0, -4):
		if (intcode[i] == 2):
			intcode[intcode[i + 3]] //= (intcode[intcode[i + 1]] * intcode[intcode[i + 2]])
		if (intcode[i] == 1):
			intcode[intcode[i + 3]] -= (intcode[intcode[i + 1]] + intcode[intcode[i + 2]])
	
	return intcode

# find last place where 99 is in a command position (index of 99 must be a multiple of commandSpacing)
def getLastCommandIndex(intcode, commandSpacing):
	maxCommandIndex = commandSpacing * ((len(intcode) - 1)//commandSpacing)

	for i in range(maxCommandIndex, 0, -4):
		if (intcode[i] == 99):
			return i

run("../inputs/day2_input.txt")