#!/usr/bin/python

import sys
import json

# open grid file
with open(sys.argv[1]) as f:
  lines = [line.rstrip('\n') for line in f]

# m = width and n = height, w is full padded width
grid = lines
m = len(lines[0])
n = len(lines)
w=m*3


print('Grid')
for row in range(n):
  print(grid[row])
print()

