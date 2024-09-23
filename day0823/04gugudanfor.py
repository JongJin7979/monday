# 04gugudanfor.py

import time

dan = int(input('원하는 단입력>>> ')) # input('안내') 문자형으로 인식 -> int로 변경
for k in range(1,10,1) :
    # print(dan, '*', k, '=', (dan*k))
    print(dan, '*', k, '=', (dan*k))
    time.sleep(0.5) #초단위기술