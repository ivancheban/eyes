import tkinter as tk
from tkinter import messagebox
import time

class EyeBreakApp:
    def __init__(self, master):
        self.master = master
        master.title("Eye Break Reminder")

        self.work_duration = 180  # 3 minutes in seconds
        self.break_duration = 9  # 9 seconds

        self.label = tk.Label(master, text="Time to the next break:")
        self.label.pack()

        self.time_left_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.time_left_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.is_running = False
        self.remaining_time = self.work_duration
        self.update_time_left_label()

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.countdown()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def countdown(self):
        if self.is_running and self.remaining_time > 0:
            self.update_time_left_label()
            self.remaining_time -= 1
            self.master.after(1000, self.countdown)
        elif self.is_running and self.remaining_time == 0:
            self.take_break()

    def take_break(self):
        self.is_running = False
        messagebox.showinfo("Break Time", "Time for a break!")
        self.master.after(self.break_duration * 1000, self.post_break)

    def post_break(self):
        self.remaining_time = self.work_duration
        self.update_time_left_label()
        self.start_timer()

    def update_time_left_label(self):
        mins, secs = divmod(self.remaining_time, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        self.time_left_label.config(text=time_format)

if __name__ == "__main__":
    root = tk.Tk()
    app = EyeBreakApp(root)
    root.mainloop()