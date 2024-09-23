# 01testif.py

'''
if 조건 :
    만족 문장기술 ok sucess
else:
    불만족 문장기술 failed
'''
#선언=declare
kor, eng, hap = 0,0,0 #변수초기화
message = '안내문' #변수초기화

kor = 90
eng = 85
hap = kor + eng
avg = hap/2

#문제해결1] 평균 70점부터 축합격, 0~69 재시험
if avg >= 70:
    message = '축합격'
else :
    message = '재시험'


#출력
print('국어', kor)
print('영어', eng)
print('합계', hap)
print('평균', avg)
print('결과', message)
print('❤️ ' *30)


#처리 연산, if, 반복



#출력