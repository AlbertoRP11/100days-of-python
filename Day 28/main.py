from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN  * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_time)
        timer_label.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    time_minute = math.floor(time / 60)
    time_seconds = time % 60
    if time_seconds < 10:
        time_seconds = f"0{time_seconds}"
    canvas.itemconfig(timer_text, text=f"{time_minute}:{time_seconds}")
    if time > 0:
        global timer
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=15, highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", font=15, highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=FONT_NAME)
checkmarks.grid(row=4, column=1)

window.mainloop()
