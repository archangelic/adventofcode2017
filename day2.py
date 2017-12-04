#!/usr/bin/env python3

with open('spreadsheet.txt') as f:
    spreadsheet = [sorted([int(i) for i in row.split()]) for row in f.readlines()]

print(sum([row[-1] - row[0] for row in spreadsheet]))

evens = []
for row in spreadsheet:
    for i in row:
        for z in row:
            if i % z == 0 and i != z:
                evens.append([i, z])

print(sum([a // b for a,b in evens]))

