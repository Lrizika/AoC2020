#!/bin/python38

FLOOR = object()
SEAT_EMPTY = object()
SEAT_FULL = object()
print(f'FLOOR: {FLOOR}')
print(f'SEAT_EMPTY: {SEAT_EMPTY}')
print(f'SEAT_FULL: {SEAT_FULL}')


def get_layout(str_layout: str) -> list:
	layout = []
	for str_line in str_layout.split('\n'):
		if str_line == '':
			continue

		line = []
		for char in str_line:
			if char == 'L':
				line.append(SEAT_EMPTY)
			elif char == '.':
				line.append(FLOOR)
			elif char == '#':
				line.append(SEAT_FULL)
			else:
				raise ValueError(
					f'Unexpected character {char} in layout string'
				)
		layout.append(line)
	return layout


def get_layout_str(layout: list) -> str:
	str_lines = []
	for line in layout:
		str_line = ''
		for item in line:
			str_line = str_line + {
				SEAT_EMPTY: 'L',
				FLOOR: '.',
				SEAT_FULL: '#',
			}[item]
		str_lines.append(str_line)
	return '\n'.join(str_lines)


def step_layout(layout: list) -> list:
	DIRECTIONS = [
		( 0,  1),
		( 1,  1),
		( 1,  0),
		( 1, -1),
		( 0, -1),
		(-1, -1),
		(-1,  0),
		(-1,  1),
	]
	new_layout = [line[:] for line in layout]
	for y in range(len(layout)):
		for x in range(len(layout[y])):
			if layout[y][x] is FLOOR:
				continue

			adjacent_count = 0
			for direction in DIRECTIONS:
				dist = 1
				while True:
					x_adj = x + (direction[0] * dist)
					y_adj = y + (direction[1] * dist)
					if y_adj < 0 or y_adj >= len(layout):
						break
					elif x_adj < 0 or x_adj >= len(layout[y_adj]):
						break
					elif layout[y_adj][x_adj] is SEAT_EMPTY:
						break
					elif layout[y_adj][x_adj] is SEAT_FULL:
						adjacent_count += 1
						break

					dist += 1

			if adjacent_count == 0:
				new_layout[y][x] = SEAT_FULL
			elif adjacent_count >= 5:
				new_layout[y][x] = SEAT_EMPTY

	return new_layout


if True:
	with open('./day11.data', 'r') as f:
		text_layout = f.read()
else:
	text_layout = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''

layout = get_layout(text_layout)

for i in range(1000):
	print(f'Iteration {i}:')
	print(get_layout_str(layout))
	print('=====================')
	new_layout = step_layout(layout)
	if new_layout == layout:
		break
	else:
		layout = new_layout

count = 0
for line in new_layout:
	for pos in line:
		if pos is SEAT_FULL:
			count += 1
print(f'{count} seats are occupied.')

