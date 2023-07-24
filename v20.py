from tkinter import *

def add():
    n3.set(n1.get()+n2.get())

window=Tk()
window.title("v20")

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window, width=8, textvariable=n1)
label = Label(window, width=3, text="+")
e2 = Entry(window, width=8, textvariable=n2)
btn = Button(window, width=5, text="=", command=add)
e3 = Entry(window, width=8, textvariable=n3)

e1.grid(row=0, column=0)
label.grid(row=0, column=1, padx=5)
e2.grid(row=0, column=2)
btn.grid(row=1, column=1, pady=5)
e3.grid(row=2, column=1)

window.mainloop()