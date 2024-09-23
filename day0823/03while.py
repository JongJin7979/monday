# 03while.py

su = 0 # 변수선언 declare + 값 초기화 0
while True :
    su = su + 1
    print(su)
    if su == 100 :
        break

print()
print('- '*50)

# 1 2 3 4 6 7 8 9 10

a = 0
while True :
    a = a + 1
    if a == 5 :
        continue
    print(a, end = ' ')
    if a == 10 :
        break