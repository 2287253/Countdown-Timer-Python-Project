import tkinter as tk
from tkinter import ttk
import time
import winsound
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Variables
        self.hours = tk.StringVar(value="0")
        self.minutes = tk.StringVar(value="0")
        self.seconds = tk.StringVar(value="0")
        self.is_running = False
        self.remaining_time = 0
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create time input frame
        self.time_frame = ttk.Frame(self.main_frame)
        self.time_frame.pack(pady=20)
        
        # Hours input
        ttk.Label(self.time_frame, text="Hours:").grid(row=0, column=0, padx=5)
        self.hours_entry = ttk.Entry(self.time_frame, textvariable=self.hours, width=5)
        self.hours_entry.grid(row=0, column=1, padx=5)
        
        # Minutes input
        ttk.Label(self.time_frame, text="Minutes:").grid(row=0, column=2, padx=5)
        self.minutes_entry = ttk.Entry(self.time_frame, textvariable=self.minutes, width=5)
        self.minutes_entry.grid(row=0, column=3, padx=5)
        
        # Seconds input
        ttk.Label(self.time_frame, text="Seconds:").grid(row=0, column=4, padx=5)
        self.seconds_entry = ttk.Entry(self.time_frame, textvariable=self.seconds, width=5)
        self.seconds_entry.grid(row=0, column=5, padx=5)
        
        # Timer display
        self.timer_label = ttk.Label(self.main_frame, text="00:00:00", font=("Arial", 48))
        self.timer_label.pack(pady=20)
        
        # Buttons frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=20)
        
        # Start button
        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Pause button
        self.pause_button = ttk.Button(self.button_frame, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        # Reset button
        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Validation
        self.hours.trace_add("write", self.validate_input)
        self.minutes.trace_add("write", self.validate_input)
        self.seconds.trace_add("write", self.validate_input)
    
    def validate_input(self, *args):
        for var in [self.hours, self.minutes, self.seconds]:
            try:
                value = int(var.get())
                if value < 0:
                    var.set("0")
            except ValueError:
                var.set("0")
    
    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            
            # Calculate total seconds
            h = int(self.hours.get())
            m = int(self.minutes.get())
            s = int(self.seconds.get())
            self.remaining_time = h * 3600 + m * 60 + s
            
            self.update_timer()
    
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
    
    def reset_timer(self):
        self.is_running = False
        self.remaining_time = 0
        self.update_display()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
    
    def update_timer(self):
        if self.is_running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
            self.root.after(1000, self.update_timer)
        elif self.remaining_time == 0 and self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            # Play sound when timer completes
            winsound.Beep(1000, 1000)  # Frequency: 1000Hz, Duration: 1000ms
    
    def update_display(self):
        hours = self.remaining_time // 3600
        minutes = (self.remaining_time % 3600) // 60
        seconds = self.remaining_time % 60
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop() 