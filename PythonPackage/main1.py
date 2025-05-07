from tkinter import *
from tkinter import messagebox
import tkinter as tr
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image,ImageTk
import seaborn as sns
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
        Label(text="Equation for Graph").place(x=8,y=18)
        
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
    root=tk.Tk()
    calculator=ScientificCalculator(root)
    root.mainloop()

def BMICalculator():
    root=Tk()
    root.title("BMI Calculator")
    root.geometry("470x590")
    root.resizable(False,False)
    root.configure(bg="#f0f1f5")

    def BMI():
        h=float(Height.get())
        w=float(Weight.get())

        file1=open("bmi.txt","a")
        file1.write(str(h)+" : "+str(w)+'\n')
        file1.close()

        m=h/100.0
        bmi=round(float(w/m**2),1)
        print(bmi)
        label1.config(text=bmi)
    
        if bmi<=18.5:
            label2.config(text="Underweight!")
            label3.config(text="you have lower weight then normal body !")
        elif bmi>18.5 and bmi<25:
            label2.config(text="Normal")
            label3.config(text="It indicates that you are healthy joy!")
        elif bmi>25 and bmi <=30:    
            label2.config(text="Overweight!")
            label3.config(text="It indicated that a person is \n slightly overweight!\n A doctor may advise to lose some \n weight for health reason \n ! !")
        else:
            label2.config(text="Obes!")
            label3.config(text="Health my be at risk ,if they do not \n lose weight !")

    #icon
    image_icon=PhotoImage(file="icon.png")
    root.iconphoto(False,image_icon)

    #top
    top=PhotoImage(file="top.png")
    top_image=Label(root,image=top,background='#f0f1f5')
    top_image.place(x=-10,y=-10)

    #bottom box
    Label(root,width=72,height=21,bg="lightblue").pack(side=BOTTOM)

    #two boxes
    box=PhotoImage(file="box.png")
    Label(root,image=box).place(x=20,y=70)
    Label(root,image=box).place(x=240,y=70)

    #scale
    scale=PhotoImage(file="scale.png")
    Label(root,image=scale,bg="lightblue").place(x=20,y=310)
    
    current_value=tk.DoubleVar()
    def get_current_value():
        return '{: .2f}'.format(current_value.get())

    def slider_changed(event):
       Height.set(get_current_value())
   
       size=int(float(get_current_value()))
       img=(Image.open("man.png"))
       resized_image=img.resize((50,10+size))
       photo2=ImageTk.PhotoImage(resized_image)
       secondimage.config(image=photo2)
       secondimage.place(x=70,y=550-size)
       secondimage.image=photo2
   
    
    style=ttk.Style()
    style.configure("TScale",background="white")
    Label(text="Height in cms").place(x=80,y=120)
    slider=ttk.Scale(root,from_=0, to=300,orient='horizontal',style="TScale",command=slider_changed,variable=current_value)
    slider.place(x=80,y=210)
    

    current_value2=tk.DoubleVar()
    def get_current_value2():
        return '{: .2f}'.format(current_value2.get())

    def slider_changed2(event):
       Weight.set(get_current_value2())
   

    style2=ttk.Style()
    style2.configure("TScale",background="white")
    Label(text="Weight in kgs").place(x=300,y=120)
    slider2=ttk.Scale(root,from_=0, to=300,orient='horizontal',style="TScale",command=slider_changed2,variable=current_value2)
    slider2.place(x=300,y=210)
    
    Height=StringVar()
    Weight=StringVar()
    height=Entry(root,text="HEIGHT IN CMS",textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
    height.place(x=35,y=150)
    Height.set(get_current_value())
    
    weight=Entry(root,text="WEIGHT",textvariable=Weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
    weight.place(x=255,y=150)
    Weight.set(get_current_value2())
    
    secondimage=PhotoImage("man.png")
    secondimage=Label(root,bg="lightblue")
    secondimage.place(x=70,y=530)
    Button(root,text="View Report ",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=350)
    
    label1=Label(root,font="arial 40 bold ",bg="lightblue",fg="#fff")
    label1.place(x=150,y=300)
    
    label2=Label(root,font="arial 20 bold ",bg="lightblue",fg="#3b3a3a")
    label2.place(x=200,y=440)
    
    label3=Label(root,font="arial 10 ",bg="lightblue")
    label3.place(x=200,y=470)

    root.mainloop()

def WeatherApp():
    process=Tk()
    process.title("Weather App")
    process.geometry("900x500")
    process.resizable(False,False)

    def getWeather():
        try:
            cityName=textfield.get()
            geolocator=Nominatim(user_agent="geoapiExercises")
            location=geolocator.geocode(cityName)
            print(location)
            obj1=TimezoneFinder()
            result=obj1.timezone_at(lng=location.longitude,lat=location.latitude)
            print(result)
            home=pytz.timezone(result)
            localTime=datetime.now(home)

            currentTime=localTime.strftime("%I:%M %p")
            clock.config(text=currentTime)
            name.config(text="CURRENT WEATHER:")

            application="https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=bad6bdab51b6449ee6ca3f7b183ef54b"
            weatherData=requests.get(application).json()

            condition=weatherData['weather'][0]['description']
            temp1=int(weatherData['main']['temp']-273.15)
            pressure=weatherData['main']['pressure']
            humidity=weatherData['main']['humidity']
            wind=weatherData['wind']['speed']

            temp.config(text=(temp1,"C"))
            c.config(text=(condition,"|","FEELS","LIKE"))
            w.config(text=wind)
            h.config(text=humidity)
            p.config(text=pressure)

            file1=open("weatherData.txt","a")
            file1.write(str(location))
            file1.write(str(temp1))
            file1.close()

        except Exception as e:
            messagebox.showerror("Weather app","Network error or Invalid Input!")

    # search
    searchImage=PhotoImage(file='searchbox.png')
    image1=Label(image=searchImage)
    image1.place(x=20,y=20)

    textfield=Entry(process,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
    textfield.place(x=50,y=40)
    textfield.focus()

    searchIcon=PhotoImage(file="iconWeather.png")
    image2=Button(image=searchIcon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
    image2.place(x=420,y=34)

    searchLogo=PhotoImage(file="weather.png")
    image3=Label(image=searchLogo)
    image3.place(x=200,y=150)

    searchFrame=PhotoImage(file="frame.png")
    image4=Label(image=searchFrame)
    image4.pack(padx=5,pady=5,side=BOTTOM)

    # time
    name=Label(process,font=("arial",15,"bold"))
    name.place(x=100,y=100)
    clock=Label(process,font=("arial",20))
    clock.place(x=30,y=130)

    label1=Label(process,text="WIND",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
    label1.place(x=160,y=400)

    label2=Label(process,text="HUMIDITY",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
    label2.place(x=365,y=400)

    label4=Label(process,text="PRESSURE",font=("Calibi",15,'bold'),fg="white",bg="#1ab5ef")
    label4.place(x=600,y=400)

    temp=Label(font=("arial",70,"bold"),fg="#ee666d")
    temp.place(x=400,y=150)

    c=Label(font=("arial",15,'bold'))
    c.place(x=400,y=250)

    w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
    w.place(x=170,y=430)

    h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
    h.place(x=370,y=430)

    p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
    p.place(x=610,y=430)

    process.mainloop()



root = Tk()
root.geometry("850x500+300+170")
root.resizable(False, False)

Body = Frame(root, width=900, height=600, bg="#d6d6d6")
Body.pack(padx=20, pady=20)

RHB = Frame(Body, width=470, height=190, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHB.place(x=10, y=10)

# Load images
app1Image = PhotoImage(file='weather.png').subsample(2, 2)
app2Image = PhotoImage(file='icon.png').subsample(5, 5)
app3Image = PhotoImage(file='calculatorIcon1.png').subsample(3, 3)

# Create buttons
app1 = Button(RHB, image=app1Image, bd=0, command=WeatherApp)
app1.image = app1Image
app1.place(x=15, y=5)

app2 = Button(RHB, image=app2Image, bd=0, command=BMICalculator)
app2.image = app2Image
app2.place(x=150, y=5)

app3 = Button(RHB, image=app3Image, bd=0, command=Scientific)
app3.image = app3Image
app3.place(x=285, y=5)

root.mainloop()
