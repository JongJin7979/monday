# 12sosi.py

import os
import pandas as pd
import cx_Oracle  
import oracledb     
import time

config = {
    'user': 'system',
    'password': '1234',
    'dsn': 'localhost:1521/xe'
}

conn = cx_Oracle.connect(**config) 
cursor = conn.cursor()

print("database version: ", conn.version)
print("oracle connect ok success")
print()

def sosiInsert():
    print('sosi테이블 신규등록 처리 ')
    
    dcode = int(input('코드 입력 >>> '))
    
    # 코드 중복 체크
    check_query = "SELECT COUNT(*) FROM sosi WHERE code = :1"
    cursor.execute(check_query, (dcode,))
    count = cursor.fetchone()[0]
    
    if count > 0:
        print("중복된 코드입니다. 다른 코드를 입력하세요.")
        return  # 함수 종료

    dname = input('이름 입력>> ')
    
    # 제목 입력 및 검증
    dtitle = input('제목 입력>> ')
    
    # 제목 길이 검증 (최대 16자)
    if len(dtitle) > 16:
        print("제목은 최대 16자까지 입력할 수 있습니다.")
        return  # 함수 종료

    # 급여 입력 및 검증
    dsal = int(input('급여 입력>> '))
    
    # 급여 검증 (예: 0 ~ 99999 범위)
    if dsal < 0 or dsal > 99999:
        print("급여는 0 이상 99999 이하의 값이어야 합니다.")
        return  # 함수 종료
    
    msg = "INSERT INTO sosi (code, name, title, sal, wdate, grade) VALUES (:1, :2, :3, :4, sysdate, 'C')"
    cursor.execute(msg, (dcode, dname, dtitle, dsal))
    conn.commit()
    
    print(dcode, ' 저장 성공했습니다')
    time.sleep(1)

def sosiSelectAll():
    msg = "SELECT * FROM sosi ORDER BY code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    print()
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' % ('코드', '이름', '제목', '급여', '날짜', '등급'))
    for r in rows:
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' % r) 
    print('전체데이터 갯수:', len(rows))
    print('- ' * 50)
    print()
    time.sleep(1)

def sosiSelectTitle():
    print('제목데이터 LIKE 조회하세요')
    
    # 제목 입력 받기
    dtitle = input('조회할 제목의 일부 입력 >>> ')
    
    # LIKE 쿼리 작성
    msg = "SELECT * FROM sosi WHERE title LIKE :1 ORDER BY code"
    
    # 쿼리 실행
    cursor.execute(msg, ('%' + dtitle + '%',))
    rows = cursor.fetchall()

    print()
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' % ('코드', '이름', '제목', '급여', '날짜', '등급'))
    
    # 결과 출력
    for r in rows:
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' % r)
    
    print('조회된 데이터 갯수:', len(rows))
    print('- ' * 50)
    print()
    time.sleep(1)

def sosiDelete():
    print('삭제할 레코드의 코드를 입력하세요.')

    # 삭제할 코드 입력 받기
    dcode = int(input('코드 입력 >>> '))

    # 코드 존재 여부 확인
    check_query = "SELECT COUNT(*) FROM sosi WHERE code = :1"
    cursor.execute(check_query, (dcode,))
    count = cursor.fetchone()[0]

    if count == 0:
        print("존재하지 않는 코드입니다.")
        return  # 함수 종료

    # 삭제 쿼리 실행
    delete_query = "DELETE FROM sosi WHERE code = :1"
    cursor.execute(delete_query, (dcode,))
    conn.commit()

    print(dcode, '번 코드가 삭제되었습니다.')
    time.sleep(1)

def manage_sosi():
    sosiSelectAll()      # 전체 조회
    sosiInsert()         # 신규 등록
    time.sleep(0.5)
    sosiSelectAll()      # 등록 후 전체 조회
    time.sleep(0.5)
    sosiSelectTitle()    # 제목 조회
    time.sleep(0.5)
    sosiDelete()         # 삭제
    time.sleep(0.5)
    sosiSelectAll()      # 삭제 후 전체 조회

# 실행
manage_sosi()

# 연결 종료
cursor.close()
conn.close()