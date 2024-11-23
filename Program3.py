import tkinter as tk
from tkinter import messagebox


def calculate_charge():
    selected_category = rate_category.get()

    try:
        minutes = float(minutes_entry.get())
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")
    except ValueError as e:
        return

    if selected_category == "Daytime":
        rate = 0.02
    elif selected_category == "Evening":
        rate = 0.12
    elif selected_category == "Off-Peak":
        rate = 0.05


    total_charge = minutes * rate

    messagebox.showinfo("Total Charge", f"The total charge for the call is: ${total_charge:.2f}")


root = tk.Tk()
root.title("Call Charge Calculator")

rate_category = tk.StringVar()

daytime_button = tk.Radiobutton(root, text="Daytime (6:00 AM - 5:59 PM) - $0.02/min", variable=rate_category,
                                value="Daytime")
evening_button = tk.Radiobutton(root, text="Evening (6:00 PM - 11:59 PM) - $0.12/min", variable=rate_category,
                                value="Evening")
offpeak_button = tk.Radiobutton(root, text="Off-Peak (Midnight - 5:59 AM) - $0.05/min", variable=rate_category,
                                value="Off-Peak")

daytime_button.pack()
evening_button.pack()
offpeak_button.pack()

minutes_label = tk.Label(root, text="Enter the number of minutes of the call:")
minutes_label.pack()

minutes_entry = tk.Entry(root)
minutes_entry.pack()

calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.pack()

root.mainloop()