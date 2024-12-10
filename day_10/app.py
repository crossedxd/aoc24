#!/usr/bin/env python3

import sys

class TrailMap:
    def __init__(self, data):
        self.map = [[i for i in row] for row in data.strip().split('\n')]
        self.height = len(self.map)
        self.width = len(self.map[0])

    def starting_locations(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.map[h][w] == '0':
                    yield (h, w)
    
    def score_trailhead(self, h, w):
        if self.map[h][w] == '9':
            return 1
        count = 0
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if h + dh < 0 or h + dh >= self.height:
                continue
            if w + dw < 0 or w + dw >= self.width:
                continue
            if int(self.map[h + dh][w + dw]) == int(self.map[h][w]) + 1:
                count += self.score_trailhead(h + dh, w + dw)
        return count
    
    def score_visited(self, h, w):
        if self.map[h][w] == '9':
            return {tuple((h, w))}
        visited = set()
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if h + dh < 0 or h + dh >= self.height:
                continue
            if w + dw < 0 or w + dw >= self.width:
                continue
            if int(self.map[h + dh][w + dw]) == int(self.map[h][w]) + 1:
                visited.update(self.score_visited(h + dh, w + dw))
        return visited

with open(sys.argv[1]) as f:
    trail_map = TrailMap(f.read())

trailhead_score_sum = 0
for h, w in trail_map.starting_locations():
    trailhead_score_sum += len(trail_map.score_visited(h, w))

print(f'Trailhead score sum: {trailhead_score_sum}')

trailhead_rating = 0
for h, w in trail_map.starting_locations():
    trailhead_rating += trail_map.score_trailhead(h, w)

print(f'Trailhead rating: {trailhead_rating}')
