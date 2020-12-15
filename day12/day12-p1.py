#!/bin/python38

from math import sin, cos, pi


DTOR = pi * 2 / 360.


class Ferry:
	dir_mappings = {
		'E': 90,
		'W': 270,
		'N': 0,
		'S': 180,
	}

	def __init__(self):
		self.x = 0
		self.y = 0
		self.facing = self.dir_mappings['E']

	def move(self, direction: int, dist: int):
		self.x += sin(direction * DTOR) * dist
		self.y += cos(direction * DTOR) * dist
		# print(self.x, self.y)

	def turn(self, direction: str, degrees: int):
		if direction == 'R':
			self.facing += degrees
		elif direction == 'L':
			self.facing -= degrees
		else:
			raise ValueError(f'Unknown direction {direction}')

	def move_card(self, cardinal: str, dist: int):
		self.move(self.dir_mappings[cardinal], dist)

	def move_forward(self, dist: int):
		self.move(self.facing, dist)

	def parse(self, command: str):
		action = command[0]
		value = int(command[1:])

		if action in self.dir_mappings:
			self.move_card(action, value)
		elif action in ['R', 'L']:
			self.turn(action, value)
		elif action == 'F':
			self.move_forward(value)
		else:
			raise ValueError(f'Unknown action {action}')

	def get_taxicab(self):
		return abs(self.x) + abs(self.y)


ship = Ferry()

if True:
	with open('./day12/day12.data', 'r') as f:
		commandstr = f.read()
else:
	commandstr = '''
F10
N3
F7
R90
F11
'''

commands = [command for command in commandstr.split('\n') if command != '']

for command in commands:
	ship.parse(command)

print(f'Ship ends at ({ship.x}, {ship.y})')
print(f'Taxicab dist: {int(ship.get_taxicab() + 0.5)}')

