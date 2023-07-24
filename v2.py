from tkinter import *

window = Tk()
window.title("MyWindow")
window.geometry("300x160")

window.mainloop()

# maxsize(width, height): 拖曳時可以設定視窗最大的寬與高
# resizeable(True, True): 是否更改視窗大小；若要固定視窗大小可以使用 resizeable(0, 0)