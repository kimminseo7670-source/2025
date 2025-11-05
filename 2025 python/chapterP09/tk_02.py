
from tkinter import *


class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.borrowed = False

  def borrow(self):
    if not self.borrowed:
      self.borrowed = True
      return f"{self.title}이(가) 대출되었습니다."
    return f"{self.title}은(는) 이미 대출 중입니다."

  def return_book(self):
    if self.borrowed:
      self.borrowed = False
      return f"{self.title}이(가) 반납되었습니다."
    return f"{self.title}은(는) 대출되지 않은 상태입니다."

borrowed_books = []  

def update_borrowed_list():
  if borrowed_books:
    books_str = ", ".join([f"{b.title}({b.author})" for b in borrowed_books])
  else:
    books_str = "현재 대출 중인 도서가 없습니다."
  label_list.config(text=f"대출 현황: {books_str}")

def borrow_book():
  title = title_E.get().strip()
  author = author_E.get().strip()
  if not title or not author:
    label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
    return
  for b in borrowed_books:
    if b.title == title and b.author == author:
      label_result.config(text=f"{title}은(는) 이미 대출 중입니다.", fg="red")
      return
    
  book = Book(title, author)
  msg = book.borrow()  
  borrowed_books.append(book)
  label_result.config(text=msg, fg="blue")
  update_borrowed_list()

def return_book():
  title =title_E.get().strip()
  author = author_E.get().strip()
  if not title or not author:
    label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
    return

  for b in borrowed_books:
    if b.title == title and b.author == author:
      borrowed_books.remove(b)
      label_result.config(text=f"{title}이(가) 반납되었습니다.", fg="green")
      update_borrowed_list()
      return

  label_result.config(text=f"{title}은(는) 대출 목록에 없습니다.", fg="red")


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
label_list = Label(root, text="대출 현황: 현재 대출 중인 도서가 없습니다.", wraplength=400, justify="left")
label_list.pack(pady=10)

root.mainloop()