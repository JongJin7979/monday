# 04delpop.py
import time

data = [7,8,9,10,3,5,2,4,1]
data.remove(9) # 9삭제
data.pop() # 2삭제
print(data)
time.sleep(0.5)

del data[2]
print(data)
time.sleep(0.5)

del data[1:5] # [시작:끝+1]
print(data)
time.sleep(0.5)

data = [7,8,9,10,3,5,2,4,1] # 문제 모든 데이터 전부 삭제
data.clear()
print(data)
time.sleep(0.5)

del data[:]
print(data) # 전체삭제 비권장
print('삭제연습 끝! dict 실습 k:v')

# count(90), len(리스트/딕트/문자열), 



# remove, del, pop, clear 제거삭제기능
# remove(데이터값)
# pop(위치)  pop()맨끝
# del 대상[위치]
# clear 전부 삭제


# 추가 append(), insert(위치, 값), add()
# 추가 딕트이름[k] = dataValue
# 덮어씌어짐 딕트이름[k] = dataValue