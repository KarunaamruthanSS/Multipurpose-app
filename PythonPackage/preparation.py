import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class CombinedCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Combined Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Scientific Calculator icon
        sci_icon = Image.open("weather.png")
        sci_icon = sci_icon.resize((100, 100), Image.ANTIALIAS)
        sci_icon = ImageTk.PhotoImage(sci_icon)
        scientific_icon = tk.Button(self.master, image=sci_icon, command=self.open_scientific_calculator)
        scientific_icon.image = sci_icon
        scientific_icon.grid(row=0, column=0, padx=20, pady=20)

        # BMI Calculator icon
        bmi_icon = Image.open("icon.png")
        bmi_icon = bmi_icon.resize((100, 100), Image.ANTIALIAS)
        bmi_icon = ImageTk.PhotoImage(bmi_icon)
        bmi_icon = tk.Button(self.master, image=bmi_icon, command=self.open_bmi_calculator)
        bmi_icon.image = bmi_icon
        bmi_icon.grid(row=0, column=1, padx=20, pady=20)

    def open_scientific_calculator(self):
        self.master.destroy()  # Close the combined calculator window
        scientific_root = tk.Tk()
        scientific_calculator = ScientificCalculator(scientific_root)
        scientific_root.mainloop()

    def open_bmi_calculator(self):
        self.master.destroy()  # Close the combined calculator window
        bmi_root = tk.Tk()
        bmi_calculator = BMICalculator(bmi_root)
        bmi_root.mainloop()


class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.create_widgets()

    # Add your Scientific Calculator code here

class BMICalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        self.create_widgets()

    # Add your BMI Calculator code here


if __name__ == "__main__":
    root = tk.Tk()
    calculator = CombinedCalculator(root)
    root.mainloop()
