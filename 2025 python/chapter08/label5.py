
from tkinter import *

root =Tk()
photo = PhotoImage(file='wl.gif')
w = Label(root,image=photo,justify='left').pack(side='right')
message = '''하이'''

w2=Label(root,padx=10,text=message).pack(side='left')
root.mainloop()


