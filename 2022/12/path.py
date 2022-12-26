from __future__ import annotations
from typing import Any, List
from collections import defaultdict
import math
import heapdict
x = 0
y = 0
def reconstruct_path(came_from: dict, current: tuple) -> List[tuple]:
    total_path = [current]
    while current in came_from.keys():
        current = came_from.get(current)
        total_path.insert(0, current)
    return total_path

def A_Star(start: tuple, goal: tuple, lines):
    openset = heapdict.heapdict()
    came_from = dict()
    gscore = dict()
    gscore[start] = 0
    fscore = dict()
    fscore[start] = 0 # No heuristic lol
    openset[start] = fscore[start]
    status = 0
    while openset:
        current = openset.peekitem()[0]
        if current == goal:
            return reconstruct_path(came_from, current)
        openset.pop(current)
        neighbors = []
        # print(current)
        if current == start:
            if current[0] + 1 < x and ord('a') + 1 >= ord(lines[current[1]][current[0] + 1]):
                neighbors.append((current[0] + 1, current[1]))
            if current[0] - 1 > 0 and ord('a') + 1 >= ord(lines[current[1]][current[0] - 1]):
                neighbors.append((current[0] - 1, current[1]))
            if current[1] + 1 < y and ord('a') + 1 >= ord(lines[current[1] + 1][current[0]]):
                neighbors.append((current[0], current[1] + 1))
            if current[1] - 1 > 0 and ord('a') + 1 >= ord(lines[current[1] - 1][current[0]]):
                neighbors.append((current[0], current[1] - 1))
        else:
            if current[0] + 1 < x and ord(lines[current[1]][current[0]]) + 1 >= ord(lines[current[1]][current[0] + 1]):
                if (current[0] + 1, current[1]) == goal:
                    # print(ord(lines[current[1]][current[0]]))
                    if ord(lines[current[1]][current[0]]) + 1 >= ord('z'):
                        neighbors.append((current[0] + 1, current[1]))
                else:
                    neighbors.append((current[0] + 1, current[1]))
            if current[0] - 1 > 0 and ord(lines[current[1]][current[0]]) + 1 >= ord(lines[current[1]][current[0] - 1]):
                if (current[0] - 1, current[1]) == goal:
                    if ord(lines[current[1]][current[0]]) + 1 >= ord('z'):
                        neighbors.append((current[0] - 1, current[1]))
                else:
                    neighbors.append((current[0] - 1, current[1]))
            if current[1] + 1 < y and ord(lines[current[1]][current[0]]) + 1 >= ord(lines[current[1] + 1][current[0]]):
                if (current[0], current[1] + 1) == goal:
                    if ord(lines[current[1]][current[0]]) + 1 >= ord('z'):
                        neighbors.append((current[0], current[1] + 1))
                else:
                    neighbors.append((current[0], current[1] + 1))
            if current[1] - 1 > 0 and ord(lines[current[1]][current[0]]) + 1 >= ord(lines[current[1] - 1][current[0]]):
                if (current[0], current[1] - 1) == goal:
                    if ord(lines[current[1]][current[0]]) + 1 >= ord('z'):
                        neighbors.append((current[0], current[1] - 1))
                else:
                    neighbors.append((current[0], current[1] - 1))
            
        if status != 0:
            print(current)
            # print(current)
            # print(neighbors)
            # print(lines[current[1] + 1][current[0]])
            status -= 1
        for point in neighbors:
            g = gscore[current] + abs(point[0] - start[0]) + abs(point[1] - start[1])
            # g = abs(point[0] - start[0]) + abs(point[1] - start[1])
            f = g
            fscore.setdefault(point, math.inf)
            if f < fscore[point]:
                came_from[point] = current
                gscore[point] = g
                fscore[point] = f
                if point not in openset.keys():
                    openset[point] = f

    return []

lines = []
with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)
f.close()
x = len(lines[0])
y = len(lines)
start = (0, 0)
elevation_a = []
end = (0, 0)
for i in range(len(lines[0])):
    for j in range(len(lines)):
        if (lines[j][i] == 'S'):
            start = (i, j)
        if (lines[j][i] == 'E'):
            end = (i, j)
        if (lines[j][i] == 'a'):
            elevation_a.append((i, j))
shortest_paths = []
shortest_paths.append(len(A_Star(start, end, lines)) - 1)
for elevation in elevation_a:
    temp = len(A_Star(elevation, end, lines))
    if temp != 0:
        shortest_paths.append(temp - 1)
print(min(shortest_paths))
