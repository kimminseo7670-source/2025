from tkinter import *

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f'{self.title}이(가) 대출되었습니다'
        else: 
            return f'{self.title}은(는) 이미 대출중입니다'

    def return_book(self):
        if self.borrowed:
            self.borrowed=False
            return f'{self.title}이(가) 반납되었습니다'

def borrow_book():
    title=title_E.get()
    author=author_E.get()

    if title =='' or author=='':
        label_result.config(text='제목과 저자를 모두 입력하세요',fg='red')
        return
    global book
    book = Book(title, author)
    msg=book.borrow()
    label_result.config(text=msg)

def return_book():
      try:
         msg = book.return_book()
         label_result.config(text=msg, fg="green")
      except NameError:
         label_result.config(text="먼저 도서를 대출하세요.", fg="red")



root=Tk()

root.geometry('300x200')
root.title('도서 대출 관리 프로그램')
Label(root,text='도서 대출 관리 시스템',font='bold').pack()
frame=Frame(root)
frame.pack()
title=Label(frame,text='제목:')
author=Label(frame,text='저자:')

title.grid(row=0,column=0)
author.grid(row=1,column=0)


title_E=Entry(frame)
author_E=Entry(frame)

title_E.grid(row=0,column=1)
author_E.grid(row=1,column=1)

label_result=Label(root,text='')

button_frame = Frame(root)
button_frame.pack(pady=10)  
Button(button_frame, text='대출', command=borrow_book, width=10).pack(side='left', padx=10)
Button(button_frame, text='반납', command=return_book, width=10).pack(side='left', padx=10)
label_result.pack()


root.mainloop()

