# homeworklottoset.py

# 로또 1~45사이 숫자
# 로또 정수
# 반복문 for, while
# 난수발생 6개 숫자 중복 체크
# 난수발생 후 출력은 sort정렬

# 강사님 버전
import random

lotto = { }
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if (lotto.count(lotto[k]) >1):
            lotto.pop()
            lotto.append(random.radint(1,45))

print(lotto)
lotto.sort()
print(lotto)


''' 나중에 리스트대신 set 타입으로 변환 '''
myset = {7, 29, 45, 3, 36, 12}
print(myset)
