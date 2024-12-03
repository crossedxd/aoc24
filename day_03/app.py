#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    data = f.read()

result = 0
for match in re.findall("mul\((\d+),(\d+)\)", data):
    result += int(match[0]) * int(match[1])

print(f"Result: {result}")

result = 0
enabled = True
for match in re.findall(
    "(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))",
    data
):
    if match[3] == "do()":
        enabled = True
    elif match[4] == "don't()":
        enabled = False
    else:
        if enabled:
            result += int(match[1]) * int(match[2])

print(f"Enabled result: {result}")
