from tkinter import*



root = Tk()
root.geometry("1000x500+0+0")
root.title("Dojo Python3")

text_input = StringVar()
operator = ""

Tops = Frame(root, width = 1600, height = 80, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

frame = Frame(root, width = 300, height = 700, bg = "powder blue", relief = SUNKEN)
frame.pack(side = TOP)

lblinfo = Label(Tops, font = ("SHOWCARD GOTHIC", 50, 'bold'), text = "dojo python3")
lblinfo.grid(row = 0, column = 0)

def btnClick(numero):
    global operator
    operator = operator + str(numero)
    text_input.set(operator)

def btnEval(numero):
    global operator
    result = str(eval(operator))
    text_input.set(result)
    operator = ""

txtDisplay = Entry(frame, font = ("SHOWCARD GOTHIC", 50, 'bold'),
    textvariable = text_input, bg = "black")
txtDisplay.grid(columnspan = 4)

btn1 = Button(frame, font = ("SHOWCARD GOTHIC", 20, 'bold'),
    command = lambda:btnClick(1)).grid(row = 2, column = 0)
btn2 = Button(frame, font = ("SHOWCARD GOTHIC", 20, 'bold'),
    command = lambda:btnClick(2)).grid(row = 2, column = 1)
Addition = Button(frame, font = ("SHOWCARD GOTHIC", 20, 'bold'),
    command = lambda:btnClick("+")).grid(row = 2, column = 2)
Equals = Button(frame, padx = 16, pady = 8, bd = 8, fg= "black", font = ("SHOWCARD GOTHIC", 20, 'bold'),
    command = btnEval).grid(row = 2, column = 3)
root.mainloop()
