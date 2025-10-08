from tkinter import *

root = Tk()
Label(root, text='Times 폰트와 빨강색을 사용한다',fg =  'red',font='Times 32 bold italic').pack()
Label(root, text='helvetica폰트와 파란색을 사용한다',fg =  'blue',bg='yellow',font='Helvetica 32 bold italic').pack()
root.mainloop()