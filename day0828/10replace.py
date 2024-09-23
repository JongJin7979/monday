# 10replace.py

# 문자,문자열변경 replace(구변경대상,신)
# 문자,문자열 공백제거 strip

info = 'my best friend gildong'
myret1 = info.replace('best', 'coffee')
print(info)
print(myret1)
myret2 = info.replace(' ', '')
print(myret2)


print()
msg = '    it is a best python    '
x = 'aaa '
y = ' yyy'
print(x+msg+y) #공백유지하면서 연결
print(x+msg.lstrip()+y)  #msg 왼쪽공백제거 
print(x+msg.rstrip()+y)  #msg 오른쪽공백제거 

print()