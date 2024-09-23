# 03lotto.py

lotto = [23,19,5,42,19,27,23,5,23]
myset = set(lotto) # filtering
print(myset)
lotto = list(myset)
lotto.sort() # 오름차순 a,b,c ~~~ 1,2,3~~~
print(lotto)
print()

mylength = len(lotto)
if mylength < 6 :
    print('항복 하나 추가하셔야 처리가능')
elif mylength > 6 :
    print('항목 데이터 초과입니다\n다시 확인하세요 ')
# 문제 lotto개수 6개 아니면 추가
# len() 전역함수



# 조건1 숫자 6개
# 조건2 중복 숫자 제거
# 조건3 정수 숫자로만 구성 문자x, 