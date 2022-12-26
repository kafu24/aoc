import re
from collections import deque

known = dict()
unknown = deque()
with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.findall(r'[a-z]{4}|-|\+|/|\*|\d+', line)
        if len(tokens) == 2:
            known[tokens[0]] = int(tokens[1])
        else:
            unknown.append(tokens)
f.close()
known.pop('humn')
status = 0
while unknown:
    value = unknown.popleft()
    if value[0] == 'root':
        if status == 10: # Random number to iterate more times to truly flush out knowns
            break
        if status == 0:
            if value[1] in known.keys():
                print(value[1], 'is known: ', known[value[1]])
                known_val = value[1]
                unknown_val = value[3]
                status += 1
            elif value[3] in known.keys():
                print(value[3], 'is known: ', known[value[3]])
                known_val = value[3]
                unknown_val = value[1]
                status += 1
        if status != 0:
            status += 1
    if value[1] in known.keys() and value[3] in known.keys():
        if value[2] == '+':
            known[value[0]] = known[value[1]] + known[value[3]]
        elif value[2] == '-':
            known[value[0]] = known[value[1]] - known[value[3]]
        elif value[2] == '*':
            known[value[0]] = known[value[1]] * known[value[3]]
        elif value[2] == '/':
            known[value[0]] = known[value[1]] / known[value[3]]
    else:
        unknown.append(value)
humn_val = known[known_val]
while unknown:
    value = unknown.popleft()
    if value[0] == unknown_val:
        if value[2] == '+':
            if value[1] in known.keys():
                humn_val -= known[value[1]]
                unknown_val = value[3]
            elif value[3] in known.keys():
                humn_val -= known[value[3]]
                unknown_val = value[1]
        elif value[2] == '-':
            if value[1] in known.keys():
                humn_val -= known[value[1]]
                humn_val *= -1
                unknown_val = value[3]
            elif value[3] in known.keys():
                humn_val += known[value[3]]
                unknown_val = value[1]
        elif value[2] == '/':
            if value[1] in known.keys():
                humn_val = known[value[1]] / humn_val
                unknown_val = value[3]
            elif value[3] in known.keys():
                humn_val *= known[value[3]]
                unknown_val = value[1]
        elif value[2] == '*':
            if value[1] in known.keys():
                humn_val /= known[value[1]]
                unknown_val = value[3]
            elif value[3] in known.keys():
                humn_val /= known[value[3]]
                unknown_val = value[1]
    else:
        unknown.append(value)
    if unknown_val == 'humn':
        print(humn_val)
        break
# print(known['root'])
