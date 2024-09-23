# homeworkstar.py
# 교재 100p 
# 조건 : *while 반복문 사용금지 / 중복 for 반복문 사용

# 처리 지역변수, 특정변수 필요없음
# 반복문 대표변수
# for a in range(1,11,1):
#     for b in range(1,11,1):
#         pass

'''
♥
♥  ♥
♥  ♥  ♥
♥  ♥  ♥  ♥
♥  ♥  ♥  ♥  ♥

♥  ♥  ♥  ♥  ♥
♥  ♥  ♥  ♥
♥  ♥  ♥
♥  ♥
♥
'''


for a in range(1, 6):
    print('♥  ' * a)

print()

for a in range(5, 0, -1):
    print('♥  ' * a)

print('=='*30)

for a in range(1, 6):
    print('  '.join(['♥'] * a))

print()

for a in range(5, 0, -1):
    print('  '.join(['♥'] * a))

print('=='*30)

for a in range(1,6):
    for b in range(a):
        print('♥',end='  ')
    print()

print()

for a in range(5,0,-1):
    for b in range(a):
        print('♥',end='  ')
    print()

print('=='*30)



    
     
    
   