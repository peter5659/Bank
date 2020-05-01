class Account:
    def __init__(self,number,name,money):
        self.number=number
        self.name=name
        self.money=money
    def introduce(self):   
        print("계좌번호: ",self.number," / 이름:",self.name,"/ 잔액: ",self.money)
