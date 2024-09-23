# 06testkor.py

'''
if  조건 :   
  만족 문장기술 


if  조건 :   
  만족 문장기술 ok sucess
else:
  불만족 문장기술 failed
'''

#선언=declare
kor, eng , hap = 0,0,0 
avg = 0.0 
message ='안내문' 
grade = 'F'

#처리 연산,if,반복
kor = 90 
eng = 96
hap = kor + eng
avg = hap/2 

#문제해결1] 평균 70점부터 축합격, 0~69 재시험
if  avg >= 70 :
    message = '축합격'
else :
    message = '재시험'

#잘못된 처리
#평균 100~90 A, 89~80 B, 79~70 C, 69~60 D, 59~0 F
if avg >= 90 :
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

#출력 
print('국어 ', kor)
print('영어 ', eng)
print('합계 ', hap)
print('평균 ', avg)
print('학점 ', grade)
print('결과 ', message)
print( '🎄 ' *30)
print()





