from tkinter import *

def bColor(bgColor):
    window.config(bg=bgColor)

window = Tk()
window.title("v13")
window.geometry("300x200")

# 依次建立 3 個 Button
exitbtn = Button(window, text="Exit", command=window.destroy)
bluebtn = Button(window, text="Blue", command=lambda:bColor("blue"))
yellowbtn = Button(window, text="Yellow", command=lambda:bColor("yellow"))

# 將 3 個鈕包裝定位在右下方
exitbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5) # anchor
bluebtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
yellowbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()