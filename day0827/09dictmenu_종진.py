# # 09dictmenu.py
# 예외처리 try: ~~~ except: ~~~ 생략

import time
import sys  # 프로그램 종료 sys.exit()




menu = dict()
flag = True
num, su, sel = 0,0,0
msg, info, message = '안내메', '안내메', '안내메'

while flag:
    print()
    try:
        num = int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 9.종료 >>> '))
    except ValueError:
        print('잘못된 입력입니다. 숫자를 입력하세요.')
        continue

    if num == 9:
        print('딕트 처리를 종료합니다.')
        flag = False
        sys.exit()
    elif num == 1:  # 딕트 등록
        name = input('이름 입력(key값) >>> ')
        price = input('가격 입력(value) >>> ')
        menu[name] = price
        print(name, '등록 성공했습니다.')
    elif num == 2:  # 딕트 전체 출력
        if not menu:
            print('등록된 항목이 없습니다.')
        else:
            for i, (k, v) in enumerate(menu.items()):
                print(f"{i + 1}. {k} : {v}")
    elif num == 3:  # 딕트 편집처리
        name = input('편집 대상 키값 입력 >>> ')
        if name not in menu:
            print('편집 대상 딕트에 해당하는 key가 없습니다.')
        else:
            price = input('새로운 가격 입력 >>> ')
            menu[name] = price
            print(name, '수정 성공했습니다.')
    elif num == 4:  # 딕트 삭제
        name = input('삭제할 키값 입력 >>> ')
        if name in menu:
            del menu[name]
            print(name, '삭제 성공했습니다.')
        else:
            print('삭제할 딕트에 해당하는 key가 없습니다.')
    elif num == 5:  # 딕트 조회
        name = input('조회할 키값 입력 >>> ')
        if name in menu:
            print(f"{name} : {menu[name]}")
        else:
            print('조회할 딕트에 해당하는 key가 없습니다.')
    else:
        print('처리 번호를 잘못 입력하셨네요\n')

print('딕트 CRUD 처리를 종료합니다.')

# # 사용자 정의 함수
# # 클래스
# # 파일처리 - 파일저장, 파일열기
# # 예외처리
# # crud
# # ㄴ c 추가 신규 등록create(insert=add)
# # ㄴ r read 읽기
# # ㄴ u update 수정
# # ㄴ d delete 삭제

# mysite = dict()
# mysite[100] = 'naver'
# mysite[200] = 'kakao'
# mysite[300] = 'apple'

# for i,k in enumerate(mysite):
#     print(i,k,' ', mysite[k])


# # 등록 100k: 네이버v / 200k: 카카오v
# # 출력 items(), enumerate(mysite)
# # 수정 100: 네이버 100: 에이콘
# mysite[100] = '에이콘'
# print()

# for k,v in mysite.items():
#     print(k," ", v)

# print()
# # print(mysite[210]) 에러발생
# print(mysite.get(210) ) # 에러대신 None 출력
# print( 210 in mysite) # 에러대신 False 출력




