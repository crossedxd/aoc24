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

total = 0
for target, numbers in data:
    for operators in product('+*|', repeat=len(numbers)-1):
        nums = [i for i in numbers]
        ops = list(operators)
        while ops:
            a = nums.pop(0)
            b = nums.pop(0)
            op = ops.pop(0)
            if op == '+':
                a += b
            elif op == '*':
                a *= b
            elif op == '|':
                a = int(f'{a}{b}')
            nums.insert(0, a)
        if target == nums[0]:
            total += target
            break

print(f"Total calibration result: {total}")
