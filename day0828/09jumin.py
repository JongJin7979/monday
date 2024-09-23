# 09jumin.py

import datetime  #from  import 
import time

jumin = '971230-2835064' 
# mylist  = list(jumin.split()) #비권장 

#문자열데이터 리스트화 
mylist  = list(jumin.split('-')) 
print(mylist)

gender = mylist[1][0]
print('성별표시확인', gender)

if (jumin.split('-')[1][0]==1) or  (jumin.split('-')[1][0]==3) :
    pass
    print('당신의 성별은 남자입니다')
elif (jumin.split('-')[1][0]==2) or  (jumin.split('-')[1][0]==4) :
    pass
    print('당신의 성별은 여자입니다')
else:
    print('성별표기 오류입니다\n다시 체크하세요')

print('😒 ' * 30)
print()

year = jumin.split('-')[0][:2]
# year = jumin.split('-')[0][0:2]
print('태어난 년도 ' , year)




print()
print()
