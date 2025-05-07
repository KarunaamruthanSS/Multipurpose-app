from tkinter import *
import tkinter as tk
from tkinter import ttk
import pPackage1 as weather
import BMI as b
import caluclator3 as c
import os
import seaborn as sns
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ScientificCalculator:
    def __init__(self,master):
        self.master=master
        self.master.title("Scientific Calculator")
        self.create_widgets()

    def create_widgets(self):

        style=ttk.Style()
        style.configure("TScale",background="white")
        
        self.equationEntry=tk.Entry(self.master,width=40,font=('Arial',14))
        self.equationEntry.grid(row=0,column=0,columnspan=80,pady=10)

        self.entry=tk.Entry(self.master,width=40,font=('Arial',14))
        self.entry.grid(row=1,column=0,columnspan=80,pady=10)

        # Buttons
        buttons=[
            ('7', 2, 0),('8', 2, 1),('9', 2, 2),('/', 2, 3),
            ('4', 3, 0),('5', 3, 1),('6', 3, 2),('*', 3, 3),
            ('1', 4, 0),('2', 4, 1),('3', 4, 2),('-', 4, 3),
            ('0', 5, 0),('.', 5, 1),('=', 5, 2),('+', 5, 3)]

        for(text,row,col)in buttons:
            ttk.Button(self.master,text=text,command=lambda t=text:self.button_click(t)).grid(row=row,column=col)

        ttk.Button(self.master,text='Plot Graph',command=self.plot_graph).grid(row=6,column=0,columnspan=4,pady=10)

    def button_click(self,text):
        currentText=self.entry.get()

        if text=='=':
            try:
                result=eval(currentText)
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END,str(result))
            except Exception as e:
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END,"Error")
        else:
            self.entry.insert(tk.END, text)

    def plot_graph(self):
        threading.Thread(target=self.plot_graph_thread).start()

    def plot_graph_thread(self):
        equation=self.equationEntry.get()
        x=np.linspace(-10,10,100)
        try:
            y=eval(equation)
        except Exception as e:
            y=np.zeros_like(x)

        plt.figure(figsize=(6,4))
        plt.plot(x,y,color='b')
        plt.title(f'Graph of {equation}')
        plt.xlabel('x')
        plt.ylabel(f'y={equation}')
    
        figure_canvas=FigureCanvasTkAgg(plt.gcf(),master=self.master)
        figure_canvas.get_tk_widget().grid(row=7,column=0,columnspan=4)
        figure_canvas.draw()


def Scientific():
    global root
    root=tk.Tk()
    calculator=ScientificCalculator(root)
    root.mainloop()

Scientific()
