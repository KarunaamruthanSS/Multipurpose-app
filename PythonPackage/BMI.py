from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import pPackage1 as weather
import BMI as b
import caluclator3 as c

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
	height=Entry(root,text="HEIGHT IN CMS",textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)#to align text in center
	height.place(x=35,y=150)
	Height.set(get_current_value())
	
	weight=Entry(root,text="WEIGHT",textvariable=Weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)#to align text in center
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

BMICalculator()

