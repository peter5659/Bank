

from Account import *

class System(Account):
    
    def deposit(self):   
        self.introduce()
        while(1):
            money_in=input("입금하실 금액을 입력해주세요: ")
            if money_in=="":
                print("입력하세요")
                continue
            k=0
            for i in range(len(money_in)):
                if str(0) <= money_in[i] and money_in[i]<=str(9):
                    k+=1
            
                else:
                    print("다시 입력해주세요")
                    break
            if k==len(money_in):
                money_in=int(money_in)
                break

        self.money+=money_in
        self.introduce()
    
    def withdraw(self):

        self.introduce()
        while(1):
            money_out=input("출금하실 금액을 입력해주세요: ")
            if money_out=="":
                print("입력하세요")
                continue
            k=0
            for i in range(len(money_out)):
                if str(0) <= money_out[i] and money_out[i]<=str(9):
                    k+=1
                
                else:
                    print("다시 입력해주세요")
                    break
            if k==len(money_out):
                money_out=int(money_out)
                break
        if money_out>self.money:
            print("돈이 부족합니다")
        else:
            self.money-=money_out
        self.introduce()
    
class BankingSystem:
    def show_menu():
        print("======Bank Menu======")
        print("1. 계좌개설")
        print("2. 입금하기")
        print("3. 출금하기")
        print("4. 전체조회")
        print("5. 종료하기")
        print("=====================")

    account_objects=[]
    confirm={}
    num=int(0)
    while(1):
        show_menu()
        menu=(input())
        if(menu==str(1)):
            
            print("======계좌개설======")
            while(1):
                account_number=str(input("계좌번호 :"))
                k=0
                for j in range(num):
                    if account_number in confirm:
                        print("이미 존재하는 계좌번호입니다. 다시 설정해주세요")
                        k=1
                        break
                if k==0:
                    break            
            while(1):
                name=str(input("이름: "))
                k=0
                if name=="":
                    print("입력하세요")
                    k=1
                    
                if k==0:
                    break

            while(1):
                first_money=input("예금: ")
                k=0
                if first_money=="":
                    print("입력하세요")
                    continue
                for i in range(len(first_money)):
                    if str(0) <= first_money[i] and first_money[i]<=str(9):
                        k+=1
                    else:
                        print("다시 입력해주세요")
                        break
                if k==len(first_money):
                    first_money=int(first_money)
                    break
            
            a=System(account_number,name,first_money)
            account_objects.append(a)
            confirm[account_number]=num
            num+=1
            
            print("##계좌개설을 완료하였습니다##")

        elif(menu==str(2)):
            while(1):
                find=input("입금하실 계좌번호를 입력해주세요: ")
                if find in confirm:
                    break
                print("존재하지 않는 계좌번호입니다.")
            account_objects[confirm[find]].deposit()


        elif(menu==str(3)):
            while(1):
                find=input("출금하실 계좌번호를 입력해주세요: ")
                if find in confirm:
                    break
                print("존재하지 않는 계좌번호입니다.")
            account_objects[confirm[find]].withdraw()


        elif(menu==str(4)):
            for i in range(len(account_objects)):
                account_objects[i].introduce()
            
        elif(menu==str(5)):
            print("##프로그램을 종료합니다##")
            break 
            
        else:
            print("잘못 입력하셨습니다")

            

