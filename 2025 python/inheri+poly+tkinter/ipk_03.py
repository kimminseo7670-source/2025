import tkinter as tk

import math


class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self,canvas):
        pass

class Rectangle(shape):
    def __init__(self, x, y,w,h):
        super().__init__(x, y)
        self.w=w
        self.h=h

    def area(self):
        return self.w * self.h
    
    def perimeter(self):
        return (self.w + self.h) *2
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.h,fill='tomato')
    
class Circle(shape):
    def __init__(self, x, y,r):
        super().__init__(x, y)
        self.r=r

    def area(self):
        return self.r**2*math.pi
    
    def perimeter(self):
        return 2*self.r*math.pi
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="skyblue")
        
    
    

root=tk.Tk()

root.title('문제 3')
canvas=tk.Canvas(root,width=300,height=220,bg='white')
canvas.pack()

reslut = tk.Label(text='도형을 선택하고 그리기를 누르세요')
reslut.pack()
frame=tk.Frame()
frame.pack(padx=10)

var=tk.StringVar(value='rect')

tk.Radiobutton(frame,text='사각형',value='rect',variable=var).pack(side='left')
tk.Radiobutton(frame,text='원',value='circ',variable=var).pack(side='left')



def drawing():
    canvas.delete('all')
    if var.get()=='rect':
        a = Rectangle(50, 50, 100, 60)
    else:
        a=Circle(150, 110, 40)
    a.draw(canvas)

    reslut.config(text=f'면적={a.area():.2f}, 둘레={a.perimeter():.2f}')

tk.Button(root,text='그리기',command=drawing).pack()



root.mainloop()