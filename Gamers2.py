from Ships import *

def draw_table(offset_x):
    for i in range(0, amount_cell_x + 1):
        canvas.create_line(offset_x + step_x * i, 0, offset_x + step_x * i, size_canvas_y)
    for i in range(0, amount_cell_y + 1):
        canvas.create_line(offset_x, step_y * i, offset_x + size_canvas_x, step_y * i)
draw_table(0)
draw_table(size_canvas_x + menu_x)

t0 = Label(tk, text="Игрок №1", font=("Helvetica", 16))
t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
t1 = Label(tk, text="Игрок №2", font=("Helvetica", 16))
t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)


def button_show_enemy1():
    for i in range(0, amount_cell_x):
        for j in range(0, amount_cell_y):
            if ships1gamer[j][i] > 0:
                color = "red"
                if points1[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)

def button_show_enemy2():
    for i in range(0, amount_cell_x):
        for j in range(0, amount_cell_y):
            if ships2gamer[j][i] > 0:
                color = "red"
                if points2[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(size_canvas_x + menu_x + i * step_x, j * step_y,
                                              size_canvas_x + menu_x + i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)


def button_begin_again():
    global list_ids
    global points1, points2
    global ships1gamer, ships2gamer
    for el in list_ids:
        canvas.delete(el)
    list_ids = []
    generate_ships_list()
    # print(ships_list)
    ships1gamer = generate_enemy_ships()
    ships2gamer = generate_enemy_ships()
    points1 = [[-1 for i in range(amount_cell_x)] for i in range(amount_cell_y)]
    points2 = [[-1 for i in range(amount_cell_x)] for i in range(amount_cell_y)]


b0 = Button(tk, text="Показать корабли Игрока №1", command=button_show_enemy1)
b0.place(x=size_canvas_x + 20, y=30)

b1 = Button(tk, text="Показать корабли Игрока №2", command=button_show_enemy2)
b1.place(x=size_canvas_x + 20, y=70)

b2 = Button(tk, text="Начать заново!", command=button_begin_again)
b2.place(x=size_canvas_x + 20, y=110)

is1gamershooting = True
t0.configure(bg="red")
t1.configure(bg="white")
def draw_point(x, y):
    global is1gamershooting
    if ships1gamer[y][x] == 0 and not is1gamershooting:
        color = "red"
        id1 = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3, x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)
        is1gamershooting = True
        t0.configure(bg="red")
        t1.configure(bg="white")
    if ships1gamer[y][x] > 0 and not is1gamershooting:
        color = "blue"
        id1 = canvas.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,
                                      y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                      x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
        list_ids.append(id1)
        list_ids.append(id2)
        is1gamershooting = False
        t1.configure(bg="red")
        t0.configure(bg="white")

def draw_point2(x, y, offset_x=size_canvas_x + menu_x):
    global is1gamershooting
    if ships2gamer[y][x] == 0 and is1gamershooting:
        color = "red"
        id1 = canvas.create_oval(offset_x + x * step_x, y * step_y, offset_x + x * step_x + step_x, y * step_y + step_y,
                                 fill=color)
        id2 = canvas.create_oval(offset_x + x * step_x + step_x // 3, y * step_y + step_y // 3,
                                 offset_x + x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)
        is1gamershooting = False
        t1.configure(bg="red")
        t0.configure(bg="white")
    if ships2gamer[y][x] > 0 and is1gamershooting:
        color = "blue"
        id1 = canvas.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,
                                      offset_x + x * step_x + step_x,
                                      y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                      offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y,
                                      fill=color)
        list_ids.append(id1)
        list_ids.append(id2)
        is1gamershooting = True
        t0.configure(bg="red")
        t1.configure(bg="white")

def save_result(string):
    with open("Save", "a") as file_save:
        file_save.write(string)
save_result("Test")
def check_winner1():
    win = True
    for i in range(0, amount_cell_x):
        for j in range(0, amount_cell_y):
            if ships1gamer[j][i] > 0 and points1[j][i] == -1:
                    win = False
    return win

def check_winner2():
    win = True
    for i in range(0, amount_cell_x):
        for j in range(0, amount_cell_y):
            if ships2gamer[j][i] > 0 and points2[j][i] == -1:
                    win = False
    return win

