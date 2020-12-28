import re

def run(input_file):
	contents = open(input_file, "r")
	pw_range_string = contents.read()
	contents.close()

	pw_range = parse_range(pw_range_string)
	num_matches = len(get_valid_passwords(pw_range))

	print(num_matches)

def parse_range(pw_range_string):
	range_min = re.search("([0-9]+)-", pw_range_string).group(1)
	range_max = re.search("-([0-9]+)", pw_range_string).group(1)

	return (int(range_min), int(range_max))

def get_valid_passwords(pw_range):
	valids = []

	for i in range(pw_range[0], pw_range[1]):
		strI = str(i)
		if (is_valid_pw((strI))):
			valids.append(i)

	return valids

def is_valid_pw(string):
	return (
		len(string) == 6
		and always_increases(string)
		and adjacent_same(string)
		)

def always_increases(string):
	for i in range(1, 6):
		if (string[i] < string[i-1]):
			return False

	return True

def adjacent_same(string):
	for i in range(1, 6):
		if (string[i] == string[i-1]):
			return True

	return False

run("../inputs/day4_input.txt")