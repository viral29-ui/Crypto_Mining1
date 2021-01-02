from tkinter import *  #
import time # For time module everything as imported of time library


def times(): # Create a variable times since time is the name of module
    time_string = time.strftime("%I:%M:%S %D ") # Variable time_string
    clock.config(text=time_string) # Configure clock base on your current system time
    clock.after(200, times) # It can change 200 microsecond in timeframe


root = Tk() # Create a variable Tk variable window
clock = Label(root, font=("Arial", 50),fg="#00FF00",bg="black") # Define the clock frame as it look
clock.grid(row=2,column=2, pady=25, padx=100) # Clock grid as pading of y is 25 and x-axis 100
times() # Call the time function
digi = Label(root, text = "Digital clock", font = "Times 24 bold") # As seen of clock name
root.mainloop() # Create a variable for digital clock
# Update 2