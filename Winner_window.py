import time
from tkinter import *
def ininitializate(text):
    t0.config(text = text)
def close():  # выход из приложения
    global app_running_winner_window
    app_running_winner_window = False
    #time.sleep(1)
    tk.destroy()
    import startwindow
    startwindow
app_running_winner_window = True
tk = Tk()
tk.protocol("WM_DELETE_WINDOW", close)
tk.title("Sea Battle")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width= 300, height=300, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 300, 300, fill="white")
t0 = Label(tk, font=("Helvetica", 30))
t0.pack()
canvas.pack()
tk.update()
#ininitializate("HAHA")
def Show_result():

    while app_running_winner_window:
        if app_running_winner_window:
            try:
                tk.update_idletasks()
                tk.update()
            except:
                pass
        else:
            break
        time.sleep(0.01)