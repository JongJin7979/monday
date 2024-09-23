# 11gugudan.py
# 파이썬 함수 def 함수이름() :
import time

def gugudan(dan):
    print('저자는 ', name)
    for k in range(1,10,1):
        print(f'{dan}*{k} = {k*dan}')
        time.sleep(0.5)

mydata = 0
try:
    mydata = int(input('단입력>>>'))
except:
    print('정수 숫자를 입력하세요(1~9사이 숫자를 입력하세요)\n')


gugudan(21) #함수이름(21매개인자 = argument = parameter)
print()
