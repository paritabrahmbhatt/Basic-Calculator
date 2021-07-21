from tkinter import *
from tkinter import font

#Defining various functions
expression = ""
#Function 1: The user input using the buttons:
def pressb(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def pressequal():
    try:
        global expression
        answer = str(eval(expression))
        equation.set(answer)
        expression = ""

    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

#Basic Format 
root = Tk()
#r = Frame(root, bg = 'aquamarine' ).pack()
root.configure(background = 'aquamarine')
root.title('Calculator')
root.geometry('394x266')

#Creating the text Entry box
equation = StringVar()
expression_field = Entry(root, bg = 'White', bd = '4',font = ('calibre',15,'bold'), 
    textvariable= equation)
expression_field.grid(columnspan = 4,ipadx = '79')

#Adding Buttons
buttonFont = font.Font(family='Helvetica', size=15, weight='bold') #Setting the font for buttons

#Button which will be in row 1:
btn1 = Button(root, text = '1',bd = '4',command = lambda:pressb(1),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn1.grid(row = 1, column =0)

btn2 = Button(root, text = '2',bd = '4',command = lambda:pressb(2),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn2.grid(row = 1,column = 1)

btn3 = Button(root,text = '3',bd = '4',command = lambda:pressb(3),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn3.grid(row = 1,column = 2)

btndivisor = Button(root,text = '÷',bd = '4',command = lambda:pressb("/"),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btndivisor.grid(row=1,column=3)

#Buttons of row 2:
btn4 = Button(root,text = '4',bd = '4',command = lambda:pressb(4),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn4.grid(row=2,column= 0)

btn5 = Button(root,text = '5',bd = '4',command = lambda:pressb(5),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn5.grid(row = 2, column=1)

btn6 = Button(root,text = '6',bd = '4',command = lambda:pressb(6),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn6.grid(row=2,column=2)

btnmult = Button(root,text = 'x',bd = '4',command = lambda:pressb("*"),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btnmult.grid(row = 2,column = 3)

#Buttons in row 3:
btn7 = Button(root,text = '7',bd = '4',command = lambda:pressb(7),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn7.grid(row=3,column=0)
btn8 = Button(root,text = '8',bd = '4',command = lambda:pressb(8),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn8.grid(row=3,column=1)
btn9 = Button(root,text = '9',bd = '4',command = lambda:pressb(9),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn9.grid(row=3,column = 2)
btnminus = Button(root,text = '-',bd = '4',command = lambda:pressb("-"),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btnminus.grid(row=3,column=3)

#Buttons in row 4:
btn0 = Button(root,text = '0',bd = '4',command = lambda:pressb(0),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btn0.grid(row = 4,column=0)
btndot = Button(root,text = '.',bd = '4',command = lambda:pressb('.'),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btndot.grid(row = 4, column = 1)

btnequal = Button(root,text = '=',bd = '4',command = lambda:pressequal(),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btnequal.grid(row=4,column=2)

btnplus = Button(root,text = '+',bd = '4',command = lambda:pressb("+"),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btnplus.grid(row=4,column=3)

#Button in row 5:
btnclr = Button(root,text = 'C',bd = '4',command = lambda:clear(),
    background= 'rosybrown1',font = buttonFont,height = 1, width = '7')
btnclr.grid(row = 5,column=0)

root.mainloop()

