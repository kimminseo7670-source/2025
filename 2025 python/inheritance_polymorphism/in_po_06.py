from tkinter import *

class Animal:
    def speak():
        pass

class Dog(Animal):
    def speak():
        return '멍멍'
    

class Cat(Animal):
    def speak():
        return '야옹'
    
class Duck(Animal):
    def speak():
        return '꽥꽥'
    
def make_sound(animal):
    result.config(text=animal.speak())
      


    

root=Tk()

root.title('동물소리 듣기')
root.geometry('300x200')

Label(root,text='동물 버튼을 눌러 소리를 들어보세요.').pack(pady=15)
btf=Frame(root)
btf.pack(pady=4)
Button(btf,text='강아지',command=lambda:make_sound(Dog)).pack(side='left',padx=10)
Button(btf,text='고양이',command=lambda:make_sound(Cat)).pack(side='left',padx=10)
Button(btf,text='오리',command=lambda:make_sound(Duck)).pack(side='left',padx=10)

result=Label(root,text='(여기에 울음소리가 나옵니다)')
result.pack()
root.mainloop()