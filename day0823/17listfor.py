#17listfor.py

mylist= ['tea', 7]  
print(mylist)

mylist.append('파이썬')
print(mylist)

mylist.append(23)
print(mylist)

mylist.insert(1, 'blue')
print(mylist)
print('- ' * 50 )

# 수정할때 
mylist[0] = 'kakao'
mylist[2] = 94
print(mylist)

# blue삭제  del mylist[1], mylist.pop(위치)
#정답 mylist.pop(1) 권장
del mylist[1]
print(mylist)
print()

#에러 mylist.sort()
#주의사항 sort()적용은 같은타입만 가능 

for a in mylist:
    print(a, end=' ')
print()
print()


