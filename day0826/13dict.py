# 13dict.py

mysite = dict()

mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['naver'] = 'www.naver.com'
mysite['google'] = 'www.google.org'

print(mysite['kakao'])
print(mysite.get('kakao'))
print()

# 에러 print(mysite['kako'])     #키값없으면 실행중 에러
print(mysite.get('kako')) #키값없으면 None
print()

#키값있어야  딕트이름[키값] 출력및수정,신규등록이 가능
mya = 'naver' in mysite 
myb = 'navr' in mysite 
print(mya) # True
print(myb) # False



#for반복문
# for key in mysite:
#     print(key, ':', mysite[key])