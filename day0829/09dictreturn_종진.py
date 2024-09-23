# 09dictreturn.py


# 함수의 리턴값 1개 이상처리
# 함수의 매개인자 1개 이상 처리(*args)

def score_procedure(score):
    kor_list = []
    eng_list = []
    
    # 점수를 리스트에 추가
    for student, scores in score.items():
        kor_list.append(scores[0])
        eng_list.append(scores[1])
    
    # 합계 및 평균 계산
    kor_sum = sum(kor_list)
    eng_sum = sum(eng_list)
    
    kor_average = kor_sum / len(kor_list) if kor_list else 0
    eng_average = eng_sum / len(eng_list) if eng_list else 0
    
    return kor_sum, eng_sum, kor_average, eng_average

score = {'kim': [100, 60], 'lee': [90, 77], 'goo': [82, 34]}
a, b, c, d = score_procedure(score)

print(f"국어 합계: {a}, 영어 합계: {b}, 국어 평균: {c}, 영어 평균: {d}")



#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
# 강사님 코드

def score_procedure(score):
    kor_list = []
    eng_list = []
    for data in score.values():
        kor_list.append(data[0])
        eng_list.append(data[1])

    kor_hap = sum(kor_list)
    eng_hap = sum(eng_list)
    kor_avg = kor_hap//len(kor_list)
    eng_avg = eng_hap//len(eng_list)
    return kor_hap,eng_hap,kor_avg,eng_avg

score = {'kim': [100, 60], 'lee': [90, 77], 'goo': [82, 34]}
a, b, c, d = score_procedure(score)