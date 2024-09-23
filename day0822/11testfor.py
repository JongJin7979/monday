# 11testfor.py

# 변수선언안하고 for 대표변수 처리

for k in range(1, 61, 1) :
    print(k, end='\t') # print()함수 자동 라인개행포함 엔터기능<br>
    # 5개씩 6줄 출력이니까 if조건
    if k % 5 == 0: print()

    # 문제1 한 행에 5개의 데이터만 출력
    # 문제2 40까지만 출력

print()

for k in range(1, 61, 1) :
    print(k, end='\t') # print()함수 자동 라인개행포함 엔터기능<br>
    # 5개씩 6줄 출력이니까 if조건
    if k % 5 == 0: print()

    if k == 40:
        break


print()
'''
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
26  27  28  29  30
'''