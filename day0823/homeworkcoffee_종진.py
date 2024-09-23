# homeworkcoffee.py

money, sel = 0, 9

money = int(input('금액입력 >>> '))
while True:
    print('-----☕-----')
    data = input('1.커피(250) 2.코코아(200) 3.반환 9:종료 >>> ')
    sel = int(data)

    if sel == 9:
        print("종료합니다.")
        break
    elif sel == 3:
        print("잔액 반환:", money)
        money = 0  # 잔액을 반환 후 0으로 초기화
        continue

    if sel == 1:
        if money >= 250:
            money -= 250
            print('커피 주문 완료', "남은 잔액은", money, "입니다.")
        else:
            print('잔액이 부족합니다. 현재 잔액:', money)
    elif sel == 2:
        if money >= 200:
            money -= 200
            print('코코아 주문 완료', "남은 잔액은", money, "입니다.")
        else:
            print('잔액이 부족합니다. 현재 잔액:', money)
    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")
    
        

# homeworkcoffee.py

money = int(input('금액입력 >>> '))

while True:
    print('-----☕-----')
    sel = int(input('1.커피(250) 2.코코아(200) 3.반환 9:종료 >>> '))

    if sel == 9:
        print("종료합니다.")
        break
    elif sel == 3:
        print("잔액 반환:", money)
        money = 0
    elif sel == 1 and money >= 250:
        money -= 250
        print(f'커피 주문 완료. 남은 잔액은 {money}입니다.')
    elif sel == 2 and money >= 200:
        money -= 200
        print(f'코코아 주문 완료. 남은 잔액은 {money}입니다.')
    else:
        print("잔액이 부족하거나 잘못된 선택입니다. 현재 잔액:", money)



#if~elif~else제어문 커피값계산