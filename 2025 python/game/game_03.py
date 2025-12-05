#점수가 5씩 증가할 때마다 속도가 증가함
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) 

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, color): 
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) 
        self.paddle = paddle  
        self.canvas.move(self.id, 245, 100) 

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)      
        self.x = starts[0]       
        self.y = -3 
 
        self.canvas_height = self.canvas.winfo_height() 
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False  

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) 

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: 
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      
        print(self.canvas.coords(self.id))

        if pos[1] <= 0:
            self.y = abs(self.y)  #self.y=3처럼 초기 값을 넣어두면 점수 증가로 올린 속도가 초기값으로 바뀜
                                  #따라서 절댓값을 사용하여 속도 크기를 유지하도록 설정       
        if pos[3] >= self.canvas_height:  
            self.hit_bottom = True 

       
        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:
                self.y = -abs(self.y)

        if pos[0] <= 0: 
            self.x = abs(self.x)
        if pos[2] >= self.canvas_width: 
            self.x = -abs(self.x)

class Paddle: 
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0 
        self.canvas_width = self.canvas.winfo_width() 
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) 
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.speed=2

    def turn_left(self, evt):
        self.x = -self.speed 

    def turn_right(self, evt):
        self.x = self.speed

    def draw(self): 
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0




def start():
    
    btn.place_forget()
    

    canvas.delete('all')
    paddle = Paddle(canvas, 'blue') 
    ball = Ball(canvas, paddle, 'red')
    

    def loop(): 
      
      score=0
      score_txt =canvas.create_text(50,15,text=f'점수 : {score}',font=('bold',15))
      while True:
       pos=canvas.coords(ball.id)    
       if ball.hit_bottom == False:   
          ball.draw()
          paddle.draw()
       else:
          canvas.create_text(250,180,text='GAME OVER',font=('bold',25),fill='red')
          
          btn.place(x=250,y=200)
          break
       if ball.hit_paddle(pos) :
        score += 1
        canvas.itemconfig(score_txt,text=f'점수 : {score}')
        if score % 5==0:  #점수가 5씩 증가할 때마다 속도가 증가함
            if ball.x > 0:
             ball.x += 1
            else:
             ball.x -= 1
            if ball.y > 0:
             ball.y += 1
            else:
             ball.y -= 1

            paddle.speed +=1 #공만 빨라지면 게임의 진행이 어려우니 패들의 속도도 같이 늘려줌
    
    
       tk.update_idletasks() 
       tk.update() 
       time.sleep(0.01)
    loop()
btn=Button(tk,text='re',command=start)

start()

tk.mainloop()
