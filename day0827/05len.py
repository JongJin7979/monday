# 05len.py

# jumin='980726-2451876'
# jumin1='980726'  앞번호 6자릿수
# jumin2='2451876' 뒷번호 7자릿수


jumin='9807262451876' 
jumin1='980726'   
jumin2='2451876' 
# 문제 총자릿수 jumin1 6자릿수   jumin2 7자릿수  = 13자릿수
# len()사용  변수로 받아서
frontlen = len(jumin1)
backlen = len(jumin2)

if (frontlen != 6) or (backlen != 7 ):
    print('다시 정확한 데이터를 입력하세요')
else:
    print('정확한 데이터 감사합니다') 

#딕트예제 - 함수에적용, 클래스에 적용, 파일처리
#딕트 추가,삭제,수정,전체출력,한건조회,갯수
#예외처리 적용  try: ~~ except: ~~~ 




