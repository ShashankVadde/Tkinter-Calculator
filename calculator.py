from tkinter import *

# Creates The Window To Do The calculations
windowRoot = Tk()
windowRoot.geometry("350x390")  # (width x height)
windowRoot.resizable(0, 0)
windowRoot.title("Calculator")


math = " "
# Buttons For The Calculator
def buttons(item):   
    global math
    math = math + str(item)
    inputText.set(math)

# Clears the frame
def clearButton():
    global math
    math = " "
    inputText.set(" ")

# Result of the operations
def equalButton():
    global math
    try: 
        result = str(eval(math))
        inputText.set(result)
        math = result  # This line of code allows the user to do more opeartions on the output of the prevous operation
    except Exception as e:
        inputText.set("Invalid")
        
# Deletes the individual numbers in the frame
def deleteButton():
    global math
    math = math[:-1]
    inputText.set(math)

inputText = StringVar()

# Frame on the top of the window
inputFrame = Frame(windowRoot, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
inputFrame.pack(side = TOP)

# Field where all the inputs will be placed
inputField = Entry(inputFrame, font = ('arial', 30, 'bold'), textvariable = inputText, width = 50, bg = "#d8d7bf", bd = 0, justify = RIGHT)
inputField.grid(row = 0, column = 0)
inputField.pack(ipady = 10)

# Buttons inside the frame for the input
frameButtons = Frame(windowRoot, width = 312, height = 272.5, bg = "grey")
frameButtons.pack()

# Button Placement to Clear the frame
clear = Button(frameButtons, text = "Clear", fg = "white", width = 35, height = 3, bd = 5, bg = "#12239e", cursor = "hand2", command = clearButton)
clear.grid(row = 4, column = 0, columnspan = 3, padx = 1, pady = 1)


# Button placement for the result of the input
equal = Button(frameButtons, font = ('arial', 9, 'bold'), text = "=", fg = "white", width = 10, height = 3, bd = 5, bg = "#5f6b6d", cursor = "hand2", command = equalButton)
equal.grid(row = 4, column = 3, padx = 1, pady = 1)

# Button placement to delete the individual numbers from the frame
delete = Button(frameButtons, text = "Del", fg = "white", width = 10, height = 3, bd = 5, bg = "#12239e", cursor = "hand2", command = deleteButton)
delete.grid(row = 3, column = 2, padx = 1, pady = 1)

# List of all of the buttons
buttonsData = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 3), ("+", 3, 3)
]

for (text, row, column) in buttonsData:
    button = Button(frameButtons, text = text, font = ('arial', 9, 'bold'), fg = "black", width = 10, height = 3, bd = 5, bg = "#ffd86c" if text.isdigit() or text == "." else "#eee", cursor = "hand2", command = lambda t=text: buttons(t))
    button.grid(row = row, column = column, padx = 1, pady = 1)
    
windowRoot.mainloop()
