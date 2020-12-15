#!/bin/python38

from math import sin, cos, pi


DTOR = pi * 2 / 360.
RTOD = 360. / pi / 2


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
		self.wp_x = 10
		self.wp_y = 1

	def move_wp(self, direction: int, dist: int):
		self.wp_x += sin(direction * DTOR) * dist
		self.wp_y += cos(direction * DTOR) * dist

	def turn_wp(self, direction: str, degrees: int):
		if degrees > 90:
			self.turn_wp(direction, degrees - 90)

		old_x = self.wp_x
		old_y = self.wp_y
		if direction == 'R':
			self.wp_x = old_y
			self.wp_y = old_x * -1
		elif direction == 'L':
			self.wp_x = old_y * -1
			self.wp_y = old_x
		else:
			raise ValueError(f'Unknown direction {direction}')

	def move_wp_card(self, cardinal: str, dist: int):
		self.move_wp(self.dir_mappings[cardinal], dist)

	def move_forward(self, dist: int):
		for i in range(dist):
			self.x += self.wp_x
			self.y += self.wp_y

	def parse(self, command: str):
		action = command[0]
		value = int(command[1:])

		if action in self.dir_mappings:
			self.move_wp_card(action, value)
		elif action in ['R', 'L']:
			self.turn_wp(action, value)
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

