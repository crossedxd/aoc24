#!/usr/bin/env python3

import sys
from collections import Counter


"""
For the second part, I'd like to randomly drop boxes on the grid and test them to see
if we've trapped them in a loop.  I think it may be more efficient to try to work this 
out as an array of rectangle corners, but it's simpler to just run the tests.

First, it might be helpful to refactor things a bit (Grid class, simulate() function)
"""

class Map:

    vectors = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = self.hoist_guard()

    def find_elements(self, s):
        """
        Searches the grid for any of the characters appearing in s and returns them as a
        set of coordinates.
        """
        coords = set()
        for h in range(self.height):
            for w in range(self.width):
                if self.get_pos(h, w) in s:
                    coords.add((h, w))
        return coords
    
    def get_pos(self, h, w):
        return self.grid[h][w]
    
    def set_pos(self, h, w, c):
        self.grid[h][w] = c

    def hoist_guard(self):
        '''Removes guard indicator from grid and returns its current coordinates.'''
        # for orientation in '^<>v':
        for orientation in Map.vectors:
            coords = self.find_elements(orientation).pop()
            if coords:
                self.set_pos(coords[0], coords[1], '.')
                return orientation, coords
        return None, None
    
    def navigate(self):
        '''
        Uses stored grid and start info to simulate navigating the map, until either:
        1) we leave the map, or
        2) we revisit a coordinate we've already visited
        '''
        on_map = True
        rot = self.start[0]
        pos = self.start[1]
        visited = {self.start[1]}
        tread_count = Counter()
        obstacles = self.find_elements('#')
        # print(obstacles)
        is_navigating = True
        while is_navigating:
            # Loop until we either leave the map or retrace our steps
            for orientation in Map.vectors:
                if rot == orientation:
                    new_pos = tuple(map(sum, zip(pos, Map.vectors[orientation])))
                    # Did we leave the map?
                    if (new_pos[0] < 0 or
                        new_pos[1] < 0 or
                        new_pos[0] > self.height - 1 or
                        new_pos[1] > self.width - 1):
                        on_map = False
                        is_navigating = False
                        break
                    # Have we already been here?
                    if new_pos in visited:
                        tread_count[new_pos] += 1
                        if tread_count[new_pos] == 3:
                            on_map = True
                            is_navigating = False
                            break
                    # Did we collide with an object?
                    if new_pos in obstacles:
                        k = list(Map.vectors.keys())
                        rot = k[(k.index(rot) + 1) % len(k)]
                    else:
                        pos = new_pos
                        visited.add(pos)
            pass
        return on_map, visited


with open(sys.argv[1]) as f:
    m = Map([list(row) for row in f.read().strip().split('\n')])

print(f"Visited count: {len(m.navigate()[1])}")
