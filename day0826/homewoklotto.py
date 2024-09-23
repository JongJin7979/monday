# homewoklotto.py

import random 

# homewoklotto.py

import random 

# 로또 1~45사이 숫자
# 로또 정수 
# 반복문 for,while,if 
# 난수발생 6개 숫자 중복 체크 조별... 
# 난수발생후 출력은 sort정렬 
# set이용하지 마세요 
# 12시 30분까지
# while반복문안에서 다시 for반복문 
# 리스트이름[2]= 39

lotto = [] 
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if (lotto.count(lotto[k]) > 1) :
            lotto.pop() 
            lotto.append(random.randint(1,45))

print(lotto)
lotto.sort()
print(lotto)    

print()
print()

lotto = [] 
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if (lotto.count(lotto[k]) > 1) :
            lotto.pop() 
            lotto.append(random.randint(1,45))

print(lotto)
lotto.sort()
print(lotto)    

print()
print()