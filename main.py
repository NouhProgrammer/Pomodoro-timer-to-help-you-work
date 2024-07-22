from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
ORANGE = "#ffb200"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"
reps = 1
timer_window = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global timer_window, reps
    window.after_cancel(timer_window)
    canvas.itemconfig(timer, text="0:00")
    title.config(text="Timer", fg=GREEN)
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title.config(text="Work Time", fg=GREEN)
    elif reps % 8 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Break", fg=RED)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global timer_window
    minutes = seconds // 60
    seconds_in_time = seconds % 60
    if seconds_in_time < 10:
        seconds_in_time = f"0{seconds_in_time}"
    time_remaining = f"{minutes}:{seconds_in_time}"
    canvas.itemconfig(timer, text=time_remaining)
    if seconds > 0:
        timer_window = window.after(1000, count_down, seconds - 1)
    else:
        window.after(1000, start_timer)
        marks = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            marks += check_mark
        check_mark_onscreen.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Timer")
window.config(padx=100, pady=50, bg=ORANGE)

title = Label(text="Timer", bg=ORANGE, fg=GREEN, font=(FONT_NAME, 50))
canvas = Canvas(width=200, height=224, bg=ORANGE, highlightthickness=0)
left_button = Button(text="Start", command=start_timer)
right_button = Button(text="Reset", command=reset)
check_mark_onscreen = Label(bg=ORANGE, fg=GREEN)

photo = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=photo)
timer = canvas.create_text(103, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=2, column=2)
title.grid(row=1, column=2)
left_button.grid(row=3, column=1)
right_button.grid(row=3, column=3)
check_mark_onscreen.grid(row=4, column=2)



window.mainloop()