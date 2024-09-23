# 02testlist.py

data = [ #4행 * ???열
        [71,72,73,74,70] ,
        [25,26,28] , 
        [39,10,11,12] ,
        [33,55]
    ]

for k in range(len(data)): # 4행  
    for b in range(len(data[k])): # 열갯수
        print(data[k][b] , end = '\t')
    print()

# 힌트 중첩for반복문 권장, while반복문 비권장 
# range(len()) 이용하면 편해 
# for a in range(0,3,1): #3행 *  열갯수 고정일 
#     for b in range(0,4,1):
#         print(data[a][b] , end = '\t')
#     print()

print()
print('- '  * 50)
# 1   2   3   4
# 5   6   7   8
# 9   10  11  12



