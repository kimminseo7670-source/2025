from tkinter import *

root=Tk()
root.title('중간고사 7번')
root.geometry('420x440')
w=Canvas(root,width=400,height=320,bg='white')
w.pack()

frame=Frame(root,width=200,height=100)
frame.pack()
def rec():
    w.delete('all')
    w.create_rectangle(20,20,200,100,fill='red')


def cir():
    w.delete('all')
    w.create_oval(10,10,200,100,fill='blue')
    

def draw():
    global img
    w.delete('all')
    img=PhotoImage(file="d:/2025/DS_20251246/a.png")
    w.create_image(20, 20, anchor=NW, image=img)

def delete():
    w.delete('all')

Button(frame,text='사각형',command=rec).pack(side=LEFT)
Button(frame,text='원',command=cir).pack(side=LEFT)
Button(frame,text='그림',command=draw).pack(side=LEFT)
Button(frame,text='지우기',command=delete).pack(side=LEFT)
Label(root, text="버튼을 눌러 도형을 선택하세요").pack()

root.mainloop()
