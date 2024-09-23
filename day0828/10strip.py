# 10strip.py

# 문자,문자열변경 replace(구변경대상,신)
# 문자,문자열 공백제거 strip


msg = '       it is a best python       '
x = 'aaa '
y = ' yyy'
print(x + msg + y) #공백유지하면서 연결
print(x + msg.lstrip() + y)  #msg 왼쪽공백제거 
print(x + msg.rstrip() + y)  #msg 오른쪽공백제거 
print(x + msg.strip() + y)   #strip()

print()