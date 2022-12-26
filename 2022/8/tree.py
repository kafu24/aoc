sum = 0
lines = []

with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line.strip("\n"))
f.close()
# All trees on the border are visible
sum += len(lines[0]) * 2 + len(lines) * 2 - 4
# Count interior trees visible from outside
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        visibleN = True
        visibleE = True
        visibleS = True
        visibleW = True
        tree = lines[i][j]
        # Is there any tree to be left as tall as me?
        for k in range(j):
            if tree <= lines[i][k]:
                visibleW = False
        # How about to my right?
        for k in range(j + 1, len(lines[0])):
            if tree <= lines[i][k]:
                visibleE = False
        # To my top?
        for k in range(i):
            if tree <= lines[k][j]:
                visibleN = False
        # And below me
        for k in range(i + 1, len(lines)):
            if tree <= lines[k][j]:
                visibleS = False
        if visibleN or visibleE or visibleS or visibleW:
            sum += 1
print("Sum:", sum)
score = 0
# Scenic score, no point in counting the edges as they'll just be zero
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        distN = 0
        distE = 0
        distS = 0
        distW = 0
        tree = lines[i][j]
        # Left
        for k in range(j - 1, -1, -1):
            distW += 1
            if tree <= lines[i][k]:
                break
        # Right
        for k in range(j + 1, len(lines[0])):
            distE += 1
            if tree <= lines[i][k]:
                break
        # Up
        for k in range(i - 1, -1, -1):
            distN += 1
            if tree <= lines[k][j]:
                break
        # Down
        for k in range(i + 1, len(lines)):
            distS += 1
            if tree <= lines[k][j]:
                break
        score = distN * distE * distS * distW if distN * distE * distS * distW > score else score
print("Score:", score)
