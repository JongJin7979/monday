# 07exceptinput.py
# 문제1 dan입력 키보드 input(), 형변환
# 문제2 dan입력 범위 정수 1 이상 2~9사이 숫자만 입력
# 문제3 예외처리 try: ~ except: ~
# 1건 이상처리는 무조건 반복문

import time

dna = 0 #초기값
try:
    dan = int(input('원하는 단 입력>>> '))
    if dan < 2 or dan > 9 :
        print('숫자범위는 2~9 사이 숫자입니다\n다시 입력하세요')
    
    for k in range(1,10,1):
        print(f'{dan}*{k}={dan*k}')
        time.sleep(0.5)
except:
    pass


print()
time.sleep(0.5)
print('포인트 7점 획득')
print('포인트 5점이상이면 vip자격만족대상입니다')

print()



# 내풀이

import time

# 문제1: dan 입력 받기
while True:
    try:
        dan = int(input("구구단의 단수를 입력 >>>  "))
        
        # 문제2: 범위 체크
        if dan < 2 or dan > 9:
            print("잘못된 입력입니다. 2~9 사이의 정수를 입력하세요.")
            continue
        
        break  # 유효한 입력일 경우 루프 종료

    except ValueError:
        print("유효한 정수를 입력하세요.")

# 문제3: 입력된 dan에 대한 구구단 출력
for k in range(1, 10):
    print(f'{dan} * {k} = {dan * k}')
    time.sleep(0.5)

print()
time.sleep(0.5)
print('포인트 7점 획득')
print('포인트 5점 이상이면 VIP 자격 만족 대상입니다.')

print()