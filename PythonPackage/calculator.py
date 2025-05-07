import numpy as _
import matplotlib.pyplot as plt

def calculatorMode():
    print("***NORMAL CALCULATOR MODE***")
    temp=""

    while temp!="q":
        try:
            temp=input("Enter the problem: ")
            print(eval(bytes([ord(p) for p in temp])))

        except:
            if temp is "q":
                print("Invalid Input")

def graphMode():
    print("***GRAPH MODE***")
    graph,x,y="",0,0

    while graph!="q":
        try:
            graph=input("Enter Equation: ")
            if graph=="q":
                break

            x=input("Enter the range: ")
            if x=="q":
                break
            else:
                x=int(x)

            y=input("Enter the range: ")
            if y=="q":
                break
            else:
                y=int(y)

            x=numpy.array(range(int(x),int(y)))
            y=eval(bytes([ord(p) for p in graph]))
            plt.plot(x,y)
            plt.show()

        except:
            if graph!="q":
                print("Invalid Input")

mode=""

while mode!="q":
    print("\n PRESS c - NORMAL CALCULATION \n PRESS g - GRAPHICS \n PRESS h - HELP \n PRESS q - QUIT")

    mode=input().lower()
    if mode=="c":
        calculatorMode()
    elif mode=="g":
        graphMode()
    elif mode=="h":
        print("\n 1. Do not use parenthese while multiplying. \n Put 'numpy.' before using any of the numpy functions")

    
    print(" ")
