# test03def.py


# 본인데이터 
#  ㄴ이름,나이, 
#  ㄴ성별,주소
#  ㄴ포인터점수 7.8 실수 

# 컴퓨터언어는 대소문자구별,  문장마지막 종료 ;
# 컴퓨터언어는 타입 숫자, 문자, 문자열, 불
# 파이썬언어는 대소문자구별 

# 파이썬 변수,연산, 처리 화면모니터출력 print()
# 파이썬 타입지정X
# 파이썬 문장마지막 ; 생략
# 파이썬 명령어 짧아요 = 축약 
# 파이썬 모니터출력 print() 자동라인개행=엔터기능
# 파이썬 모니터출력 print('안내메세지', 값)

# 문제1 본인정보 최소 3가지 출력 이름,나이
# 확장해서 공부할때 고정데이터를 키보드입력 input('안내문')
# 고길동 데이터입력 문자열인식 변수 = input('안내문') 
# 입력한 이름데이터 출력 

# 문제2 나이입력후 
# if조건  20~70입력 20~30청년  31~64중년 65세이상 노년


# 문제3 본인정보  출력 이름,나이 5회이상 
# 1회이상 반복문 - for,while
# 1회이상 반복, 몇회인지 모를때  함수구현후 호출 
# 숙제 
def myinfo():
    print('myinfo함수')
    msg = '나이정보'
    nick =input('이름입력>>> ')
    age = int(input('나이입력(20~70)>>> '))

    if age < 20 :
        print('청소년및 초등 유아입니다 - 대상아닙니다')
    elif age >= 20 and age <= 30:
        msg = '청년'
    elif age > 30 and age < 65:
        msg = '중년'
    elif age > 65 :
        msg = '노년'

    print('사용자', nick)
    print(age, msg)
    print(78.9) #키보드에서 입력해서 연산처리할때 형변환float()



myinfo() 
#myinfo() 
#myinfo() 



print() 
print()
'''
다른언어 java,C#, C, VB, PowerBuilder
char[] name = '길'
String nick = "길동"

int age = 24 
float point = 7.8

bool gender = true
'''

