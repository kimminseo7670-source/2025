class BankAccount:

    interset_rate=0.3

    def __init__(self,name,number,balance):
        self.name = name
        self.number=number
        self.balance= balance
    
    def deposit(self,amount):
        self.balance += amount
        print('입금 성공')
    


    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print('인출 성공')
        else:
            print('잔액이 부족합니다')

account= BankAccount('kim','123456789',1000)
print('초기잔고',account.balance)
account.deposit(500)
print('저축 후 잔고',account.balance)
account.withdraw(200)
print('인출 후 잔고',account.balance)
account.withdraw(1400)
