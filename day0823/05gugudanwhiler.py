# 05gugudanwhile.py

import time

dan = int(input('원하는 단입력>>> '))
# print(f'{dan}*{k}={dan*k}')

k = 1
while True :
    print(f'{dan}*{k}={dan*k}')
    k = k + 1
    time.sleep(0.5)
    if k == 10:
        break


print()