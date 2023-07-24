from tkinter import *

window = Tk()
window.title("v10")
lab1 = Label(window, text="Tag 1", relief="raised")
lab2 = Label(window, text="Tag 2", relief="raised")
lab3 = Label(window, text="Tag 3", relief="raised")
lab4 = Label(window, text="Tag 4", relief="raised")
lab5 = Label(window, text="Tag 5", relief="raised")
lab6 = Label(window, text="Tag 6", relief="raised")
lab7 = Label(window, text="Tag 7", relief="raised")
lab8 = Label(window, text="Tag 8", relief="raised")

lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1, rowspan=2)
lab3.grid(row=0, column=2)
lab4.grid(row=0, column=3)
lab5.grid(row=1, column=0)
#lab6.grid(row=1, column=1)
lab7.grid(row=1, column=2)
lab8.grid(row=1, column=3)

window.mainloop()