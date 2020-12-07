def run(inputFile):
	contents = open(inputFile, "r")
	finishedProgram = runIntcode(contents.read().split(","))

	print(finishedProgram)


def runIntcode(intcode):
	intcode = [int(i) for i in intcode]

	for i in range(0, len(intcode), 4):
		if (intcode[i] == 1):
			intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
		elif (intcode[i] == 2):
			intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
		elif (intcode[i] == 99):
			return intcode

run("day2_input.txt")