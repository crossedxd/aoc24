#!/usr/bin/env python3

import sys

def is_safe(report):
    is_safe = True
    is_increasing = False
    is_decreasing = False
    for i in range(len(report) - 1):
        delta = report[i] - report[i+1]
        abs_delta = abs(delta)
        if abs_delta < 1 or abs_delta > 3:
            is_safe = False
        if delta > 0:
            is_increasing = True
        if delta < 0:
            is_decreasing = True
    if is_increasing and is_decreasing:
        is_safe = False        
    # print(f"{report}: {'Safe' if is_safe else 'Unsafe'}")
    return is_safe        

with open(sys.argv[1]) as f:
    reports = [
        list(map(int, row.split()))
        for row in f.readlines()
    ]

safe_report_count = 0
for report in reports:
    if is_safe(report):
        safe_report_count += 1

print(f"Safe reports: {safe_report_count}")

def generate_variants(report):
    for i in range(len(report)):
        yield report[0:i] + report[i+1:]

tolerable_report_count = 0
for report in reports:
    for variant in generate_variants(report):
        if is_safe(variant):
            tolerable_report_count += 1
            break

print(f"Tolerable reports: {tolerable_report_count}")
