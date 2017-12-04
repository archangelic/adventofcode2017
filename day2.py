#!/usr/bin/env python3

with open('spreadsheet.txt') as f:
    rows = [row.split() for row in f.readlines()]

spreadsheet = []
for row in rows:
    r = sorted([int(i) for i in row])
    spreadsheet.append(r)

checks = [row[-1] - row[0] for row in spreadsheet]
print(sum(checks))

evens = []
for row in spreadsheet:
    for i in row:
        for z in row:
            if i % z == 0 and i != z:
                evens.append([i, z])

divs = [a // b for a,b in evens]
print(sum(divs))
