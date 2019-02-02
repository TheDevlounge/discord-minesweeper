import random
import itertools

def generate(mx=9, my=9, mines=10):
    grid = [[0 for x in range(mx)] for y in range(my)]

    # generate mines

    coords_used = set()

    while len(coords_used) < mines:
        x, y = random.randint(0, mx - 1), random.randint(0, my - 1)

        if (x,y) not in coords_used:
            coords_used.add((x, y))

            grid[y][x] = 'x'

    for x,y in itertools.product(range(0,mx), range(0,my)):
        c = grid[y][x]

        if c == 'x':
            continue

        # mark numbers of neighbor mines
        nmines = 0
        for nx,ny in neighbors( x,y, mx, my):
            if grid[ny][nx] == 'x':
                nmines += 1
        grid[y][x] = nmines

    return grid


def neighbors(cx,cy, mx, my):
    for x,y in itertools.product(range(cx-1,cx+2), range(cy-1, cy+2)):
        if x < 0 or y < 0 or x >= mx or y >= my:
            continue
        yield x,y

def to_dc_spoilers(grid):
    mx = len(grid)
    my = len(grid[0])

    str0 = ""

    for y in range(0, my):

        for x in range(0, mx):
            c = grid[y][x]
            char = "?"

            if c == 'x': char = ':bomb:'
            elif c == 0: char = ':zero:'
            elif c == 1: char = ':one:'
            elif c == 2: char = ':two:'
            elif c == 3: char = ':three:'
            elif c == 4: char = ':four:'
            elif c == 5: char = ':five:'
            elif c == 6: char = ':six:'
            elif c == 7: char = ':seven:'
            elif c == 8: char = ':eight:'
            elif c == 9: char = ':nine:'

            str0 += "||{}|| ".format(char)

        str0 += "\n"

    return str0


if __name__ == "__main__":


    grid = generate()

    print(to_dc_spoilers(grid))
