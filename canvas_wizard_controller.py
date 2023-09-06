import tkinter as tk
import subprocess
import os

# Store the process ID of the running air_canvas_ml.py script
running_process = None

def start_project():
    global running_process
    # Replace 'python air_canvas_ml.py' with the actual command to start your Python project
    running_process = subprocess.Popen(['python', 'air_canvas_ml.py'])

def stop_project():
    global running_process
    if running_process:
        # Terminate the running process
        running_process.terminate()
        running_process = None
    # Close the controller script
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("CanvasWizard Controller")

# Create buttons to start and stop the project
start_button = tk.Button(root, text="Start Drawing", command=start_project)
stop_button = tk.Button(root, text="Stop Drawing", command=stop_project)

# Place the buttons in the window
start_button.pack()
stop_button.pack()

# Start the Tkinter main loop
root.mainloop()
