import tkinter
import tkinter.messagebox
from tkinter.ttk import Button, Label


class LuckAward:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("学生成绩管理系统")
        self.root.minsize(720, 480)
        self.initGUi()
        self.root.mainloop()

    def initGUi(self):
        b1 = Button(self.root, text="增加学生")
        b1.pack(side="top", anchor="nw")


ym = LuckAward()