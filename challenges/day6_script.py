from enum import Enum
import re

def run(input_file):
	contents = open(input_file, "r")
	orbit_strings = contents.read().split("\n")
	contents.close()

	orbits = parse_orbits(orbit_strings)
	all_orbits = get_all_orbits(orbits)
	orbit_count = get_orbit_count(all_orbits)

	print(orbit_count)

def parse_orbits(orbit_strings):
	orbits = dict()

	for orbit in orbit_strings:
		orbit_objects = re.search("^([A-Z0-9]+)\)([A-Z0-9]+)$", orbit)
		base = orbit_objects.group(1)
		orbiter = orbit_objects.group(2)

		if base not in orbits:
			orbits[base] = {orbiter}

		if base in orbits:
			orbits[base].add(orbiter)

	return orbits

def get_all_orbits(orbits):
	all_orbits = dict()

	for key in orbits:
		all_orbits[key] = set()
		add_indirect_orbits(all_orbits[key], key, orbits)

	return all_orbits

def add_indirect_orbits(parent_orbits, obj, orbits):
	if obj not in orbits.keys():
		return

	for val in orbits[obj]:
		parent_orbits.add(val)

		if val in orbits.keys():
			add_indirect_orbits(parent_orbits, val, orbits)

def get_orbit_count(orbits):
	total_orbits = 0

	for key in orbits:
		total_orbits += len(orbits[key])

	return total_orbits

run("../inputs/day6_input.txt")