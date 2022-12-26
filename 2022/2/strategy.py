lines = []

with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)
f.close()
sum = [0] * 9
sum2 = 0

for line in lines:
    if line[0] == 'A':
        if line[2] == 'X': # lose
            sum2 += 3 + 0 # choose scissors
        if line[2] == 'Y': # draw
            sum2 += 1 + 3 # choose rock
        if line[2] == 'Z': # win
            sum2 += 2 + 6 # choose paper
    if line[0] == 'B':
        if line[2] == 'X': # lose
            sum2 += 1 + 0 # choose rock
        if line[2] == 'Y': # draw
            sum2 += 2 + 3 # choose paper
        if line[2] == 'Z': # win
            sum2 += 3 + 6 # choose scissors
    if line[0] == 'C':
        if line[2] == 'X':
            sum2 += 2 + 0
        if line[2] == 'Y':
            sum2 += 3 + 3
        if line[2] == 'Z':
            sum2 += 1 + 6

print(sum2)

# for line in lines:
#     if line[0] == 'A': # Rock
#         if line[2] == 'X':
#             # X is rock, draw
#             sum[0] += 1 + 3
#             # X is paper, win
#             sum[1] += 2 + 6
#             # X is scissors, lose
#             sum[2] += 3 + 0
#         if line[2] == 'Y':
#             # Y is rock, draw
#             sum[3] += 1 + 3
#             # Y is paper, win
#             sum[4] += 2 + 6
#             # Y is scissors, lose
#             sum[5] += 3 + 0
#         if line[2] == 'Z':
#             # Z is rock, draw
#             sum[6] += 1 + 3
#             # Z is paper, win
#             sum[7] += 2 + 6
#             # Z is scissors, lose
#             sum[8] += 3 + 0
#     if line[0] == 'B':
#         if line[2] == 'X':
#             sum[0] += 1 + 0
#             sum[1] += 2 + 3
#             sum[2] += 3 + 6
#         if line[2] == 'Y':
#             sum[3] += 1 + 0
#             sum[4] += 2 + 3
#             sum[5] += 3 + 6
#         if line[2] == 'Z':
#             sum[6] += 1 + 0
#             sum[7] += 2 + 3
#             sum[8] += 3 + 6
#     if line[0] == 'C':
#         if line[2] == 'X':
#             sum[0] += 1 + 6
#             sum[1] += 2 + 0
#             sum[2] += 3 + 3
#         if line[2] == 'Y':
#             sum[3] += 1 + 6
#             sum[4] += 2 + 0
#             sum[5] += 3 + 3
#         if line[2] == 'Z':
#             sum[6] += 1 + 6
#             sum[7] += 2 + 0
#             sum[8] += 3 + 3
print(sum)
