import tk

def create_new_button():
    button = tk.Button(root, text='新按钮', command=lambda: print('新按钮被点击'))
    button.pack()

root = tk.Tk()
root.title('动态创建按钮')

original_button = tk.Button(root, text='创建新按钮', command=create_new_button)
original_button.pack()

root.mainloop()
import tkinter as tk

def create_new_button():
    button = tk.Button(root, text='新按钮', command=lambda: print('新按钮被点击'))
    button.pack()

root = tk.Tk()
root.title('动态创建按钮')

original_button = tk.Button(root, text='创建新按钮', command=create_new_button)
original_button.pack()

root.mainloop()
