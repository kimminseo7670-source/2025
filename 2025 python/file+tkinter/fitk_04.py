
import tkinter as tk

class Vehicle:
    def __init__(self,name):
        self.name=name

    def drive(self):
        return NotImplementedError
    

class Car(Vehicle):
    def drive(self):
        return f'승용차 {self.name}가 주행합니다'
    
class Truck(Vehicle):
    def drive(self):
        return f'트럭 {self.name}가 화물을 싣고 주행합니다'
    
def append_log(message):
    with open('drive_log.txt','a',encoding='utf-8') as file:
        file.write(message +'\n')

def clear_log_file():
    with open('drive_log.txt','w',encoding='utf-8') as file:
        pass


def drive_car():
    name=name_Entry.get().strip()
    if name =='':
        name = '이름 없음'
    
    car = Car(name)
    message = car.drive()
    append_log(message)
    result.config(text=message)

def drive_truck():
    name=name_Entry.get().strip()
    if name =='':
        name = '이름 없음'
    
    truck = Truck(name)
    message = truck.drive()
    append_log(message)
    result.config(text=message)

def clear_log():
    clear_log_file()
    result.config(text='로그 파일을 비웠습니다')


root=tk.Tk()

root.title('문제 4')
root.geometry('400x320')
tk.Label(root,text='차량 이름을 입력하세요').pack(pady=10)

name_Entry=tk.Entry(root)
name_Entry.pack(pady=10)

result=tk.Label(root,text='결과가 이곳에 표시됩니다')
result.pack(pady=10)


frame=tk.Frame()
frame.pack()
tk.Button(frame,text='자동차 주행',command=drive_car).pack(pady=10)
tk.Button(frame,text='트럭 주행',command=drive_truck).pack(pady=10)
tk.Button(frame,text='로그 비우기',command=clear_log).pack(pady=10)

root.mainloop()