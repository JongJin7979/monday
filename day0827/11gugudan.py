# 11gugudan.py

# 내장함수
# list(), len(), tuple(), set()
# str(), int(), round(), print(), input()

# 리턴값x, 매개인자x  일반함수
def book():
    # 서점, 예약, 내용위주
    pass

def main():
    # 메인함수 진입시작
    pass

import time

def gugudan(dan):
    for k in range(1,10,1):
        print(f'{dan}*{k} = {k*dan}')
        time.sleep(0.5)


gugudan(21) #함수이름(21매개인자 = argument = parameter)
print('구구단 연습 4:35 4:37')
print()

def mysum(a,b):
    print(a,b, '합계 = ', (a+b))

mysum(17,26)
# 문제 mysume함수 호출



# 파이썬 함수 def 함수이름( ):
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값
# 함수는 호출 call