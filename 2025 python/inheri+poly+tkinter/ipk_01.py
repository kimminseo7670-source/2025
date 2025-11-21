import tkinter as tk

class Vehicle:
    def __init__(self,name):
        self.name= name
    
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f'승용차 {self.name}가 주행합니다'
    
class Truck(Vehicle):
    def drive(self):
        return f'트럭 {self.name}가 주행합니다'
    
car1= Car('car1')
truck1=Truck('truck1')
    
root= tk.Tk()
root.title('문제 1')

root.geometry('400x300')

tk.Label(root,text='버튼을 눌러보세요').pack(pady=10)

frame= tk.Frame()
frame.pack(pady=10)


def car():
    msg=car1.drive()
    result.config(text=msg)

def truck():
    msg=truck1.drive()
    result.config(text=msg)

tk.Button(frame,text='자동차 주행',command=car).pack(side='left')
tk.Button(frame,text='트럭 주행',command=truck).pack(side='left')

result=tk.Label(text='')
result.pack()

root.mainloop()