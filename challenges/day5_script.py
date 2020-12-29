from enum import Enum
import re

class ParameterMode(Enum):
	Position = 0
	Immediate = 1

class Instruction:
	def __init__(self, p3_mode, p2_mode, p1_mode, opcode):
		self.param3_mode = p3_mode
		self.param2_mode = p2_mode
		self.param1_mode = p1_mode
		self.opcode = opcode

	def __str__(self):
		return "p3 {}, p2 {}, p1{}, opcode {}" \
			.format(self.param3_mode, self.param2_mode, self.param1_mode, self.opcode)

def run(input_file):
	contents = open(input_file, "r")
	intcode = contents.read().split(",")
	contents.close()

	intcode = [int(i) for i in intcode]
	run_intcode(intcode, 5)

def run_intcode(intcode, initial_input):
	i = 0;
	while (i < len(intcode)):
		instruction = getModeAndOpcode(intcode[i])
		(param3, param2, param1) = getParameters(intcode, instruction, i)

		if (instruction.opcode == 1):
			intcode[param3] = param2 + param1
			i += 4
		elif (instruction.opcode == 2):
			intcode[param3] = param2 * param1
			i += 4
		elif (instruction.opcode == 3):
			intcode[param1] = initial_input
			i += 2
		elif (instruction.opcode == 4):
			print("value at {} is {}".format(param1, intcode[param1]))
			i += 2
		elif (instruction.opcode == 5):
			if (param1 != 0):
				i = param2
			else:
				i += 3
		elif (instruction.opcode == 6):
			if (param1 == 0):
				i = param2
			else:
				i += 3
		elif (instruction.opcode == 7):
			if (param1 < param2):
				intcode[param3] = 1
			else:
				intcode[param3] = 0
			i += 4
		elif (instruction.opcode == 8):
			if (param1 == param2):
				intcode[param3] = 1
			else:
				intcode[param3] = 0
			i += 4
		elif (instruction.opcode == 99):
			return intcode
		else:
			raise Exception("invalid opcode {} at index {}".format(instruction.opcode, i))

def getModeAndOpcode(instruction):
	instruction = str(instruction).rjust(5, "0")

	param3_mode = int(instruction[0:1]) # not translating to enum
	param2_mode = int(instruction[1:2])
	param1_mode = int(instruction[2:3])
	opcode = int(instruction[3:5])

	return Instruction(param3_mode, param2_mode, param1_mode, opcode)


def getParameters(intcode, instruction, index):
	param3 = None
	param2 = None
	param1 = None

	if (instruction.opcode == 99):
		pass
	elif (instruction.opcode == 3 or instruction.opcode == 4):
		param1 = intcode[index + 1]
	else:
		if (index < len(intcode) - 3):
			param3 = intcode[index + 3]

		if (index < len(intcode) - 2):
			param2 = intcode[intcode[index + 2]] \
				if instruction.param2_mode == ParameterMode.Position.value \
				else intcode[index + 2]

		if (index < len(intcode) - 1):
			param1 = intcode[intcode[index + 1]] \
				if (instruction.param1_mode == ParameterMode.Position.value) \
				else intcode[index + 1]

	return (param3, param2, param1)

run("../inputs/day5_input.txt")