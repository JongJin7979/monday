# 07comprehension.py [ 연산 if/else  for~~ ]

message=['ham', 'ham', 'spam', 'ham', 'spam', 'ham','spam']

# 문제1   for반복 ~ if제어
# spam출력 , 갯수출력 
for k in message:
    if k=='spam':
        print(k, end=' ')



print()
# 문제2 [ 만앞 if조건  else 불뒤 for~~~ ] comprehension처리
# 문제2 [ 만앞 for~~~ if 조건만족 ] comprehension처리
# 방법1 temp_list= [ k for k in message  if k=='spam' ]
temp_list= [ k for k in message  if 'spam' in k ]
print(temp_list)



print()
dummy = [ 1, 1, 0, 1, 0, 1, 0 ]
# 문제3 spam=0 ham=1 dummy = [0,1,0,1,0,0]
# message=['ham', 'ham', 'spam', 'ham', 'spam', 'ham','spam']
# for ~~ if~else








print()