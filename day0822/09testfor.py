# 08testfor.py

# 문자열, list, tuple, set, dict
# 반복데이터 사용

'''
for 변수대표k in range(10) :
    10회처리 0~4까지 10회처리

for 변수대표k in range(1,10) :
    9회처리 0~4까지 9회처리

for 변수대표k in range(1,10,1) :
    9회처리 0~4까지 9회처리
    1씩 증가일 때 3번째 1생략

while 조건 :
    조건 만족시 루프loop처리
    무한루프처리일 때 if제어문으로 break반복탈출
'''

# for, while 연습할 때 사용 a, b, hap, tot
a, b = 0,0
hap, tot = 0,0

# 첫번째 a, hap 1 ~ 5 출력 누적
'''
1 1
2 3
3 6
4 10
5 15
'''

a = a+1; hap = hap +a; print(a,hap)
a = a+1; hap = hap +a; print(a,hap)
a = a+1; hap = hap +a; print(a,hap)
a = a+1; hap = hap +a; print(a,hap)
a = a+1; hap = hap +a; print(a,hap)
print()


# 변수 재사용할 때 초기화
# for 반복문, 대입연산
a, hap = 0,0 #재선언보다는 초기화
for k in range(5) :
    a = a + 1
    hap = hap + a
    print(a, hap)



# for k in range(5) :
#     print(k, message)
    

