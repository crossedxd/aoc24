#!/usr/bin/env python3

import sys

"""
Puzzle input looks like this:
3   4
4   3
2   5
1   3
3   9
3   3

Goal is to get the sum of differences between each (min(listA), min(listB)).

So we'd look at these pairs:
abs(1 - 3) = 2
abs(2 - 3) = 1
abs(3 - 3) = 0
abs(3 - 4) = 1
abs(3 - 5) = 2
abs(4 - 9) = 5

And add them all up:
2 + 1 + 0 + 1 + 2 + 5 = 11
"""

left = list()
right = list()
with open(sys.argv[1]) as f:
    for row in f.readlines():
        a,b = row.split()
        left.append(int(a))
        right.append(int(b))

left = sorted(left)
right = sorted(right)
sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)
