# 01string.py

# str(), len()

x = 'blue'
y = 1234
print( x + str(y)) #blue1234
print(f'{x}{y}')   #blue1234
print(x,y)         #blue1234
print('- ' * 50)

msg = 'sakbtberteryulg'
print('총길이', len(msg))       #총길이 15
print('b갯수', msg.count('b'))   #b갯수 3

# kb글자단어를 추출 [시:끝+1]
my = msg[2:4]
print(my)       #kb추출
print(msg[2:4]) #kb추출


print()