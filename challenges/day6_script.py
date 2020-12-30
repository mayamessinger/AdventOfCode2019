from enum import Enum
import re

class Node:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent

def run(input_file):
	contents = open(input_file, "r")
	orbit_strings = contents.read().split("\n")
	contents.close()

	orbits = parse_orbits(orbit_strings)
	end_node = breadth_first_search(orbits, "YOU", "SAN")
	num_switches = get_num_switches(end_node, "YOU", "SAN")

	print(num_switches)

def parse_orbits(orbit_strings):
	orbits = dict()

	for orbit in orbit_strings:
		orbit_objects = re.search("^([A-Z0-9]+)\)([A-Z0-9]+)$", orbit)
		base = orbit_objects.group(1)
		orbiter = orbit_objects.group(2)

		if base not in orbits:
			orbits[base] = {orbiter}
		elif base in orbits:
			orbits[base].add(orbiter)

		if orbiter not in orbits:
			orbits[orbiter] = {base}
		elif orbiter in orbits:
			orbits[orbiter].add(base)

	return orbits

def breadth_first_search(orbits, start, end):
	start_node = Node(start, None)

	discovered = set([start_node])
	to_visit = [start_node]

	while len(to_visit) != 0:
		curr_obj = to_visit.pop()

		if curr_obj.name == end:
			return curr_obj

		for adjacent_obj in orbits[curr_obj.name]:
			if adjacent_obj not in map(lambda d: d.name, discovered):
				adjacent_node = Node(adjacent_obj, curr_obj)

				discovered.add(adjacent_node)
				to_visit.append(adjacent_node)

def get_num_switches(node, start, end):
	num_mintermediate = 0

	curr_node = node
	while curr_node.parent:
		if (curr_node.name not in [start, end]):
			num_mintermediate += 1
		curr_node = curr_node.parent

	return num_mintermediate - 1 # 1 less switch than objects

run("../inputs/day6_input.txt")