#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = f.read().strip()

def map_disk(disk_data):
    is_data = True
    curr_id = 0
    disk_map = []
    for block in disk_data:
        if is_data:
            for i in range(int(block)):
                disk_map.append(str(curr_id))
            curr_id += 1
            is_data = False
        else:
            for i in range(int(block)):
                disk_map.append('.')
            is_data = True
    return disk_map

def fragment_disk(disk_map):
    free_index = 0
    data_index = len(disk_map) - 1
    while True:
        # Get next free/data
        while disk_map[free_index] != '.':
            free_index += 1
        while disk_map[data_index] == '.':
            data_index -= 1
        if free_index >= data_index:
            break
        disk_map[free_index] = disk_map[data_index]
        disk_map[data_index] = '.'
    return disk_map

def calculate_checksum(disk_map):
    total = 0
    for i in range(len(disk_map)):
        if disk_map[i] != '.':
            total += i * int(disk_map[i])
    return total

print(f'Filesystem checksum: {calculate_checksum(fragment_disk(map_disk(data)))}')

# Was gonna do part 2 fancy w/ linked lists, but when I got home I decided to
# do it with a simple tuple array or something like that

"""
I was originally going to complete the second star part using a linked list or something
like that, but I decided I wanted to do something "simpler" instead. You'll see below
how that quickly spiraled out of control, and how how I skipped over a handful of things
that would have improved the overall performance.

In the end, I just wanted to commit to the bit that was my disk initialization.

"Everyone knows that debugging is twice as hard as writing a program in the first place.
So if you're as clever as you can be when you write it, how will you ever debug it?"

- Brian Kernighan, 1974
"""

# Array of (id, size, is_empty) tuples
disk = [(int(i * 0.5) if i % 2 == 0 else None, int(data[i]), i % 2 != 0) for i in range(len(data))]

def print_disk(disk):
    for i in disk:
        if i[2]:
            c = '.'
        else:
            c = str(i[0])
        for n in range(i[1]):
            print(c, end='')
    print()

skipped_chunks = set()
while True:
    # Find index of last non-free chunk (data)
    data_chunk = None
    for i in range(len(disk) - 1, 0, -1):
        if not disk[i][2] and disk[i][0] not in skipped_chunks:
            data_size = disk[i][1]
            data_chunk = i
            break

    # Find index first free chunk of >= data chunk's size
    free_chunk = None
    for i in range(len(disk)):
        if disk[i][2] and disk[i][1] >= data_size:
            free_size = disk[i][1]
            free_chunk = i
            break

    # If we're out of data_chunks, we're done
    if not data_chunk:
        break
    
    # If we couldn't find an appropriate free chunk, skip the data chunk
    if not free_chunk:
        skipped_chunks.add(disk[data_chunk][0])
        continue

    # If free chunk occurs later than data chunk, skip the data chunk
    if free_chunk > data_chunk:
        skipped_chunks.add(disk[data_chunk][0])
        continue

    # If they're not the same size, break off excess free space
    if free_size > data_size:
        disk[free_chunk] = (None, data_size, True)
        disk.insert(free_chunk + 1, (None, free_size - data_size, True))
        data_chunk += 1

    # Swap the two chunks
    disk[free_chunk], disk[data_chunk] = disk[data_chunk], disk[free_chunk]

checksum = 0
i = 0
for block in disk:
    for _ in range(block[1]):
        if not block[2]:
            checksum += i * block[0]
        i += 1

print(f'Updated checksum: {checksum}')
