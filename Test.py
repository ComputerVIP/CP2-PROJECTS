from tkinter import *  # Import all Tkinter functions
from tkinter import ttk  # Import themed Tkinter widgets
from test2 import calculate  # Import the calculate function from test2.py

# Create the main application window
root = Tk()  
root.title("Feet to Meters")  # Set the window title

# Create a main frame inside the window with padding
# Padding values: Left (3), Top (3), Right (12), Bottom (12)
mainframe = ttk.Frame(root, padding="3 3 12 12")  
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Expand in all directions

# Configure resizing behavior
root.columnconfigure(0, weight=1)  # Allow column expansion
root.rowconfigure(0, weight=1)  # Allow row expansion

# Define a variable to store user input (feet)
feet = StringVar()

# Create an entry field for feet input
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  

feet_entry.grid(column=2, row=1, sticky=(W, E))  # Expand entry field horizontally

# Define a variable to store the output (meters)
meters = StringVar()

# Create a label to display the converted meters value
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))  

# Create a button that calls the 'calculate' function when pressed
# Uses lambda to pass 'feet' and 'meters' as arguments
ttk.Button(mainframe, text="Calculate", command=lambda: calculate(feet, meters)).grid(column=3, row=3, sticky=W)

# Create labels for user instructions
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)  
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)  
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)  

# Add padding to all child widgets inside 'mainframe' for better spacing
for child in mainframe.winfo_children():  
    child.grid_configure(padx=5, pady=5)  

# Set focus to the feet entry field for immediate input
feet_entry.focus()  

# Bind the 'Enter' key to trigger the 'calculate' function
root.bind("<Return>", lambda event: calculate(feet, meters))  

# Set the default window size (300x300 pixels)
root.geometry('300x300')  

# Allow the window to be resized in both width and height
root.resizable(True, True)  

# Start the Tkinter event loop (keeps the window open and responsive)
root.mainloop()
