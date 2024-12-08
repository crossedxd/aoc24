#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import combinations

class Node:

    def __init__(self, h, w):
        self.h = h
        self.w = w

    def delta(self, other):
        return Node(other.h - self.h, other.w - self.w)

    def antinodes(self, other):
        delta = self.delta(other)
        return [
            Node(other.h + delta.h, other.w + delta.w),
            Node(self.h - delta.h, self.w - delta.w)
        ]

    def t_freq_antinodes(self, other, height, width):
        delta = self.delta(other)
        antinodes = set()
        h, w = self.h, self.w
        while (
            h >= 0 and
            w >= 0 and
            h < height and
            w < width):
            antinodes.add(Node(h, w))
            h -= delta.h
            w -= delta.w
        h, w = self.h, self.w
        while (
            h >= 0 and
            w >= 0 and
            h < height and
            w < width):
            antinodes.add(Node(h, w))
            h += delta.h
            w += delta.w
        return antinodes

    def __repr__(self):
        return f'Node({self.h},{self.w})'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return self.h == other.h and self.w == other.w

with open(sys.argv[1]) as f:
    data = f.read().strip().split('\n')

height = len(data)
width = len(data[0])

nodes = defaultdict(set)
antinodes = set()
for h in range(height):
    for w in range(width):
        if data[h][w] != '.':
            nodes[data[h][w]].add(Node(h, w))

for freq in nodes:
    for a, b in combinations(nodes[freq], 2):
        [antinodes.add(i) for i in a.antinodes(b)]

unique_locations = 0
for antinode in antinodes:
    if (antinode.h >= 0 and
        antinode.w >= 0 and
        antinode.h < height and
        antinode.w < width):
        unique_locations += 1

print(f"Unique locations: {unique_locations}")

t_freq_antinodes = set()
for freq in nodes:
    for a, b in combinations(nodes[freq], 2):
        [t_freq_antinodes.add(i) for i in a.t_freq_antinodes(b, height, width)]

t_freq_locations = 0
for antinode in t_freq_antinodes:
    if (antinode.h >= 0 and
        antinode.w >= 0 and
        antinode.h < height and
        antinode.w < width):
        t_freq_locations += 1

print(f"T-frequency locations: {t_freq_locations}")

# # This was a quick renderer for the test maps
# for h in range(height):
#     for w in range(width):
#         if Node(h,w) in t_freq_antinodes:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()
