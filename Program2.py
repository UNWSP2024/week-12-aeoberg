import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Service Selection")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.oil_change_var = tkinter.IntVar()
        self.lube_job_var = tkinter.IntVar()
        self.radiator_flush_var = tkinter.IntVar()
        self.transmission_fluid_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_replacement_var = tkinter.IntVar()
        self.tire_rotation_var = tkinter.IntVar()

        self.oilChange = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.oil_change_var)
        self.lubeJob = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.lube_job_var)
        self.radiatorFlush = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.radiator_flush_var)
        self.transmissionFluid = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.transmission_fluid_var)
        self.inspection = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.inspection_var)
        self.mufflerReplacement = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.muffler_replacement_var)
        self.tireRotation = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.tire_rotation_var)

        self.oilChange.pack()
        self.lubeJob.pack()
        self.radiatorFlush.pack()
        self.transmissionFluid.pack()
        self.inspection.pack()
        self.mufflerReplacement.pack()
        self.tireRotation.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.quit)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        total_charge = 0

        if self.oil_change_var.get() == 1:
            total_charge += 30.00
        if self.lube_job_var.get() == 1:
            total_charge += 20.00
        if self.radiator_flush_var.get() == 1:
            total_charge += 40.00
        if self.transmission_fluid_var.get() == 1:
            total_charge += 100.00
        if self.inspection_var.get() == 1:
            total_charge += 35.00
        if self.muffler_replacement_var.get() == 1:
            total_charge += 200.00
        if self.tire_rotation_var.get() == 1:
            total_charge += 20.00

        tkinter.messagebox.showinfo('Total Charge', f"The total charge for selected services is: ${total_charge:.2f}")


if __name__ == '__main__':
    my_gui = MyGUI()