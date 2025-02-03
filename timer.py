import time
import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize pygame mixer
pygame.mixer.init()

def play_sound():
    """Plays the alarm sound."""
    try:
        pygame.mixer.music.load("/Users/RyanYunseokChoi/Documents/Coding/Timer/alarm.mp3")  # Load the alarm sound
        pygame.mixer.music.play()  # Play the sound
    except pygame.error as e:
        messagebox.showerror("Error", f"Sound playback failed: {e}")

def update_timer(x):
    global timer_running, timer_paused
    
    if not timer_running:
        return  # Stop execution when "Stop Timer" is clicked
    
    while timer_paused:
        main.update()
        time.sleep(0.1)  

    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    time_str.set(f'{hours:02}:{minutes:02}:{seconds:02}')
    
    if x > 0:
        main.after(1000, update_timer, x - 1)  # Schedule next update after 1 second
    else:
        time_str.set("00:00:00")  # Set to 00:00:00 when done
        play_sound()  # Play the sound
        messagebox.showinfo("Notification", "Time's Up!")

def start_timer():
    global timer_running, timer_paused
    timer_running = True
    timer_paused = False
    
    try:
        my_time = int(entry.get()) * 60  # Convert minutes to seconds
        update_timer(my_time)  # Start countdown
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

def stop_timer():
    global timer_running
    timer_running = False
    time_str.set("00:25:00")

def hold_timer():
    global timer_paused
    if timer_running:
        timer_paused = not timer_paused
        hold_button.config(text="Resume Timer" if timer_paused else "Hold Timer")

# Update button setup with click effects
def button_click_effect(button):
    original_color = button.cget("bg")
    button.config(bg="yellow")
    button.after(200, lambda: button.config(bg=original_color))

# Create the main window (Create an instance of the Tk class)
main = tk.Tk()
main.title("Countdown TImer")

# Declaration of Tkinter variable
time_str = tk.StringVar()
# Initialization of Tkinter variables
time_str.set("00:25:00")

# Create the label widget (Create an instance of the Label class)
label = tk.Label(main, text="Enter time in minutes", font=("Helvetica", 14))
# Pack the label into the window
label.pack(pady=10) # Add some padding to the top

# Creat the entry widget
entry = tk.Entry(main, font=("Helvetica", 14))
entry.insert(0, "25")
entry.pack(pady=10)

# Create the label widget for displaying time
time_display = tk.Label(main, textvariable=time_str, font=("Helvetica", 24), bg="black", fg="#90EE90")
time_display.pack(pady=20)

# Create the button to run 'start_timer' function
start_button = tk.Button(main, text="Start Timer", command=lambda: [button_click_effect(start_button), start_timer()], font=("Helvetica", 14))
start_button.pack(pady=10)

stop_button = tk.Button(main, text="Stop Timer", command=lambda: [button_click_effect(stop_button), stop_timer()], font=("Helvetica", 14))
stop_button.pack(pady=1)

# Create the button to hold fuction
hold_button = tk.Button(main, text="Hold Timer", command=lambda: [button_click_effect(hold_button), hold_timer()], font=("Helvetica", 14))
hold_button.pack(pady=10)

# run the applications
main.mainloop()