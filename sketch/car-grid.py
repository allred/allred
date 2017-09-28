#!/usr/bin/env python
# given a grid m by n, position x y, and steps
# turn the car clockwise and move if cell is 0
# turn the car counter-clockwise and move if cell is 1
# flip the cell you just left
import pprint

pp = pprint.PrettyPrinter()
last_grid = []
location = {}

def grid_step(grid):
    for i, row in enumerate(grid):
        if location['y'] == len(grid) - (i + 1):
            if row[location['x']] == '>':
                if row[location['x'] + 1] == 0:
                    row[location['x']] = 1
                    row[location['x'] + 1] = 'v'
                else:
                    row[location['x']] = 0
                    row[location['x'] + 1] = '^'
                location['x'] += 1
                break
            if row[location['x']] == 'v':
                if grid[i + 1][location['x']] == 0:
                    grid[i][location['x']] = 1
                    grid[i + 1][location['x']] = '<'
                else:
                    grid[i][location['x']] = 0
                    grid[i + 1][location['x']] = '>'
                location['y'] -= 1
                break
            if row[location['x']] == '<':
                if row[location['x'] - 1] == 0:
                    row[location['x']] = 1
                    row[location['x'] - 1] = '^'
                else:
                    row[location['x']] = 0
                    row[location['x'] - 1] = 'v'
                location['x'] -= 1
                break
            if row[location['x']] == '^':
                if grid[i - 1][location['x']] == 0:
                    grid[i][location['x']] = 1
                    grid[i - 1][location['x']] = '>'
                else:
                    grid[i][location['x']] = 0
                    grid[i - 1][location['x']] = '<'
                location['y'] += 1
                break
    last_grid = grid
    pp.pprint({'step': last_grid})

def initialize_grid(m, n, x, y):
    location['x'] = x
    location['y'] = y
    for z in reversed(range(0, m)):
        ary = [0] * n
        if z == x:
            ary[y] = '>'
        last_grid.append(ary)

def output_grid(m, n, x, y, num_steps):
    if len(last_grid) == 0:
        initialize_grid(m, n, x, y)
    for s in range(0, num_steps):
        grid_step(last_grid)
    return last_grid

pp.pprint({'output': output_grid(5, 5, 1, 1, 4)})
