

#        Python program to create a GUI Calculator with tkinter


from tkinter import *


expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)  # Transformation de la string en variable
                              # tkinter (StringVar) pour l'afficher apres
    
def clear():
    global expression
    expression = ""
    equation.set("")
    
    

def equalpress():
    try: 
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
        
    except:
        equation.set("erreur")
        expression = ""
    

if __name__ == "__main__":

    root = Tk()
    root.configure(background="light gray")
    root.title("Calculatrice")
    root.geometry("250x370")
    
    equation = StringVar()
    
    expression_field = Entry(root, width=100, font="Arial 20", background="light grey", textvariable=equation)
    expression_field.grid(columnspan=100, ipadx=50)
    
    equation.set("Entrer l'opération: ")

    
    button1 = Button(root, text='1', fg='black',font="Arial 15", bg='light blue', command=lambda: press(1), height=2, width=5)
    button1.grid(row=2, column=0)
    
    button2 = Button(root, text='2', fg='black',font="Arial 15", bg='light blue', command=lambda: press(2), height=2, width=5)
    button2.grid(row=2, column=1)
    
    button3 = Button(root, text='3', fg='black',font="Arial 15", bg='light blue', command=lambda: press(3), height=2, width=5)
    button3.grid(row=2, column=2)
    
    button4 = Button(root, text='4', fg='black',font="Arial 15", bg='light blue', command=lambda: press(4), height=2, width=5)
    button4.grid(row=3, column=0)
    
    button5 = Button(root, text='5', fg='black',font="Arial 15", bg='light blue', command=lambda: press(5),height=2, width=5)
    button5.grid(row=3, column=1)
    
    button6 = Button(root, text='6', fg='black', font="Arial 15",bg='light blue', command=lambda: press(6), height=2, width=5)
    button6.grid(row=3, column=2)
    
    button7 = Button(root, text='7', fg='black',font="Arial 15", bg='light blue', command=lambda: press(7), height=2, width=5)
    button7.grid(row=4, column=0)
    
    button8 = Button(root, text='8', fg='black',font="Arial 15", bg='light blue', command=lambda: press(8), height=2, width=5)
    button8.grid(row=4, column=1)
    
    button9 = Button(root, text='9', fg='black',font="Arial 15", bg='light blue', command=lambda: press(9), height=2, width=5)
    button9.grid(row=4, column=2)
    
    button0 = Button(root, text='0', fg='black',font="Arial 15", bg='light blue', command=lambda: press(0), height=2, width=5)
    button0.grid(row=5, column=0)
    
    multiply = Button(root, text='x', fg='black',font="Arial 15", bg='light blue', command=lambda: press("*"), height=2, width=5)
    multiply.grid(row=5, column=1)
    
    divide = Button(root, text='/', fg='black',font="Arial 15", bg='light blue', command=lambda: press("/"), height=2, width=5)
    divide.grid(row=5, column=2)
    
    addition = Button(root, text='+', fg='black',font="Arial 15", bg='light blue', command=lambda: press("+"), height=2, width=5)
    
    soustraction = Button(root, text='-', fg='black',font="Arial 15", bg='light blue', command=lambda: press("-"),height=2, width=5)
    soustraction.grid(row=6, column=1)
    
    equal = Button(root, text='=', fg='black',font="Arial 15", bg='light blue', command=equalpress, height=2, width=5)
    equal.grid(row=6, column=2)
    
    clear = Button(root, text='clear', fg='black',font="Arial 15", bg='light blue', command=clear, height=2, width=5)
    clear.grid(row=6, column=0)
    
  
    root.mainloop()
