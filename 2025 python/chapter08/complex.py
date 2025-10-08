from tkinter import *

root=Tk()
f= Frame(root)


root.geometry('300x100')

button1=Button(root,text='버튼1',bg='red',fg='white')


button2=Button(root,text='버튼2',bg='green',fg='white')


button3=Button(root,text='버튼3',bg='blue',fg='white')


button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

l = Label(root,text='이 레이블은 버틈 뉘네 배치된다.')
l.pack()
f.pack()

root.mainloop()