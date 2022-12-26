"""I honestly can't understand what this story is trying to say, 
so I'll just go based off the diagrams.
"""
import re
    
def i_hate_functional(graph):
    """Takes a vertical scan thing and simulates dropping
    sand at coordinates (500, 0) until an endless void
    or no more sand can be spawned at (500, 0). Prints the
    count of the amount of sand at rest.

    Args:
        graph - Vertical scan thing

    Returns:
        graph with units of sand at rest
    """
    status = 0
    count = 0
    diverge_y = 0
    cur_x = 500
    while (1):
        if status:
            cur_x = 500
            diverge_y = 0
            status = 0
        if graph[diverge_y][cur_x] == ".":
            diverge_y += 1
            if diverge_y >= 1000:
                print(count)
                return graph
        elif graph[diverge_y][cur_x - 1] == ".":
            diverge_y += 1
            cur_x -= 1
            if diverge_y >= 1000 or cur_x - 1 < 0:
                print(count)
                return graph
        elif graph[diverge_y][cur_x + 1] == ".":
            diverge_y += 1
            cur_x += 1
            if diverge_y >= 1000 or cur_x + 1 >= 1000:
                print(count)
                return graph
        elif graph[0][500] == "o":
            print(count)
            return graph
        else:
            count += 1
            graph[diverge_y - 1][cur_x] = "o"
            status = 1

max_y = 0
# Use a 1000x1000 grid, seems to be big enough.
graph = [ [ "." for _ in range(1000) ] for _ in range(1000) ]
with open("input.txt", 'r') as f:
    for line in f:
        tokens = re.findall("\d+", line)
        for i in range(0, len(tokens) - 2, 2):
            for j in range(min(int(tokens[i]), int(tokens[i+2])), max(int(tokens[i]), int(tokens[i+2])) + 1):
                graph[int(tokens[i+1])][j] = "#"
            for j in range(min(int(tokens[i+1]), int(tokens[i+3])), max(int(tokens[i+1]), int(tokens[i+3])) + 1):
                graph[j][int(tokens[i])] = "#"
            a = max(int(tokens[i+1]), int(tokens[i+3]))
            max_y = a if a > max_y else max_y
f.close()
for i in range(0, len(graph[0])):
    graph[max_y + 2][i] = "#"
graph = i_hate_functional(graph)
