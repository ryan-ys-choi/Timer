import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        my_time = int(entry.get())
        for x in range(my_time * 60, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f'{hours:02}:{minutes:02}:{seconds:02}')
            main.update() # a method to process all pending events in the Tkinter event queue and updates the display accordingly
            time.sleep(1)
        time_str.set("00:00:00")
        messagebox.showinfo("Notification", "Time's Up!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number ")

print("Time's Up!")

# Create the main window (Create an instance of the Tk class)
main = tk.Tk()
main.title("Countdown TImer")

# Declaration of Tkinter variable
time_str = tk.StringVar()
# Initialization of Tkinter variables
time_str.set("00:00:00")

# Create the label widget (Create an instance of the Label class)
label = tk.Label(main, text="Enter time in minutes", font=("Helvetica", 14))
# Pack the label into the window
label.pack(pady=10) # Add some padding to the top

# Creat the entry widget
entry = tk.Entry(main, font=("Helvetica", 14))
entry.pack(pady=10)

# Create the label widget for displaying time
time_display = tk.Label(main, textvariable=time_str, font=("Helvetica", 24), bg="black", fg="white")
time_display.pack(pady=20)

# Create the button to run 'start_timer' function
start_button = tk.Button(main, text="Start Timer", command=start_timer, font=("Helvetica", 14))
start_button.pack(pady=10)

# run the application
main.mainloop()