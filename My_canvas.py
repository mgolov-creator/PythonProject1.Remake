from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()
app_running = True
from Load_settings import load_settings
size_canvas_x = load_settings()['size_canvas_x']
size_canvas_y = load_settings()['size_canvas_y']
amount_cell_x = load_settings()['amount_cell']  # размер игрового поля
amount_cell_y = load_settings()['amount_cell'] # поле в игре будет квадратным
step_x = size_canvas_x // amount_cell_x  # размер ячейки по горизонтали
step_y = size_canvas_y // amount_cell_y  # размер ячейки по вертикали
size_canvas_x = step_x * amount_cell_x # новая длина
size_canvas_y = step_y * amount_cell_y
delta_menu_x = 4
menu_x = step_x * delta_menu_x  # 250
menu_y = 40
def on_closing():  # выход из приложения
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Sea Battle")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x + size_canvas_x, height=size_canvas_y + menu_y, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="lightyellow")
canvas.create_rectangle(size_canvas_x + menu_x, 0, size_canvas_x + menu_x + size_canvas_x, size_canvas_y,
                        fill="lightgreen")
canvas.pack()
tk.update()