class Inventory:
    def __init__(self):
        self.__stock=0
        print('새 상품이 등록되었습니다.')


    def get_stock(self):
        return self.__stock


    
    def set_stock(self,amount):
        if amount >= 0:
            self.__stock += amount

  



itme1=Inventory()
itme1.set_stock(20)
print(itme1.get_stock())
        


