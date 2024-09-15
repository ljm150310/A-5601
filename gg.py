import tkinter as tk

def create_new_button():
    # 直接在函数内部创建并包装新的按钮
    button = tk.Button(root, text='新按钮', command=lambda: print('新按钮被点击'))
    button.pack()

root = tk.Tk()
root.title('动态创建按钮')

# 创建原始按钮，用于触发新按钮的创建
original_button = tk.Button(root, text='创建新按钮', command=create_new_button)
original_button.pack()

root.mainloop()
