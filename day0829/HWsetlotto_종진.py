# HWsetlotto.py

# 추천 lotto = set() set항목함수 lotto.add()
# 금지 lotto = lsit() 리스트 추가 append ()
# 난수 로또 숫자 발생, 중복 체크, set 추가
# set 데이터 타입을 list로 변환
# 출력은 오름차순 적용 sort()
    # while ~ while ~ if ~ else
    # while ~ for ~ if ~ else
    # while ~ if ~ else


import random

def mysetlotto():
    print('로또 번호 추천 프로그램 시작!')

    # 추천 로또 번호 저장 set
    lotto = set()

    # 로또 번호 생성
    while len(lotto) < 6:
        number = random.randint(1,45)
        # 중복 체크 후 번호 추가
        if number not in lotto:
            lotto.add(number)

    # set을 list로 변환 후 정렬
    sorted_lotto = sorted(list(lotto))
    
    print("추천 로또 번호: ", sorted_lotto)

mysetlotto()