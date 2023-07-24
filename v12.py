from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

window = Tk()
window.title("v12")
label = Label(window)
btn1 = Button(window, text="Message", width=15, command=msgShow)
btn2 = Button(window, text="Exit", width=15, command=window.destroy)

label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)

window.mainloop()