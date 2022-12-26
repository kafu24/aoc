import re

sum = 0

with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.split(",|-|\n", line)
        # if int(tokens[0]) <= int(tokens[2]) and int(tokens[1]) >= int(tokens[3]):
        #     # Second pair is fully contained in the first pair
        #     sum += 1
        # elif int(tokens[2]) <= int(tokens[0]) and int(tokens[3]) >= int(tokens[1]):
        #     # First pair is fully contained in the second pair
        #     sum += 1
        if int(tokens[0]) >= int(tokens[2]) and int(tokens[0]) <= int(tokens[3]):
            sum += 1
        elif int(tokens[1]) >= int(tokens[2]) and int(tokens[1]) <= int(tokens[3]):
            sum += 1
        elif int(tokens[2]) >= int(tokens[0]) and int(tokens[2]) <= int(tokens[1]):
            sum += 1
        elif int(tokens[3]) >= int(tokens[0]) and int(tokens[3]) <= int(tokens[1]):
            sum += 1
f.close()
print(sum)
