#!/usr/bin/env python3

import re
import sys

def get_rows(text):
    """Generator that yields rows from text content in eight orthogonal directions.

    Args:
        text (str): contiguous string of text data, with each row separated by newlines;
            string may contain trailing newlines.
    """
    
    # Quick check to get height, width, and validate we have a rectangle of data
    data = text.strip().split()
    height = len(data)
    width = len(data[0])
    for row in data:
        assert(len(row) == width)
    
    # Yield data in cardinal directions
    for row in data:
        yield row
        yield row[::-1]
    for i in range(width):
        row = []
        for j in range(height):
            row.append(data[j][i])
        row = ''.join(row)
        yield row
        yield row[::-1]
    
    # Yield diagonals
    for i in range(width):
         # Down-right and up-left (from top)
        row = []
        for j in range(0, width - i):
            row += data[j][i + j]
        row = ''.join(row)
        yield row
        yield row[::-1]
        
        # Up-right and down-left (from top)
        row = []
        for j in range(i, -1, -1):
            row += data[j][i - j]
        row = ''.join(row)
        yield row
        yield row[::-1]

    for i in range(1, height):
         # Down-right and up-left (from left)
        row = []
        for j in range(0, height - i):
            row += data[i+j][j]
        row = ''.join(row)
        yield row
        yield row[::-1]

        row = []
        # for j in range(i, height):
        #     row += data[j][width-j]
        for j in range(0, height-i):
            row += data[i+j][width-j-1]
        row = ''.join(row)
        yield row
        yield row[::-1]

with open(sys.argv[1]) as f:
    data = f.read()

count = 0
for row in get_rows(data):
    count += len(re.findall('XMAS', row))

print(f"Count: {count}")

# Second star challenge isn't compatible with the get_rows() solution
# gonna do a simple grid search instead
grid = data.strip().split()

height = len(grid)
width = len(grid[0])

count = 0
for h in range(1, height - 1):
    for w in range(1, width - 1):
        # (h,w) represents the center of the cross
        if grid[h][w] != 'A':
            continue
        corners = grid[h-1][w-1] + grid[h-1][w+1] + grid[h+1][w-1] + grid[h+1][w+1]
        if corners in ['MSMS', 'SMSM', 'MMSS', 'SSMM']:
            count += 1

print(f"X-MAS count: {count}")
