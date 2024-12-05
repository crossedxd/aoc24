#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    raw_rules, raw_orders = f.read().split('\n\n')

rules = defaultdict(list)
for i in raw_rules.split():
    a,b = i.split('|')
    rules[a].append(b)

orders = [row.split(',') for row in raw_orders.split('\n')[:-1]]

total = 0
incorrect_orders = []
for order in orders:
    is_valid = True
    for i, base in enumerate(order):
        for j, update in enumerate(order):
            if j < i: # Occurs before
                if update in rules[base]:
                    is_valid = False
            elif j > i: # Occurs after (one of these checks was unnecessary, I think)
                if base in rules[update]:
                    is_valid = False
    # Get the weird middle page num requirement
    if is_valid:
        mid = int(len(order) / 2)
        total += int(order[mid])
    else:
        incorrect_orders.append(order)

print(f"Total: {total}")

# The solution below is really, really inefficient (took 30-60s to solve part 2)
# I'd like to rewrite it and convert the rules into a linked list or something,
# but I actually, really don't want to touch it again at the moment
corrected_orders = []
corrected_total = 0
for order in incorrect_orders:
    corrected_order = []
    while order:
        changed = False
        for i, val in enumerate(order):
            if order[0] in rules[val]:
                order.insert(i, order.pop(0))
                changed = True
                break
        if not changed:
            corrected_order.append(order.pop(0))
    mid = int(len(corrected_order) / 2)
    corrected_total += int(corrected_order[mid])

print(f"Corrected total: {corrected_total}")
