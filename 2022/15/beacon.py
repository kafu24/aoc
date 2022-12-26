"""Note to self, don't use sets."""

import re

lines = []

with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.findall("-?\d+", line)
        integerized = []
        for t in tokens: integerized.append(int(t))
        lines.append(integerized)
f.close()
status = 1
for y in range(4000001):
    intervals = []
    for line in lines:
        distance = abs(line[0] - line[2]) + abs(line[1] - line[3])
        a = abs(line[1] - y)
        # |x1 - z| + |y1 - 2000000| = d. line[0] = x1, line[1] = y1. Solve z
        if distance - a >= 0:
            z_1 = line[0] + a - distance
            z_2 = line[0] - a + distance
            intervals.append([max(0, z_1), min(z_2, 4000000)])
    intervals = sorted(intervals)
    i_max = intervals[0][1]
    for i in range(1, len(intervals) - 1):
        i_max = max(i_max, intervals[i][1])
        if intervals[i + 1][0] > i_max + 1:
            # Gap found
            print((intervals[i][1] + 1) * 4000000 + y)
            status = 0
    if status == 0:
        break
