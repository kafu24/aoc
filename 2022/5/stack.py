import re

sum = 0
stacks = [ [] for _ in range(9) ]

with open("input.txt", 'r') as f:
    for line in f:
        if (line[0] == '['):
            for i in range(9):
                c = line[1 + i * 4]
                if c != ' ':
                    stacks[i].append(c)
        elif (line[0] == '\n'):
            for stack in stacks: stack.reverse()
            # print(stacks)
        elif (line[0] == 'm'):
            tokens = re.findall("\d+", line)
            temp = []
            for i in range(int(tokens[0])):
                temp.append(stacks[int(tokens[1]) - 1].pop())
            for i in range(int(tokens[0])):
                stacks[int(tokens[2]) - 1].append(temp.pop())
f.close()
str = ""

for i in range(9):
    str += stacks[i][-1]
print(stacks)
print(str)
