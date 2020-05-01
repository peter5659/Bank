
from Account import *

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
while(1):
    show_menu()
    menu=int(input())
    if(menu==1):
        
        print("======계좌개설======")
        account_number=str(input("계좌번호 :"))
        name=str(input("이름: "))
        first_money=int(input("예금: "))
        
        a=Account(account_number,name,first_money)
        account_objects.append(a)
        
        print("##계좌개설을 완료하였습니다##")

    # elif(menu==str(2)):
    # elif(menu==str(3)):
    elif(menu==4):
        for i in range(len(account_objects)):
            account_objects[i].introduce()
        
    elif(menu==5):
        print("##프로그램을 종료합니다##")
        break 
        
    else:
        print("잘못 입력하셨습니다")