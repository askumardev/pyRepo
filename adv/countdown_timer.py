# python3 adv/countdown_timer.py


import tkinter as tk
from tkinter import ttk

running = False
remaining_time = 0  # in milliseconds


def start_timer():
    global running, remaining_time

    try:
        minutes = int(min_entry.get())
        seconds = int(sec_entry.get())
        millis = int(ms_entry.get())
    except ValueError:
        return

    remaining_time = (minutes * 60 * 1000) + (seconds * 1000) + millis
    running = True
    countdown()


def stop_timer():
    global running
    running = False


def countdown():
    global remaining_time

    if running and remaining_time >= 0:

        mins = remaining_time // 60000
        secs = (remaining_time % 60000) // 1000
        millis = remaining_time % 1000

        time_label.config(
            text=f"{mins:02d}:{secs:02d}:{millis:03d}"
        )

        remaining_time -= 10
        root.after(10, countdown)
    else:
        time_label.config(text="00:00:000")


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x200")

# Display
time_label = tk.Label(root, text="00:00:000", font=("Arial", 30))
time_label.pack(pady=10)

# Input fields
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Minutes").grid(row=0, column=0)
tk.Label(frame, text="Seconds").grid(row=0, column=1)
tk.Label(frame, text="Millis").grid(row=0, column=2)

min_entry = tk.Entry(frame, width=5)
sec_entry = tk.Entry(frame, width=5)
ms_entry = tk.Entry(frame, width=7)

min_entry.grid(row=1, column=0)
sec_entry.grid(row=1, column=1)
ms_entry.grid(row=1, column=2)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start", command=start_timer, width=10)
stop_btn = tk.Button(btn_frame, text="Stop", command=stop_timer, width=10)

start_btn.grid(row=0, column=0, padx=10)
stop_btn.grid(row=0, column=1, padx=10)

root.mainloop()