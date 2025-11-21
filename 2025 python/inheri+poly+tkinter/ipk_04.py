import tkinter as tk

class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes=[]

    def enrollCourse(self,subject):
        if subject not in self.classes:
            self.classes.append(subject)


    def clearCourse(self):
        self.classes.clear()

stu = Student('홍길동')

root=tk.Tk()

root.title('문제 4')
root.geometry('380x280')
tk.Label(root,text=f'학생: {stu.name}').pack()

frame=tk.Frame()
frame.pack(padx=10,pady=10)

var_py=tk.IntVar(value=0)
var_ai=tk.IntVar(value=0)
var_ds=tk.IntVar(value=0)


tk.Checkbutton(frame,text='Python',variable=var_py).pack(side='left')
tk.Checkbutton(frame,text='Python',variable=var_ai).pack(side='left')
tk.Checkbutton(frame,text='Python',variable=var_ds).pack(side='left')

result = tk.Label(root,text='과목을 선택하고 [등록하기]를 누르세요.')
result.pack()

def register():
    if var_py.get():
        stu.enrollCourse('Python')

    if var_ai.get():
        stu.enrollCourse('AI')

    if var_ds.get():
        stu.enrollCourse('DataScience')

    if stu.classes:
        result.config(text=f'등록된 과목 : {stu.classes}')
    else:
        result.config(text='선택된 과목이 없습니다')

def reset():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    stu.classes.clear()
    result.config(text='모든 선택을 해제했습니다.')


frameB=tk.Frame()
frameB.pack(padx=10,pady=10)

tk.Button(frameB,text='등록하기',command=register).pack(side='left',padx=10)
tk.Button(frameB,text='초기화',command=reset).pack(side='left',padx=10)

root.mainloop()