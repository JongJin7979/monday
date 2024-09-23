# 08testdatetime.py

import time
import datetime

my = time.localtime()
print(my)
print(my.tm_year,'년')
print(my.tm_mon,'월')
print(my.tm_mday,'일')
print(my.tm_wday) # 0월요일 1화요일 2수요일 3목요일 4금요일 5토요일 6일요일
time.sleep(0.5)
print()

dt = datetime.datetime.now()
print(dt) # 2024-08-23 11:16:12.129932
print()

print('aaaaaaaa')
time.sleep(0.5)
print('bbbbbbbb')
time.sleep(0.5)
print('cccccccc')