import re

lines = []
with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)
f.close()
t_visited = set()
knots = 10
knots_pos = [(0, 0) for _ in range(knots)]
# print(knots_pos)
# status = 100
for line in lines:
    tokens = re.split("\\s+|\n", line)
    for i in range(int(tokens[1])):
        # Moving the head
        if tokens[0] == 'U':
            knots_pos[0] = (knots_pos[0][0], knots_pos[0][1] + 1)
        elif tokens[0] == 'R':
            knots_pos[0] = (knots_pos[0][0] + 1, knots_pos[0][1])
        elif tokens[0] == 'D':
            knots_pos[0] = (knots_pos[0][0], knots_pos[0][1] - 1)
        else:
            knots_pos[0] = (knots_pos[0][0] - 1, knots_pos[0][1])
        # Moving the tails. Only if the knot in front of one has moved enough should it ever move
        for j in range(1, len(knots_pos)):
            if (abs(knots_pos[j - 1][0] - knots_pos[j][0]) 
                + abs(knots_pos[j - 1][1] - knots_pos[j][1]) > 3): 
                """Ex.
                .....1...      .....21..
                ....2....  ->  .........
                ...3.....      ...3.....
                """
                knots_pos[j] = (knots_pos[j][0] 
                                + int((knots_pos[j-1][0] - knots_pos[j][0]) / 2),
                                knots_pos[j][1]
                                + int((knots_pos[j-1][1] - knots_pos[j][1]) / 2))
            elif (abs(knots_pos[j - 1][0] - knots_pos[j][0]) 
                + abs(knots_pos[j - 1][1] - knots_pos[j][1]) > 2):
                """Ex.
                .........      ........
                ....21...  ->  .....21..
                ...3.....      ...3.....
                """
                if abs(knots_pos[j-1][0] - knots_pos[j][0]) == 2:
                    knots_pos[j] = (knots_pos[j][0] 
                                    + int((knots_pos[j-1][0] - knots_pos[j][0]) / 2), 
                                    knots_pos[j][1]
                                    + (knots_pos[j-1][1] - knots_pos[j][1]))
                if abs(knots_pos[j-1][1] - knots_pos[j][1]) == 2:
                    knots_pos[j] = (knots_pos[j][0] 
                                    + (knots_pos[j-1][0] - knots_pos[j][0]), 
                                    knots_pos[j][1]
                                    + int((knots_pos[j-1][1] - knots_pos[j][1]) / 2))
            elif abs(knots_pos[j-1][0] - knots_pos[j][0]) == 2:
                """Ex.
                .........      .........
                .........  ->  .........
                ...321...      ...3.21..
                """
                knots_pos[j] = (knots_pos[j][0] 
                                + int((knots_pos[j-1][0] - knots_pos[j][0]) / 2),
                                knots_pos[j][1])
            elif abs(knots_pos[j-1][1] - knots_pos[j][1]) == 2:
                knots_pos[j] = (knots_pos[j][0], 
                                knots_pos[j][1]
                                + int((knots_pos[j-1][1] - knots_pos[j][1]) / 2))
        t_visited.add(knots_pos[knots - 1])
        # if (status != 0):
        #     print(knots_pos)
        #     status -= 1
print(len(t_visited))