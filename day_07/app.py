#!/usr/bin/env python3

from itertools import product
import sys

with open(sys.argv[1]) as f:
    data = [row.split(': ') for row in f.read().strip().split('\n')]

# Some data preprocessing
for row in data:
    row[0] = int(row[0])
    row[1] = [int(i) for i in row[1].split()]

test_sum = 0
for target, numbers in data:
    for operators in product('+*', repeat=len(numbers)-1):
        value = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '*':
                value *= numbers[i+1]
            elif operators[i] == '+':
                value += numbers[i+1]
        if value == target:
            test_sum += value
            break

print(f"Test value sum: {test_sum}")
