with open("input.txt", 'r') as f:
    line = f.readline()
    for i in range(len(line) - 14):
        temp = set()
        for j in range(14):
            temp.add(line[i + j])
        if (len(temp) == 14):
            print(temp)
            print(i + 14)
            break
f.close()
