import re

lines = []

with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.findall(r'\-|\=|[0-2]', line)
        tokens.reverse()
        lines.append(tokens)
f.close()

total_sum = 0

for l in lines:
    temp_sum = 0
    for i in range(len(l)):
        if l[i] == '=':
            temp_sum += -2 * 5 ** i
        elif l[i] == '-':
            temp_sum += -1 * 5 ** i
        elif l[i] == '0':
            temp_sum += 0 * 5 ** i
        elif l[i] == '1':
            temp_sum += 1 * 5 ** i
        elif l[i] == '2':
            temp_sum += 2 * 5 ** i
    total_sum += temp_sum
    
convert = ""
# Go search up "balanced ternary", this is a "balanced quinary"
while total_sum:
    convert = "012=-"[total_sum % 5] + convert
    total_sum = (total_sum + 2) // 5
print(convert)