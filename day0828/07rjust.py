# 07rjust.py

for x in range(1,6,1):
    pass
    # print(f'{x} * {x} = {x*x}')
    print(x,'*', x,'=',(x*x))


print()
for x in range(1,6,1):
    print(x,'*', x,'=',str(x*x).rjust(3))


print()
for x in range(1,6,1):
    print(x,'*', x,'=',str(x*x).zfill(5))






print()