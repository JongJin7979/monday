# 06testround.py

# 변수 다중선언
a, b, ret = 7, 4, 0
mok = 34.5637
print(mok)
print('%f' %(mok)) # %f는 자릿수 지정안하면 6자릿수까지 출력
print('%.2f' %(mok)) # %f는 자릿수 지정
print(round(mok,2)) # 내장함수

# 내장함수
# print(), int(), type(), input('안내문'), str(), sum()
# round(데이터, 실수자릿수)

# %자리수d정수 %자리수f실수
# # print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
# print('%d*%d=%d' %(a,b,ret))

# 원하는 영역 블럭 선택후 'ctrl + /'
# 곱하기 연산처리
# ret = a*b
# # print(변수, '문자', ~~ ) -> 나열식
# print(a, '*', b, '=', ret)

# # print('{} * {} = {}'.format(a,b,ret) )
# print('{} * {} = {}'.format(a,b,ret))

# # print( f'{변수 및 값}' )
# print(f'{a} * {b} = {ret}')