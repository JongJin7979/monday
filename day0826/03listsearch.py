# 03listsearch.py

data = [ 7,8,9,1,2 ]
ss = int(input('데이터찾기>>> '))
if ss in data:
    # print('결과 ', ss in data ) # True
    print('검색 성공 ok')
else:
    # print('결과 ', ss in data ) # False
    print('검색 실패 failed')


# 데이터있으면 성공메세지 데이터출력
# 데이터없으면 실패메세지 
# 참고for 대표변수 in range(5):
# list에서 데이터 찾기 할때 in키워드 사용 

print()