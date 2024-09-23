# 04lotto.py



# 로또 1~45사이 숫자
# 로또 정수
# 반복문 for, while
# 난수발생 6개 숫자 중복 체크
# 난수발생 후 출력은 sort정렬
# set함수 이용하지 마세요

import random
lotto = []
while len(lotto) < 6:
    com = random.randint(1,45)
    if com not in lotto:
        lotto.append(com)

lotto.sort()

for number in lotto:
    print(number, end = '\t')


print()
print()


# 강사님 버전
lotto = []
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if (lotto.count(lotto[k]) >1):
            lotto.pop()
            lotto.append(random.radint(1,45))

print(lotto)
lotto.sort()
print(lotto)