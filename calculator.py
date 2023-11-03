from tkinter import *

# Creates The Window To Do The calculations
windowRoot = Tk()
windowRoot.geometry("312x324")  # (width x height)
windowRoot.resizable(0, 0)
windowRoot.title("CALCULATOR")

# Buttons For The Calculator
def buttons(item):   # 
    global math
    math = math + str(item)
    inputText.set(math)

def clearButton():
    global math
    math = " "
    inputText.set(" ")
    
def equalButton():
    global math
    result = str(eval(math))
    inputText.set(result)
    math = " "

math = " "
inputText = StringVar()