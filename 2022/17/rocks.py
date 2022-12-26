window_x = 7
window_y = 30000
window = [ [ 0 for _ in range(window_x)] for _ in range(window_y) ]
bag = [
    [[1, 1, 1, 1]],
    
    [[0, 2, 0],
     [2, 2, 2],
     [0, 2, 0]],
    
    [[0, 0, 3],
     [0, 0, 3],
     [3, 3, 3]],
    
    [[4],
     [4],
     [4],
     [4]],
    
    [[5, 5],
     [5, 5]]
]

def check_collision_horiz(window: list, rock: list, offset: int, pos: tuple):
    """Returns true if there is a collision."""
    off_x = offset
    for cy, row in enumerate(rock):
        for cx, cell in enumerate(row):
            if cx + off_x + pos[0] < 0:
                return True
            try:
                if cell and window[cy + pos[1]][cx + off_x + pos[0]]:
                    return True
            except IndexError:
                return True
    return False

def check_collision_vert(window: list, rock: list, offset: int, pos: tuple):
    """Returns true if there is a collision."""
    off_y = offset
    for cy, row in enumerate(rock):
        for cx, cell in enumerate(row):
            try:
                if cell and window[cy + off_y + pos[1]][cx + pos[0]]:
                    return True
            except IndexError:
                return True
    return False

dirs = ""
with open("input.txt", 'r') as f:
    for l in f:
        dirs = l
f.close()
cycle = 0
cur_h = 0
spawn_x = 2
spawn_y = window_y - 1 - 3 # The line we want the bottom to be hitting when it spawns
cur_x = 0
cur_y = 0
rock = []
zeroes = [0, 0, 0, 0, 0, 0, 0]
in_play = False
rocks_dropped = 0
other_count = 0
status = 1
i = 0
depth = 0

while (True):
    if not in_play:
        cur_x = spawn_x
        cur_y = spawn_y - len(bag[cycle]) + 1
        rock = bag[cycle]
        cycle = 0 if cycle + 1 >= 5 else cycle + 1
        other_count += 1
        in_play = True
    curdir = dirs[i]
    if curdir == '>':
        if not check_collision_horiz(window, rock, 1, (cur_x, cur_y)):
            cur_x += 1
    elif curdir == '<':
        if not check_collision_horiz(window, rock, -1, (cur_x, cur_y)):
            cur_x -= 1
    if check_collision_vert(window, rock, 1, (cur_x, cur_y)):
        # Rock has to be placed.
        for cy, row in enumerate(rock):
            for cx, val in enumerate(row):
                window[cy + cur_y][cx + cur_x] += val
        rocks_dropped += 1
        # Honestly still can't wrap my head around this even after reading an explanation
        if cur_y - spawn_y >= depth:
            depth = cur_y - spawn_y
            # print(depth, rocks_dropped, cur_h)
        in_play = False
    else:
        cur_y += 1
    # Update current height of highest block
    for j in range(window_y - cur_h - 1, -1, -1):
        if window[j] == zeroes:
            cur_h = window_y - j - 1
            break
    spawn_y = window_y - cur_h - 1 - 3 
    i += 1
    if i == len(dirs) - 1:
        i = 0
    if rocks_dropped == 6409 + 466:
        print("For 466: ", cur_h - 9792)
    if rocks_dropped == 10000:
        break
dumb_elephants_want_this = 1000000000000
# First 40 depth drop is at 1264 rock drops. 583090378 cycles of 1715 rock drops.
# 466 more rock drops to reach 1 trillion
# Each interval of 1715 rock drop gives a height of 2613
# 466 into a cycle of 1715 gives a height of 695
# 1953 + [intervals] * 2613 + 695 = 1523615160362
x = ((dumb_elephants_want_this - 1264) // 1715)
diff = (dumb_elephants_want_this - 1715 * x) - 1264
# print(diff)
print(1953 + x * 2613 + 695)

