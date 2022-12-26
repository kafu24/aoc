from math import floor
import re

lines = []

with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)
f.close()

items = [ [] for _ in range(8) ]
# Set up starting items
for i in range(8):
    tokens = re.findall("\d+", lines[1 + (i * 7)])
    temp = []
    for item in tokens: temp.append(int(item))
    items[i] = temp
round = 1
count = [0, 0, 0, 0, 0, 0, 0, 0]
items2 = [ [] for _ in range(8)]
for r in range(10000):
    # print(round)
    # Go through a round
    for i in range(8):
        # Get what will the monkey do when it inspects an item
        tokens = re.split("\\s+|\n", lines[2 + (i * 7)])
        # The test
        tokens2 = re.findall("\d+", lines[3 + (i * 7)])
        iftrue = re.findall("\d+", lines[4 + (i * 7)])
        iffalse = re.findall("\d+", lines[5 + (i * 7)])
        count[i] += len(items[i])
        for j in range(len(items[i])):
            # Monkey inspects items in its inventory
            item = items[i].pop(0)
            if tokens[6] != "old":
                if tokens[5] == "+":
                    item += int(tokens[6])
                else:
                    item *= int(tokens[6])
            else:
                if tokens[5] == "+":
                    item += item
                else:
                    item *= item
            # item = floor(item / 3)
            # x % n = (x % M) % n where n | M, thanks reddit
            if item % int(tokens2[0]) == 0:
                items[int(iftrue[0])].append(item % 9699690)
            else:
                items[int(iffalse[0])].append(item % 9699690)
    round += 1
print(count)
a = max(count)
count.remove(max(count))
b = max(count)
count.remove(max(count))
print(a * b)