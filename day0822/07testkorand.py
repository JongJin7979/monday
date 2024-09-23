# 07testkor.py

#선언=declare
kor, eng , hap = 0,0,0 
avg = 0.0 
message ='안내문' 

#처리
kor = 65 
eng = 50
hap = kor + eng
avg = hap//2 

#if조건 and  평균 70점부터, 각과목 60점부터 합격
#if조건 or  평균 70점부터, 각과목 60점부터 합격
if  (avg>=70 or kor>=60 or eng>=60) :
    message = '축합격'
else :
    message = '재시험'


#07testand.py문서 데이터출력
print('국어 ', kor)
print('영어 ', eng)
print('합계 ', hap)
print('평균 ', avg)
print('결과 ', message)







