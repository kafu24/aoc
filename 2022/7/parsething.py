import re
import math

curdir = []
files = set()
dirs = set()
dirs2 = set()
ls = False

with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.split("\\s+|\n", line)
        if line[0] == '$':
            ls = False
            # Command
            if tokens[1] == "cd":
                if tokens[2] != "..":
                    curdir.append(tokens[2] + "/")
                    dirs.add(("".join(curdir), 0))
                else:
                    curdir.pop()
            elif tokens[1] == "ls":
                ls = True
        elif ls == True:
            # Store reg files size
            if tokens[0].isdigit():
                files.add(("".join(curdir) + tokens[1], tokens[0]))
f.close()
for dir in dirs:
    currentsum = 0
    for file in files:
        if dir[0] in file[0]:
            currentsum += int(file[1])
    dirs2.add((dir[0], currentsum))
# sum = 0
min = math.inf
mindir = ""
for dir in dirs2:
    # if dir[1] <= 100000:
    #     sum += dir[1]
    if dir[1] >= 8381165:
        if (dir[1] < min):
            min = dir[1]
            mindir = dir[0]

print(sum)
print(min)
print(mindir)