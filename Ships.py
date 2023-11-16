from My_canvas import *
from Load_settings import load_settings
if not(load_settings()['canonic']):
    ships = amount_cell_x // 2  # определяем максимальное кол-во кораблей
    ship_len1 = amount_cell_x // 5  # длина первого типа корабля
    ship_len2 = amount_cell_x // 4  # ...
    ship_len3 = amount_cell_x // 3
    ship_len4 = amount_cell_x // 2
    ship_len5 = amount_cell_x // 3
else:
    ships = 5
    ship_len1 = 5
    ship_len2 = 4
    ship_len3 = 3
    ship_len4 = 2
    ship_len5 = 1
ships1gamer = [[0 for i in range(amount_cell_x + 1)] for i in range(amount_cell_y + 1)]
ships2gamer = [[0 for i in range(amount_cell_x + 1)] for i in range(amount_cell_y + 1)]
list_ids = []  # список объектов canvas.py

# points1 - список куда мы кликнули мышкой
points1 = [[-1 for i in range(amount_cell_x)] for i in range(amount_cell_y)]
points2 = [[-1 for i in range(amount_cell_x)] for i in range(amount_cell_y)]

# ships_list - список кораблей игрока 1 и игрока 2
ships_list = []