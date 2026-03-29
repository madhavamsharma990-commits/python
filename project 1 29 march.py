import tkinter as tk
from datetime import date
from tkinter import messagebox

def calculate_age():
    try:
        # Get input values
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())
        
        # Current date
        today = date.today()
        birth_date = date(birth_year, birth_month, birth_day)
        
        # Calculation logic
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display result
        result_label.config(text=f"Your Age is: {age} Years", fg="blue")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Date, Month, and Year.")

# Initialize Main Window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("300x250")
root.config(padx=20, pady=20)

# Labels and Entry fields using Grid Geometry Manager
tk.Label(root, text="Date of Birth", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Day:").grid(row=1, column=0, sticky="e")
day_entry = tk.Entry(root, width=10)
day_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Month:").grid(row=2, column=0, sticky="e")
month_entry = tk.Entry(root, width=10)
month_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Year:").grid(row=3, column=0, sticky="e")
year_entry = tk.Entry(root, width=10)
year_entry.grid(row=3, column=1, pady=5)

# Calculate Button
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="green", fg="white")
calc_button.grid(row=4, column=0, columnspan=2, pady=15)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()