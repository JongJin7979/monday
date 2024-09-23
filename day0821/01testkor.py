# 선언부분 = 변수데이터 초기화 = declare
# 변수 초기화 = 기본값 대입 = 할당
#변수이름명명 첫글자 소문자 시작 (첫글자 숫자 비건장, 특수문장 비권장)
#변수이름 명명 첫글자 소문자 my_kor, my_sum, my_avg, team_kor

title = '데이터점수'
name = '길동'

kor = 90
eng = 85
hap = 0 # hap, total, grandTotal  sum키워드 금지 sum() 내장함수있어서
avg = 0.0 # avg평균 myavg 권장

# 로직 = 연산처리
hap = (kor+eng)
avg = (kor+eng)/2

# 처리결과 출력 print('안내문', 데이터)
print('이름=', name)
print('국어=', kor)
print('영어=', eng)
print('총점=', hap)
print('평균=', avg)
print()
