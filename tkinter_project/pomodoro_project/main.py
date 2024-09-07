from tkinter import *
import math
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep %8 == 0 : 
        count_down(long_break_sec)
        title.config(text="Break", fg = RED)
    elif rep % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg = PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = '0' + str(count_sec)
    

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    elif rep >8:
        reset()
    else:
        start_timer()
        mark = ""
        work_session = math.floor(rep/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)
Checkmark="✔"


#Timer Title
title = Label(text="Timer",font=(FONT_NAME, 40, "bold"),fg=GREEN, highlightthickness=0,bg=YELLOW)
title.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tkinter_project/pomodoro_project/tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


#start button
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

#reset button
reset_button = Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

#checkmark
check_mark = Label(text=Checkmark,bg=YELLOW, highlightthickness=0, fg=GREEN)
check_mark.grid(column=1,row=3)
window.mainloop()