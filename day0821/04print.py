# 04testprint.py

# 변수 하나씩 선언, 다중 선언
a, b, ret = 7, 4, 0
msg = 1234

ret = a*b
print('|{}| * |{}| = |{}|'.format(a,b,ret))

print('|{}|'.format(msg))
print('|{:0>10,}|'.format(msg)) # '>' 오른쪽 맞춤의 뜻 / # 000001,234
print('|{:*>10,}|'.format(msg)) # *****1,234
print('|{:,}|'.format(msg)) # 1,234








'''
# print(변수, '문자', ~~ ) -> 나열식
print(a, '*', b, '=', ret)

# print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
print('%d*%d=%d' %(a,b,ret))

# print( f'{변수 및 값}' )
print(f'{a} * {b} = {ret}')
'''

