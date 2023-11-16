from tkinter import *
from tkinter import messagebox
import time
tk = Tk()
app_running = True

size_canvas_x = 300
size_canvas_y = 500

def on_closing():  # выход из приложения
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Sea Battle")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=+ size_canvas_x, height=size_canvas_y, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")

def open_settings():
    global button_settings
    global button_2_players
    global app_running
    app_running = False
    tk.destroy()
    import setsettings
    setsettings
def play_2_gamers():
    global app_running
    app_running = False
    tk.destroy()
    import Gamers2
    Gamers2



button_settings = Button(tk, text="Settings", command=open_settings)
button_settings.place(x= 120, y=50)

button_2_players = Button(tk, text="Play 2 gamers", command=play_2_gamers)
button_2_players.place(x= 120, y=100)

def play_single():
    global app_running
    app_running = False
    tk.destroy()
    import GameSingle
    GameSingle
button_singleplayer = Button(tk, text="Play single game", command=play_single)
button_singleplayer.place(x= 120, y=150)

canvas.pack()
tk.update()

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)