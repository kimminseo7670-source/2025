from tkinter import *
root=Tk()

root.title('중간고사 4번')
root.geometry('400x400')
w=Canvas(root,bg='white')
choice=IntVar()
Radiobutton(root,text='사각형',padx=30,variable=choice,value=1).pack()
Radiobutton(root,text='원',padx=30,variable=choice,value=2).pack()
Radiobutton(root,text='텍스트',padx=30,variable=choice,value=3).pack()


root.mainloop()