from Account import *
class BankingSystem:
#a=Account("123","jon",30000) 이런식으로..
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
        menu=int(input())
        if(menu==1):
            
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
            
            name=str(input("이름: "))
            first_money=int(input("예금: "))
            
            a=Account(account_number,name,first_money)
            account_objects.append(a)
            confirm[account_number]=num
            num+=1
            
            print("##계좌개설을 완료하였습니다##")

        elif(menu==2):
            while(1):
                find=input("입금하실 계좌번호를 입력해주세요: ")
                if find in confirm:
                    break
                print("존재하지 않는 계좌번호입니다.")
                    
            for i in range(1):
                account_objects[confirm[find]].introduce()
            money_in=int(input("입금하실 금액을 입력해주세요: "))


            account_objects[confirm[find]].money+=money_in
            i=confirm[find]
            for i in range(1):
                account_objects[confirm[find]].introduce()

        elif(menu==3):
            while(1):
                find=input("출금하실 계좌번호를 입력해주세요: ")
                if find in confirm:
                    break
                print("존재하지 않는 계좌번호입니다.")
            for i in range(1):
                account_objects[confirm[find]].introduce()
            money_out=int(input("출금하실 금액을 입력해주세요: "))
            account_objects[confirm[find]].money-=money_out
            i=confirm[find]
            for i in range(1):
                account_objects[confirm[find]].introduce()

        elif(menu==4):
            for i in range(len(account_objects)):
                account_objects[i].introduce()
            
        elif(menu==5):
            print("##프로그램을 종료합니다##")
            break 
            
        else:
            print("잘못 입력하셨습니다")

BankingSystem.show_menu()