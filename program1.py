import tkinter as tk
from tkinter import messagebox

class CarMPGCalculator:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Car MPG Calculator")

        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        self.gallons_label = tk.Label(self.top_frame, text="Gallons of gas the car holds:")
        self.miles_label = tk.Label(self.top_frame, text="Miles on a full tank:")

        self.gallons_entry = tk.Entry(self.top_frame)
        self.miles_entry = tk.Entry(self.top_frame)

        self.gallons_label.pack()
        self.gallons_entry.pack()
        self.miles_label.pack()
        self.miles_entry.pack()

        self.calculate_button = tk.Button(self.bottom_frame, text="Calculate MPG", command=self.calculate_mpg)

        self.calculate_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.main_window.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())

            if gallons <= 0:
                raise ValueError("Gallons must be greater than zero.")
            if miles <= 0:
                raise ValueError("Miles must be greater than zero.")

            mpg = miles / gallons

            messagebox.showinfo("MPG Result", f"The car's miles per gallon (MPG) is: {mpg:.2f}")

        except ValueError as e:
            messagebox.showerror("Input Error", f"Please enter valid numbers. {str(e)}")

if __name__ == "__main__":
    car_mpg_calculator = CarMPGCalculator()