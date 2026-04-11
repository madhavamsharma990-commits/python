import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Retrieve and convert user inputs
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        
        # Simple Interest Formula: SI = (P * R * T) / 100
        si = (p * r * t) / 100
        
        # Compound Interest Formula: CI = P * (1 + R/100)^T - P
        # Assumes annual compounding
        amount = p * (pow((1 + r / 100), t))
        ci = amount - p
        
        # Update results in the interface
        label_si_result.config(text=f"Simple Interest: {si:.2f}")
        label_ci_result.config(text=f"Compound Interest: {ci:.2f}")
        
    except ValueError:
        # Handle cases where inputs are not valid numbers
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

# UI Layout: Principal Amount
tk.Label(root, text="Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

# UI Layout: Rate of Interest
tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

# UI Layout: Time Period
tk.Label(root, text="Time Period (Years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

# Calculation Button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest)
btn_calculate.pack(pady=15)

# Output Labels
label_si_result = tk.Label(root, text="Simple Interest: 0.00", font=("Arial", 10, "bold"))
label_si_result.pack()

label_ci_result = tk.Label(root, text="Compound Interest: 0.00", font=("Arial", 10, "bold"))
label_ci_result.pack()

# Start the application
root.mainloop()
