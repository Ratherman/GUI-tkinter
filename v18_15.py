from tkinter import *

def printInfo():
    print(f"Account: {e1.get()}\nPassoward: {e2.get()}")
    e1.delete(0, END)
    e2.delete(0, END)

window = Tk()
window.title("v18.19")

lab1 = Label(window, text="Account ").grid(row=0)
lab2 = Label(window, text="Password ").grid(row=1)

e1 = Entry(window)
e2 = Entry(window, show="*")
e1.insert(1, "Kevin")
e2.insert(1, "pwd")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = Button(window, text="Print", command=printInfo)
btn1.grid(row=2, column=0, sticky=W, pady=10)
btn2 = Button(window, text="Quit", command=window.quit)
btn2.grid(row=2, column=1, sticky=W, pady=10)

window.mainloop()