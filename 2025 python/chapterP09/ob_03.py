class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def disscount(self,rate):
        self.price= int((1-rate)*self.price)

    def get_info(self):
        print(f'상품명:{self.name}, 가격:{self.price}원')

p1=Product('운동화',3000)
p1.disscount(0.1)
p1.get_info()