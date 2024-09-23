# homeworkdict.py

score_dict = {
    '김자바':[100,60],
    '이합격':[90,77],
    'lee':[82,34],
    'park':[90,34],
}


# 아래처럼 출력
# 김자바 160 80
# 이합격 167 83
# lee 116 58
# park 124 62

for name, scores in score_dict.items():
    t = sum(scores)
    a = t//len(scores)
    print(f"{name}  {t}  {a}")

print()

for name, scores in score_dict.items():
    print(f"{name}  {sum(scores)}  {sum(scores)//len(scores)}")


# 강사님 버전
list_kor = []
list_eng = []
for data in score_dict.values():
    print(data[0], data[0])
    list_kor.append[data[0]]
    list_eng.append[data[0]]

hap_kor = sum(list_kor)
hap_eng = sum(list_eng)
print(hap_kor, hap_kor//2)
print(hap_eng, hap_eng//2)