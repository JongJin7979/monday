# 08jumin.py

import datetime
import time

jumin = '970828-1835064'

# 12시 15분 split() 사용
# 문제1 성별체크 1/3 남자  2/4 여자
# 문제2 생일 12월30일 생일 축하합니다
# 문제3 나이계산 2024-1997 = 27


# 주민번호에서 생년월일과 성별 추출
b_info, g_info = jumin.split('-')
year_i = 1900 if g_info[0] in ['1', '2'] else 2000

year = year_i + int(b_info[:2])
month = int(b_info[2:4])
day = int(b_info[4:6])

# 생일 객체 생성
birthday = datetime.date(year, month, day)
today = datetime.date.today()

# 생일 축하 메시지
if today.month == month and today.day == day:
    print("생일 축하합니다!")
    time.sleep(0.5)
print()

# 성별 판별
gender = "남자" if g_info[0] in ['1', '3'] else "여자"
print(f"성별: {gender}")
time.sleep(0.5)
print()

# 나이 계산
age = today.year - year - ((today.month, today.day) < (month, day))
print(f"나이: {age}세")