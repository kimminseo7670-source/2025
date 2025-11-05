class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'{self.title}이(가) 대출되었습니다')
        else: 
            print(f'{self.title}은(는) 이미 대출중입니다')

    def return_book(self):
        if self.borrowed:
            self.borrowed=False
            print(f'{self.title}이(가) 반납되었습니다')



b1=Book('안녕하세요','김민서')
b1.borrow()    
b1.borrow()
b1.return_book()
