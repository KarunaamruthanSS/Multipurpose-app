from tkinter import *
import pPackage1 as weather
import BMI as b
import caluclator3 as c

flagg=1
flag=1

def launch_weather_app():
    root.destroy()
    weather.WeatherApp()
    flagg=1

def launch_bmi_calculator():
    root.destroy()
    b.BMICalculator()
    flagg=1

def launch_calculator():
    root.destroy()
    c.Scientific()
    flagg=1
    
def core():
    
    global root
    root=Tk()
    root.geometry("550x300+300+170")
    root.resizable(False,False)

    Body=Frame(root,width=900,height=600,bg="#d6d6d6")
    Body.pack(padx=20,pady=20)
    RHB=Frame(Body,width=470,height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
    RHB.place(x=10,y=10)

    # Load images
    app1Image=PhotoImage(file='weather.png').subsample(2,2)
    app2Image=PhotoImage(file='icon.png').subsample(5,5)
    app3Image=PhotoImage(file='calculatorIcon1.png').subsample(3,3)

    # Create buttons
    app1=Button(RHB, image=app1Image, bd=0, command=launch_weather_app)
    app1.image = app1Image
    app1.place(x=15, y=5)

    app2=Button(RHB, image=app2Image, bd=0, command=launch_bmi_calculator)
    app2.image = app2Image
    app2.place(x=150, y=5)

    app3=Button(RHB, image=app3Image, bd=0, command=launch_calculator)
    app3.image = app3Image
    app3.place(x=285, y=5)

    if(flagg==1):
        flag=1
    else:
        flag=0
        
    root.mainloop()

while(flag!=0):
    print(flag)
    core()
    
    
