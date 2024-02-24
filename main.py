from tkinter import *
import math
import winsound
from tkinter.simpledialog import askinteger


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 52
SHORT_BREAK_MIN = 17
reps = 0
timer = None
FREQUENCY = 1250  # Set Frequency To 2500 Hertz
DURATION = 1000

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick.config(text="")
    global reps
    global turns
    reps = 0
    turns = askinteger('Input', 'How many hours do you want', parent=window)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60

    if reps % 2 == 1:
        label.config(text="Work",fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        label.config(text="Break",fg=PINK)
        count_down(short_break_sec)
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        global turns
        winsound.Beep(FREQUENCY, DURATION)
        marks = ""
        for _ in range(math.floor((reps+1)/2)):
            marks += "✓"
        tick.config(text=marks)

        if turns*2-1 == reps:
            label.config(text="Finished",fg=RED)
            return
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

#Upper text
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label.grid(row=0, column=1)

#Start button
start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

#Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

#Ticks
tick = Label(fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
tick.grid(row=3, column=1)

turns = askinteger('Input', 'How many hours do you want', parent=window)

window.mainloop()