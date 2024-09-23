# 04upper.py
# 교재 86~90페이지 참고 
msg = 'bstkpchERry'
print(msg.upper()) #대문자
print(msg.lower()) #소문자
print()
print('k =' , msg.find('k')) #k=3위치
print('t =' , msg.index('t')) #t=2위치
print()

msg = 'bstkpchERry'
pos = msg.find('z')
if pos == -1:
    pass
    print('원하는 키워드가 없습니다')
else:
    pass
    #있으면 출력을 하거나 조작,연산처리

# print('z =' , msg.find('z')) #z=-1위치
# 에러print('z =' , msg.index('z')) 



print('-' * 50)