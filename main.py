from Account import *

#a=Account("123","jon",30000)
def show_menu():
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 종료하기")
    print("=====================")

while(1):
    show_menu()
    menu=int(input())
    if(menu==5):
        print("##프로그램을 종료합니다##")
        break;    