def add_to_all(event): #without event doesn't work. watch canvas bind
    global points1, points2
    # определяем позицию мышки
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    #определяем ячейку
    game_field_x = mouse_x // step_x
    game_field_y = mouse_y // step_y
    # первое игровое поле
    if game_field_x < amount_cell_x and game_field_y < amount_cell_y and not is1gamershooting:
        if points1[game_field_y][game_field_x] == -1:
            points1[game_field_y][game_field_x] = 0
            draw_point(game_field_x, game_field_y)
            if check_winner1():
                save_result("Победа Игрока 2")

    # второе игровое поле
    if game_field_x >= amount_cell_x + delta_menu_x and game_field_x <= amount_cell_x + amount_cell_x + delta_menu_x and game_field_y < amount_cell_y and is1gamershooting:
        if points2[game_field_y][game_field_x - amount_cell_x - delta_menu_x] == -1:
            points2[game_field_y][game_field_x - amount_cell_x - delta_menu_x] = 0
            draw_point2(game_field_x - amount_cell_x - delta_menu_x, game_field_y)
            if check_winner2():
                save_result("Победа Игрока 1")

canvas.bind_all("<Button-1>", add_to_all)

def generate_ships_list():
    global ships_list
    ships_list = []
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3, ship_len4, ship_len5]))

def generate_enemy_ships():
    global ships_list
    enemy_ships = []
    sum_1_all_ships = sum(ships_list)  # подсчет суммарной длины кораблей
    sum_1_enemy = 0
    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0 for i in range(amount_cell_x + 1)] for i in
                       range(amount_cell_y + 1)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

            potential_x = random.randrange(0, amount_cell_x)
            if potential_x + len > amount_cell_x:
                potential_x = potential_x - len

            potential_y = random.randrange(0, amount_cell_y)
            if potential_y + len > amount_cell_y:
                potential_y = potential_y - len
            if horizont_vertikal == 1:
                if potential_x + len <= amount_cell_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = enemy_ships[potential_y][potential_x - 1] + \
                                               enemy_ships[potential_y][potential_x + j] + \
                                               enemy_ships[potential_y][potential_x + j + 1] + \
                                               enemy_ships[potential_y + 1][potential_x + j + 1] + \
                                               enemy_ships[potential_y - 1][potential_x + j + 1] + \
                                               enemy_ships[potential_y + 1][potential_x + j] + \
                                               enemy_ships[potential_y - 1][potential_x + j]
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[potential_y][potential_x + j] = i + 1  # записываем номер корабля
                        except:
                            pass
            if horizont_vertikal == 2:
                if potential_y + len <= amount_cell_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = enemy_ships[potential_y - 1][potential_x] + \
                                               enemy_ships[potential_y + j][potential_x] + \
                                               enemy_ships[potential_y + j + 1][potential_x] + \
                                               enemy_ships[potential_y + j + 1][potential_x + 1] + \
                                               enemy_ships[potential_y + j + 1][potential_x - 1] + \
                                               enemy_ships[potential_y + j][potential_x + 1] + \
                                               enemy_ships[potential_y + j][potential_x - 1]
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[potential_y + j][potential_x] = i + 1  # записываем номер корабля
                        except:
                            pass

        sum_1_enemy = 0
        for i in range(0, amount_cell_x):
            for j in range(0, amount_cell_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy += 1
    return enemy_ships

generate_ships_list()
ships1gamer = generate_enemy_ships()
ships2gamer = generate_enemy_ships()

while app_running:
    gamer1_alive = 0
    for i in range(len(points1)):
        for j in range(len(points1[i])):
            if ships1gamer[i][j] > 0 and points1[i][j] == -1:
                gamer1_alive+=1
    t0.config(text = "Gamer1: " + str(gamer1_alive))
    gamer2_alive = 0
    for i in range(len(points1)):
        for j in range(len(points1[i])):
            if ships2gamer[i][j] > 0 and points2[i][j] == -1:
                gamer2_alive += 1
    t1.config(text="Gamer2: " + str(gamer2_alive))
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
    from My_canvas import app_running