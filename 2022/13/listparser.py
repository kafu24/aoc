import ast
from functools import cmp_to_key
import operator

def compare(list1: list, list2: list) -> int:
    """Compares list1 and list2. 
    Returns 
     - 1 if they are in the right order. 
     - 0 if they are not.
     - 2 if undecided
    """
    # Check if left or right is empty
    if len(list2) == 0 and len(list1) == 0:
        return 2
    if len(list2) == 0 or len(list1) == 0:
        # If left is empty we're okay, else it's not in the right order
        if len(list1) != 0:
            return 0
        return 1
    for i in range(min(len(list1), len(list2))):
        temp1 = list1[i]
        temp2 = list2[i]
        # Exactly one is an int
        while type(temp1) == list and type(temp2) != list:
            temp2 = [temp2]
        while type(temp2) == list and type(temp1) != list:
            temp1 = [temp1]
        # Both are lists
        if type(temp1) == list and type(temp2) == list:
            temp = compare(temp1, temp2)
            if temp == 0:
                return 0
            elif temp == 1:
                return 1
        # If temp1 and temp2 are just integers
        if type(temp1) == int and type(temp2) == int:
            if temp1 < temp2:
                # This is in the right order
                return 1
            elif temp2 < temp1:
                # Wrong order
                return 0
        # temp1 and temp2 are equal, go compare the next one.
    # We've compared all that there is to compare in the two lists
    if len(list1) > len(list2): # Left side ran out first
        return 0
    if len(list1) == len(list2): # Ambiguous atm
        return 2
    return 1
    
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

lines = []

with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)
f.close()
packets = [[[2]], [[6]]]
sum = 0
pair = 1
for i in range(0, len(lines), 3):
    t_one = ast.literal_eval(lines[i])
    t_two = ast.literal_eval(lines[i + 1])
    # Compare the two values
    temp = compare(t_one, t_two)
    if temp:
        sum += pair
    packets.append(t_one)
    packets.append(t_two)
    pair += 1
my_key = cmp_to_key(make_comparator(compare))
a = sorted(packets, key=my_key)
# print(sum)
first = a.index([[2]]) + 1
second = a.index([[6]]) + 1
print(first * second)
