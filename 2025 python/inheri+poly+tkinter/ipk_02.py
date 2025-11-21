import tkinter as tk

class Pet:
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

def dog_choice():
    person.pet=Dog()
    result.config(text='강아지를 선택했습니다.',fg='blue')

def cat_choice():
    person.pet=Cat()
    result.config(text='고양이를 선택했습니다.',fg='blue')

def speaking():
    result.config(text=f'{person.name}의 반려동물 -> {person.pet.speak()}')


root=tk.Tk()

root.title('문제2')
root.geometry('400x200')

tk.Label(text='동물을 선택해주세요.').pack(pady=30)

frame=tk.Frame()
frame.pack(pady=10)
tk.Button(frame,text='강아지 선택',command=dog_choice).pack(side='left',padx=10)
tk.Button(frame,text='고양이 선택',command=cat_choice).pack(side='left',padx=10)
tk.Button(root,text='말하기',command=speaking).pack(pady=10)

result=tk.Label(text='')
result.pack()


root.mainloop()