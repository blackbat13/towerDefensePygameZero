import pgzrun

"""CONFIGURATION"""

WIDTH = 800
HEIGHT = 640

"""VARIABLES"""

map_list = []
towers_list = []

"""DRAW"""


def draw():
    screen.fill("white")
    draw_map()
    draw_list(towers_list)


def draw_map():
    for row in map_list:
        for tile in row:
            tile.draw()


def draw_list(list):
    for el in list:
        el.draw()


"""UPDATE"""


def update():
    pass


"""EVENTS"""


def on_mouse_down(pos):
    x, y = pos
    row, col = coord_to_map(x, y)
    if row >= len(map_list) or col >= len(map_list[row]):
        return

    if map_list[row][col].type == 1:
        add_tower(row, col, 1)
    elif map_list[row][col].type > 10:
        upgrade_tower(row, col, map_list[row][col].type % 10)


"""HELPERS"""


def add_tower(row, col, type):
    map_list[row][col].type = 10 + type
    tower = Actor(f"tower{type}")
    tower.pos = map_to_coord(row, col)
    tower.type = type
    towers_list.append(tower)


def upgrade_tower(row, col, type):
    remove_tower(row, col)
    map_list[row][col].type = 20 + type
    tower = Actor(f"tower{type}u")
    tower.pos = map_to_coord(row, col)
    tower.type = type
    towers_list.append(tower)


def remove_tower(row, col):
    for tower in towers_list:
        trow, tcol = coord_to_map(tower.x, tower.y)
        if row == trow and col == tcol:
            towers_list.remove(tower)
            return


def coord_to_map(x, y):
    row = y // 64
    col = x // 64
    return row, col


def map_to_coord(row, col):
    x = col * 64 + 32
    y = row * 64 + 32
    return x, y


"""INITIALIZATION"""


def init():
    init_map()


def init_map():
    global map_list

    file = open("map.txt")
    lines_list = file.read().split("\n")
    file.close()

    y = 32

    for line in lines_list:
        map_list.append([])
        x = 32
        for digit in line:
            tile = Actor("tile" + digit)
            tile.x = x
            tile.y = y
            tile.type = int(digit)
            map_list[-1].append(tile)
            x += 64
        y += 64


init()
pgzrun.go()
