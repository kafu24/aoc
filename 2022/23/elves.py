import re, numpy
from collections import defaultdict, deque

def consider_mvmt(elf: list, grid):
    x, y = elf[1], elf[0]
    if (grid[y+1][x-1] != '#' and grid[y+1][x] != '#'
        and grid[y+1][x+1] != '#' and grid[y][x+1] != '#'
        and grid[y-1][x+1] != '#' and grid[y-1][x] != '#'
        and grid[y-1][x-1] != '#' and grid[y][x-1] != '#'):
        return True
    return False

def propose_mvmt(elf: list, dirs: list, grid):
    x, y = elf[1], elf[0]
    for dir in dirs:
        if dir == 'n':
            if (grid[y-1][x] != '#' and grid[y-1][x+1] != '#'
                and grid[y-1][x-1] != '#'):
                return (y-1, x)
        elif dir == 's':
            if (grid[y+1][x] != '#' and grid[y+1][x+1] != '#'
                and grid[y+1][x-1] != '#'):
                return (y+1, x)
        elif dir == 'e':
            if (grid[y][x+1] != '#' and grid[y+1][x+1] != '#'
                and grid[y-1][x+1] != '#'):
                return (y, x+1)
        elif dir == 'w':
            if (grid[y][x-1] != '#' and grid[y+1][x-1] != '#'
                and grid[y-1][x-1] != '#'):
                return (y, x-1)
    return None

grid = numpy.full((5000, 5000), '.', dtype=object)

proposed = defaultdict(list)
elves = []
with open("input.txt", 'r') as f:
    x_start = 2500
    y_start = 2500
    for line in f:
        tokens = re.findall(r'\.|#', line)
        for i in range(len(tokens)):
            grid[y_start][x_start + i] = tokens[i]
            if tokens[i] == '#':
                
                elves.append([y_start, x_start + i])
        y_start += 1
f.close()
count = 0
keep_going = 1
dirs = deque('nswe')
while (keep_going):
    keep_going = 0
    proposed.clear()
    # if count == 10:
    #     break
    # First half
    # Consider the 8 positions for each elf
    for elf in elves:
        if not consider_mvmt(elf, grid):
            keep_going = 1
            if propose_mvmt(elf, dirs, grid):
                proposed[propose_mvmt(elf, dirs, grid)].append(elf)
    # Second half
    for mvt in proposed:
        if len(proposed[mvt]) == 1:
            elf = proposed[mvt][0]
            grid[elf[0]][elf[1]] = '.'
            grid[mvt[0]][mvt[1]] = '#'
            elves.remove(elf)
            elves.append([mvt[0], mvt[1]])
    dirs.append(dirs.popleft())
    count += 1
xmin, xmax = 5000, 0
ymin, ymax = 5000, 0
for elf in elves:
    if elf[0] < ymin:
        ymin = elf[0]
    if elf[0] > ymax:
        ymax = elf[0]
    if elf[1] < xmin:
        xmin = elf[1]
    if elf[1] > xmax:
        xmax = elf[1]
print(count)
emptycount = 0
with open("output.txt", 'w') as f:
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if grid[y][x] == '.':
                emptycount += 1
        f.write("".join(grid[y][xmin:xmax]))
        f.write('\n')
print(emptycount)
