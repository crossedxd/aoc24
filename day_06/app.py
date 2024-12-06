#!/usr/bin/env python3

import sys

def find_elements(s, grid):
    """
    Searches the grid for any of the characters appearing in s and returns them as a set
    of coordinates.
    """
    coords = set()
    for h in range(len(grid)):
        for w in range(len(grid[0])):
            if grid[h][w] in s:
                coords.add((h, w))
    return coords

def hoist_guard(grid):
    '''
    Removes guard indicator from new grid and returns its current coordinates.
    '''
    # coords = find_elements('^<>v', grid).pop()
    for orientation in '^<>v':
        coords = find_elements(orientation, grid).pop()
        if coords:
            grid[coords[0]][coords[1]] = '.'
            return orientation, coords
    # return coords

with open(sys.argv[1]) as f:
    grid = [list(row) for row in f.read().strip().split('\n')]

height = len(grid)
width = len(grid[0])
guard_info = hoist_guard(grid)
print(f"Guard info: {guard_info}")

on_map = True
p = guard_info[0]
h, w = guard_info[1]
visited = {guard_info[1]}
obstacles = find_elements('#', grid)
while on_map:
    if p == '^':
        if h == 0:
            on_map = False
        elif (h - 1, w) in obstacles: # Blocked, so rotate
            p = '>'
        else: # Take a step
            h -= 1
    elif p == '>':
        if w == width - 1:
            on_map = False
        elif (h, w + 1) in obstacles: # Blocked, so rotate
            p = 'v'
        else: # Take a step
            w += 1
    elif p == 'v':
        if h == height - 1:
            on_map = False
        elif (h + 1, w) in obstacles: # Blocked, so rotate
            p = '<'
        else: # Take a step
            h += 1
    elif p == '<':
        if w == 0:
            on_map = False
        elif (h, w - 1) in obstacles: # Blocked, so rotate
            p = '^'
        else: # Take a step
            w -= 1
    visited.add((h, w))

print(f"Visited count: {len(visited)}")
