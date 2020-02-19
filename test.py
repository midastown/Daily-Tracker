from tkinter import *

window = Tk()

var = IntVar()

check = Checkbutton(window, variable=var)

if var == 0:
    print("var equals 0 in pure form")
else:
    print("var does not equal an int")
    

