from collections import defaultdict

original = []
count = defaultdict(int)
with open("input.txt", 'r') as f:
    for line in f:
        count[int(line)] += 1
        original.append([int(line) * 811589153, count[int(line)]])
f.close()
numbers = original.copy()
# Really weird wrapping logic, I tried to do this without removing but it was just too hard for me.
for j in range(10):
    for i in original:
        index = numbers.index(i)
        index += i[0]
        numbers.remove(i)
        numbers.insert(index % len(numbers), [i[0], i[1]])
index_zero = numbers.index([0, 1])
num1000 = numbers[(index_zero + 1000) % len(original)][0]
num2000 = numbers[(index_zero + 2000) % len(original)][0]
num3000 = numbers[(index_zero + 3000) % len(original)][0]
print(num1000 + num2000 + num3000)
