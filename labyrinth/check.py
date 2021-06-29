#!/usr/bin/python
 
import sys
import json
from collections import Counter
 
# open grid file
with open(sys.argv[1]) as f:
  lines = [line.rstrip('\n') for line in f]
 
# m = width and n = height
grid = lines
m = len(lines[0])
n = len(lines)
 
print('Grid')
for row in range(n):
  print(grid[row])
print()

all_checks_passed = True
for i in range(n):
    counts = Counter(grid[i])
    for k, v in counts.items():
        if v != 1 and k!='-':
            print(f'{k} is repeated {v} times in row {i + 1}')
            all_checks_passed = False

for j in range(m):
    col = []
    for i in range(n):
        col.append(grid[i][j])
    counts = Counter(col)
    for k, v in counts.items():
        if v != 1 and k !='-':
            print(f'{k} is repeated {v} times in column {j + 1}')
            all_checks_passed = False


unique_letters = set()
'''
for row in grid:
    unique_letters.update(row)


print(unique_letters)
for i in range(n):
    for letter in unique_letters:
        if letter not in grid[i]:
            print(f'{letter} not present in row {i + 1}')
            all_checks_passed = False

for j in range(m):
    col = []
    for i in range(n):
        col.append(grid[i][j])
    for letter in unique_letters:
        if letter not in col:
            print(f'{letter} not present in column {j + 1}')
            all_checks_passed = False

'''

if all_checks_passed:
    print('All checks passed')

