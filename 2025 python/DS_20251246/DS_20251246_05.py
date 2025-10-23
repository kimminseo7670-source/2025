from tkinter import *
root=Tk()

root.title('중간고사 5번')
root.geometry('250x150')

Label(root,text='학번').grid(row=0,column=0)
nameE=Entry(root).grid(row=0,column=1)
Label(root,text='이름').grid(row=1,column=0)
idE=Entry(root).grid(row=1,column=1)

Button(root,text='로그인').grid(row=2,column=0)
Button(root,text='취소',command=root.quit).grid(row=2,column=1)


class Student:
    def __init__(self,stu_id,name):
        self.name=name
        self.stu_id=stu_id

    def __eq__(self, other):
        if isinstance(other,Student):
            return self.stu_id==other.stu_id
        

root.mainloop()