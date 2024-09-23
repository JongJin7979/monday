# 08Exception.py
# try: ~~ except Exception as ex: ~~ 

# 예외처리, 변수선언, if제어처리, 반복처리
x,y = 0, 0
hap, gob, mok, nmg = 0,0,0,0

x = int(input('x정수 입력(0숫자 제외) >>> '))
y = int(input('y정수 입력(0숫자 제외) >>> '))

# 예외처리  연산처리, if제어처리, 반복처리 
try:
    hap = x+y
    mok = x/y  #몫 처리 에러발생시  18라인으로 except영역 이동 
    gob = x*y
    nmg = x%y
    print(f'{x} + {y} = {hap}')
    print(f'{x} / {y} = {mok}')
    print(f'{x} % {y} = {nmg}')
    print(f'{x} * {y} = {gob}')
except Exception as ex:
    print('에러발생이유 ', ex)
    print('주의경고!!! 연산처리가 잘못 되었습니다')

print()
print('쇼핑목록')
print('주차처리')
print('정산처리')


