import re

countdown = 20
ccount = 0
position = 0
rx = 1
sum = 0

with open("input.txt", 'r') as f:
    for line in f:
        position = ccount % 40
        ccount += 1
        countdown -= 1
        if countdown == 0:
            countdown = 40
            sum += ccount * rx
        if position <= rx + 1 and position >= rx - 1:
            print("#", end="")
        else:
            print(".", end="")
        if position == 39:
            print("")
        tokens = re.split("\\s+|\n", line)
        if tokens[0] == "addx":
            position = ccount % 40
            ccount += 1
            countdown -= 1
            if (countdown == 0):
                countdown = 40
                sum += ccount * rx
            if position <= rx + 1 and position >= rx - 1:
                print("#", end="")
            else:
                print(".", end="")
            if position == 39:
                print("")
            rx += int(tokens[1])
print(sum)
        