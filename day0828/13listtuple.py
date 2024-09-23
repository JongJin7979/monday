# 13listtuply.py

#리스트list  순서유지 , 중복허용
#튜플tuple   순서유지 , 중복허용

mylist = [ 'kim', 78, True, 3.1415 , 78, 'kim' ]
mytuple = ( 'lee', 54, True, 3.1415, 54, 'lee')

mylist[1]=1200   #리스트 변경가능
mytuple[1]=1200  #튜플 변경X

print(mylist)
print(mytuple)



print()