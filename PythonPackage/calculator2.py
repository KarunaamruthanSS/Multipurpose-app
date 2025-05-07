import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ScientificCalculator:
    def __init__(self,master):
        self.master=master
        self.master.title("Scientific Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying and entering calculations
        self.entry=tk.Entry(self.master,width=40,font=('Arial',14))
        self.entry.grid(row=0,column=0,columnspan=80,pady=40)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),]

        for (text, row, col) in buttons:
            ttk.Button(self.master, text=text, command=lambda t=text: self.button_click(t)).grid(row=row, column=col)

        # Graph Button
        ttk.Button(self.master, text='Plot Graph', command=self.plot_graph).grid(row=5, column=0, columnspan=4, pady=10)

    def button_click(self, text):
        current_text = self.entry.get()

        if text == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

    def plot_graph(self):
        # Sample data for plotting
        #equation=()
        x = [1, 2, 3, 4, 5]
        y = [x_i ** 2 for x_i in x]

        # Plotting using Seaborn
        sns.set(style="whitegrid")
        plt.figure(figsize=(6, 4))
        sns.lineplot(x=x, y=y, marker='o', color='b')
        plt.title('Graph of x^2')
        plt.xlabel('x')
        plt.ylabel('y = x^2')

        # Embed the plot in Tkinter window
        figure_canvas = FigureCanvasTkAgg(plt.gcf(), master=self.master)
        figure_canvas.get_tk_widget().grid(row=6, column=0, columnspan=4)
        figure_canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
