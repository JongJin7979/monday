# 14defdict.py

# 첫번재 함수이름 test(매개인자)
# 두번째 test('code'=2400, 'title'='summer','grade'='A')
# 세번째 test함수에서 코드: 2400 제목: summer 총합: A
# 네번째 test함수에서 code: 2400 title: summer grade: A

# 파이썬 함수이름(*매개인자):
# 파이썬 함수이름(**매개인자):


# 위치 인자를 받는 함수
def test1(code, title, grade):
    print(f"코드: {code} 제목: {title} 총합: {grade}")

# 키워드 인자를 사용하여 호출
test1(code=2400, title='summer', grade='A')

# 가변 키워드 인자를 받는 함수
def test2(**kwargs):
    code = kwargs.get('code', '제공되지 않음')
    title = kwargs.get('title', '제공되지 않음')
    grade = kwargs.get('grade', '제공되지 않음')
    print(f"code: {code} title: {title} grade: {grade}")

# 가변 키워드 인자를 사용하여 호출
test2(code=2400, title='summer', grade='A')
