import numpy
import re

a = numpy.zeros((100, 100, 100), numpy.int8)
with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.findall("\d+", line)
        a[int(tokens[0]), int(tokens[1]), int(tokens[2])] = 1
f.close()
sum = 0
for x in range(50):
    for y in range(50):
        for z in range(50):
            if a[x, y, z] == 1:
                if a[x + 1, y, z] == 0:
                    sum += 1
                if a[x - 1, y, z] == 0:
                    sum += 1
                if a[x, y + 1, z] == 0:
                    sum += 1
                if a[x, y - 1, z] == 0:
                    sum += 1
                if a[x, y, z + 1] == 0:
                    sum += 1
                if a[x, y, z - 1] == 0:
                    sum += 1

def neighbor(cell, a):
    neighbors = []
    if cell[0] - 1 >= 0:
        neighbors.append([cell[0] - 1, cell[1], cell[2]])
    if cell[0] + 1 < len(a):
        neighbors.append([cell[0] + 1, cell[1], cell[2]])
    if cell[1] - 1 >= 0:
        neighbors.append([cell[0], cell[1] - 1, cell[2]])
    if cell[1] + 1 < len(a):
        neighbors.append([cell[0], cell[1] + 1, cell[2]])
    if cell[2] - 1 >= 0:
        neighbors.append([cell[0], cell[1], cell[2] - 1])
    if cell[2] + 1 < len(a):
        neighbors.append([cell[0], cell[1], cell[2] + 1])
    return neighbors

active_cells = [[0, 0, 0]]
while active_cells:
    new_active_cells = []
    for cell in active_cells:
        for nh in neighbor(cell, a):
            if a[nh[0], nh[1], nh[2]] == 0:
                a[nh[0], nh[1], nh[2]] = 2
                new_active_cells.append(nh)
    active_cells = new_active_cells

for x in range(50):
    for y in range(50):
        for z in range(50):
            if a[x, y, z] == 0:
                if a[x + 1, y, z] == 1:
                    sum -= 1
                if a[x - 1, y, z] == 1:
                    sum -= 1
                if a[x, y + 1, z] == 1:
                    sum -= 1
                if a[x, y - 1, z] == 1:
                    sum -= 1
                if a[x, y, z + 1] == 1:
                    sum -= 1
                if a[x, y, z - 1] == 1:
                    sum -= 1
print(sum)