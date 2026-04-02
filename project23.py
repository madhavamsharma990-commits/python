import tkinter as tk
from tkinter import messagebox

def convert_inches_to_cm():
    """
    This function is the 'Event Handler'. 
    It is triggered when the 'Convert' button is clicked.
    """
    try:
        # Get the input value from the Entry widget
        inches = float(entry_inches.get())
        
        # Perform the conversion (1 inch = 2.54 cm)
        cm = inches * 2.54
        
        # Display the result in the label
        label_result.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        # Error handling if the user enters non-numeric text
        messagebox.showerror("Input Error", "Please enter a valid number for inches.")

# 1. Create the main application window
root = tk.Tk()
root.title("Length Converter")
root.geometry("300x150")

# 2. Create and place widgets
label_instruction = tk.Label(root, text="Enter length in inches:")
label_instruction.pack(pady=5)

entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

# The 'command' parameter links the button click to our event function
btn_convert = tk.Button(root, text="Convert", command=convert_inches_to_cm)
btn_convert.pack(pady=5)

label_result = tk.Label(root, text="", font=("Helvetica", 10, "bold"))
label_result.pack(pady=5)

# 3. Start the application event loop
root.mainloop()
