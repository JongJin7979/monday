#15list.py
import time

# list() 반복o, 순서o
mylist =['종진', 78, 3.124, True, 'F', 'young', 78]
print(mylist)
print()
time.sleep(0.5)

# set() 반복x, 순서x
myset = ['종진', 78, 23, '종진', 78, '종진'] 
print(myset)
print()
time.sleep(0.5)

# tuple(), 수정불가
mytuple = ['blue', 21, 'A']
print(mytuple)
print()
time.sleep(0.5)

#dict key valve 700:'구글'
mydict = {100:'naver', 200:'kakao'}
print(mydict)
print()
time.sleep(0.5)
