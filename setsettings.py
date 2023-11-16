saved_dict = {}
def load_settings():
    global saved_dict
    saved_dict = {}
    with open("savedsettings", "r") as file:
        strings_saved = file.readlines()
        for i in strings_saved:
            i.strip()
            j = (i.strip()).split(":")
            if j[1].isdigit():
                saved_dict[j[0]] = int(j[1])
            else:
                saved_dict[j[0]] = j[1]
    return saved_dict
def set_and_save_settings(**kwargs):
    global saved_dict
    saved_dict = load_settings()
    with open("savedsettings", "w") as file:
        for key, value in kwargs.items():
            saved_dict[key] = value
        file.writelines(str(key)+":"+str(value)+"\n" for key, value in saved_dict.items())
#example: set_and_save_settings(size_canvas_x = 600)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
tk = Tk()
app_running = True
def on_closing():  # выход из приложения
    global app_running
    app_running = False
    tk.destroy()
    import startwindow
    startwindow


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Sea Battle")
#tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width= 500, height=500, bd=0, highlightthickness=0)

'''
size_canvas_x:500
size_canvas_y:500
amount_cell_x:8
amount_cell_y:8
canonic:1
'''
def Set_Size():
    #get x y
    x = labelsizex.get()
    y = labelsizey.get()
    if (str(x).isdigit() and int(x) >= 100 and int(x) <= 1000 and str(y).isdigit() and int(y) >= 100 and int(y) <= 1000):
        global saved_dict
        set_and_save_settings(size_canvas_x = int(x), size_canvas_y = int(y))

labelsizex = ttk.Entry(tk)
labelsizex.pack()
labelsizey = ttk.Entry(tk)
labelsizey.pack()

button_sizexy = Button(tk, text = "set size x, size y", command = Set_Size)
button_sizexy.pack()


def SetCell():
    x = amount_cell.get()
    if (str(x).isdigit() and int(x) >= 5 and int(x) <= 20):
        global saved_dict
        set_and_save_settings(amount_cell = int(x))
amount_cell = ttk.Entry(tk)
amount_cell.pack()
button_cell = Button(tk, text = "field x, y", command = SetCell)
button_cell.pack()


def Set_canonic():
    x = canonic_ref.get()
    if (x=='0' or x=='1'):
        global saved_dict
        set_and_save_settings(canonic = x)
canonic_ref = ttk.Entry(tk)
canonic_ref.pack()
button_canonic = Button(tk, text = "Save type canonic", command = Set_canonic)
button_canonic.pack()


canvas.pack()



tk.update()
while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)