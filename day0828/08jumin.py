# 08jumin.py

import datetime  #from  import 
import time

jumin = '971230-1835064' 

# 이미 파이썬지식 람다식
# 12시 15분  split()사용 [시:끝+1]
# 문제1 if제어 성별체크   1/3 남자  2/4여자 
# 문제2 생일 12월30일 생일 축하합니다
# 문제3 나이계산 2024-1997 = 27
# 문제4 나중에 공개 
print()
print()

jum1 = '971230'  #len() 6자릿수 체크
jum2 = '18350642' #len() 7자릿수 체크
# len1 = jum1.len() len(jum1) 수정해서 자릿수체크
# len2 = jum2.len() len(jum2) 수정해서 자릿수체크


'''
문자열을 주석처럼 사용 
dt = datetime.datetime.now() #정답
print(str(dt)[0:4])  #2024-2001 = 나이계산
mytime = time.localtime()
print(mytime.tm_year) #2024-2001 =  나이계산
'''
