import tkinter as tk

class Pet:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return '...'
    

class Dog(Pet):
    def speak(self):
        return '멍멍'
    
class Cat(Pet):
    def speak(self):
        return '야옹'
    
class Person:
    def __init__(self,name,pet=None):
        self.name=name
        self.pet=pet

person=Person('홍길동')

root=tk.Tk()

root.title('문제 5')
root.geometry('700x300')

tk.Label(root,text='반려동물 등록하기',font=('bold',15)).pack(pady=10)

F=tk.Frame()
F.pack()

tk.Label(F,text='반려동물 이름:').grid(column=0,row=0)
Pname= tk.Entry(F)
Pname.grid(column=1,row=0)
pet_type=tk.StringVar(value='dog')

tk.Label(F,text='종류:').grid(column=0,row=1)
tk.Radiobutton(F,text='강아지',value='dog',variable=pet_type).grid(column=1,row=1,sticky='w',padx=5)
tk.Radiobutton(F,text='고양이',value='cat',variable=pet_type).grid(column=2,row=1,sticky='w',padx=5)

vac=tk.IntVar(value=0)
neu=tk.IntVar(value=0)

tk.Label(F,text='옵션:').grid(column=0,row=2)
tk.Checkbutton(F,text='예방접종 완료',variable=vac).grid(column=1,row=2,sticky='w',padx=5)
tk.Checkbutton(F,text='중성화 완료',variable=neu).grid(column=2,row=2,sticky='w',padx=5)

result=tk.Label(root,text='등록 정보를 확인하세요',fg='blue')
result.pack(pady=10)

def register():
    pet_name=Pname.get()
    kind=pet_type.get()
    if kind=='dog':
        pet= Dog(pet_name)
    else:
        pet = Cat(pet_name)

    person.pet = pet

    if vac.get():
        Vcomplete ='O'
    else:
        Vcomplete='X'

    if neu.get():
        Ncomplete ='O'
    else:
        Ncomplete='X'

    if kind =='dog':
        kind_kor='강아지'
    else:
        kind_kor='고양이'

    msg=f'{person.name}의 반려동물 등록 완료\n 이름 : {pet.name}({kind_kor})\n소리:{pet.speak()}\n예방접종:{Vcomplete},중성화{Ncomplete}'
    result.config(text=msg)

def clear():
    Pname.delete(0,tk.END)
    pet_type.set('dog')
    vac.set(0)
    neu.set(0)
    person.pet=None
    result.config(text='등록 정보를 확인하세요')

b_frame=tk.Frame()
b_frame.pack(padx=10)
tk.Button(b_frame,text='등록하기',command=register).pack(side='left',padx=10)
tk.Button(b_frame,text='초기화',command=clear).pack(side='left',padx=10)

root.mainloop() 