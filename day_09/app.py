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
