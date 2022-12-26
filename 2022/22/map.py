from collections import defaultdict
import re

lines = []
# west, north = defaultdict(lambda: 999), defaultdict(lambda: 999)
# east, south = defaultdict(int), defaultdict(int)
west, north, east, south = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)

with open("input.txt", 'r') as f:
    r = 0
    status = 0
    for line in f:
        l = line.strip('\n')
        if len(l) == 0:
            status = 1
        # if status != 1:
            # Part 1
            # for index in range(len(l)):
            #     if l[index] != ' ':
            #         if west[r] > index:
            #             west[r] = index
            #         if north[index] > r:
            #             north[index] = r
            #         if east[r] < index:
            #             east[r] = index
            #         if south[index] < r:
            #             south[index] = r
        r += 1
        lines.append(re.findall(r'\d+|\sp|.|#|[A-Z]', l))
f.close()
# Part 2. Only works for my input. Come back in future (TM) to make something cool.
# Each box is 50x50, refer to the amazing diagram I drew for reference
for i in range(0, 50):
    north[i] = [50, i + 50, 0] # Box 5 top -> Box 3 left
    north[i + 50] = [0, i + 150, 0] # Box 1 top -> Box 6 left
    north[i + 100] = [i, 199, 3] # Box 2 top -> Box 6 bottom
    south[i] = [i + 100, 0, 1] # Box 6 bot -> Box 2 top 
    south[i + 50] = [49, i + 150, 2] # Box 4 bot -> Box 6 right
    south[i + 100] = [99, i + 50, 2] # Box 2 bot -> Box 3 right
    west[i] = [0, 149 - i, 0] # Box 1 left -> Box 5 left
    west[i + 50] = [i, 100, 1] # Box 3 left -> Box 5 top
    west[i + 100] = [50, 49 - i, 0] # Box 5 left -> Box 1 left
    west[i + 150] = [i + 50, 0, 1] # Box 6 left -> Box 1 top
    east[i] = [99, 149 - i, 2] # Box 2 right -> Box 4 right
    east[i + 50] = [i + 100, 49, 3] # Box 3 right -> Box 2 bot
    east[i + 100] = [149, 49 - i, 2] # Box 4 right -> Box 2 right
    east[i + 150] = [i + 50, 149, 3] # Box 6 right -> Box 4 bot
col = lines[0].index('.')
row = 0
facing = 0
directions = lines[len(lines) - 1]
for dir in directions:
    # print(col, row, facing)
    if dir == 'L':
        facing = facing - 1 if facing != 0 else 3
    elif dir == 'R':
        facing = facing + 1 if facing != 3 else 0
    elif dir.isdigit():
        count = 0
        while (count != int(dir)):
            if facing == 0:
                # lines[row][col] = '>'
                try:
                    if lines[row][col + 1] != '#':
                        # No wall
                        col += 1
                    else:
                        break
                except IndexError:
                    # See if loop around on the left is okay
                    # Part 1
                    # if lines[row][west[row]] != '#':
                    #     col = west[row]
                    # Part 2
                    if lines[east[row][1]][east[row][0]] != '#':
                        col = east[row][0]
                        facing = east[row][2]
                        row = east[row][1]
                    else:
                        break
                count += 1
            elif facing == 1:
                # lines[row][col] = 'V'
                try:
                    if lines[row + 1][col] == ' ':
                        # if lines[north[col]][col] != '#':
                        #     row = north[col]
                        if lines[south[col][1]][south[col][0]] != '#':
                            row = south[col][1]
                            facing = south[col][2]
                            col = south[col][0]
                        else:
                            break
                    elif lines[row + 1][col] != '#':
                        # No wall
                        row += 1
                    else:
                        break
                except IndexError:
                    # See if loop around on the top is okay
                    # if lines[north[col]][col] != '#':
                    #     row = north[col]
                    if lines[south[col][1]][south[col][0]] != '#':
                        row = south[col][1]
                        facing = south[col][2]
                        col = south[col][0]
                    else:
                        break
                count += 1
            elif facing == 2:
                # lines[row][col] = '<'
                if col > 0:
                    if lines[row][col - 1] == ' ':
                        # if lines[row][east[row]] != '#':
                        #     col = east[row]
                        if lines[west[row][1]][west[row][0]] != '#':
                            col = west[row][0]
                            facing = west[row][2]
                            row = west[row][1]
                        else:
                            break
                    elif lines[row][col - 1] != '#':
                        # No wall
                        col -= 1
                    else:
                        break
                elif col == 0:
                    # See if loop around on the right is okay
                    # if lines[row][east[row]] != '#':
                    #     col = east[row]
                    if lines[west[row][1]][west[row][0]] != '#':
                        col = west[row][0]
                        facing = west[row][2]
                        row = west[row][1]
                    else:
                        break
                count += 1
            elif facing == 3:
                # lines[row][col] = '^'
                if row > 0:
                    if lines[row - 1][col] == ' ':
                        # if lines[south[col]][col] != '#':
                        #     row = south[col]
                        if lines[north[col][1]][north[col][0]] != '#':
                            row = north[col][1]
                            facing = north[col][2]
                            col = north[col][0]
                        else:
                            break
                    elif lines[row - 1][col] != '#':
                        # No wall
                        row -= 1
                    else:
                        break
                elif row == 0:
                    # See if loop around on the bottom is okay
                    # if lines[south[col]][col] != '#':
                    #     row = south[col]
                    if lines[north[col][1]][north[col][0]] != '#':
                            row = north[col][1]
                            facing = north[col][2]
                            col = north[col][0]
                    else:
                        break
                count += 1
with open("output.txt", 'w') as f:
    for line in lines:
        f.write("".join(line))
        f.write("\n")
f.close()
print(1000 * (row + 1) + 4 * (col + 1) + facing)
