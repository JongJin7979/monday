# test.py

# day0829폴더\test.py
# 문제1 name, age, gender 변수 사용, 키보드 입력 input, 나이는 숫자
# 문제2 나이입력 범위 20~70 사이입력 그 이외 숫자 입력하면 재입력
    # 조건 20미만 청소년 1~19 20~30청년 31~65 중년 66년 이상 노년
# 문제3 남자/남/man 입력 True 출력 여자/여/woman 입력 False 출력
# 문제4 예외처리 try:
# 문제5 위의 문제1-4까지 함수화


# 문제 1: name, age, gender 변수 사용, 키보드 입력
def main_info():
    name = input("이름을 입력하세요: ")
    age = age_info()
    gender = gender_info()
    return name, age, gender

# 문제 2: 나이 입력 범위 체크
def age_info():
    while True:
        try:
            age = int(input("나이를 입력하세요 (1~70): "))
            if 1 <= age <= 70:
                return age
            else:
                print("1~70 사이의 나이를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

# 문제 3: 성별 입력
def gender_info():
    while True:
        gender_input = input("성별을 입력하세요 (남/여/man/woman): ").strip().lower()
        if gender_input in ['남자','남', 'man']:
            return True  # 남자
        elif gender_input in ['여자','여', 'woman']:
            return False  # 여자
        else:
            print("올바른 성별을 입력하세요.")

# 문제 2: 나이 범주화
def categorize_age_info(age):
    if age < 20:
        return "청소년"
    elif 20 <= age <= 30:
        return "청년"
    elif 31 <= age <= 65:
        return "중년"
    else:
        return "노년"

# 문제 4: 예외처리
def main():
    try:
        name, age, gender = main_info()
        age_category = categorize_age_info(age)
        gender_str = "남자" if gender else "여자"
        
        print(f"이름: {name}, 나이: {age}, 성별: {gender_str}, 나이 범주: {age_category}")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()



# 람다 함수

def main_info():
    name = input("이름을 입력하세요: ")
    age = (lambda: age_info())()
    gender = (lambda: gender_info())()
    return name, age, gender

def age_info():
    while True:
        try:
            age = int(input("나이를 입력하세요 (1~70): "))
            return age if 1 <= age <= 70 else print("1~70 사이의 나이를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

def gender_info():
    while True:
        gender_input = input("성별을 입력하세요 (남/여/man/woman): ").strip().lower()
        return True if gender_input in ['남자','남', 'man'] else (False if gender_input in ['여자','여', 'woman'] else print("올바른 성별을 입력하세요."))

categorize_age = lambda age: "청소년" if age < 20 else "청년" if age <= 30 else "중년" if age <= 65 else "노년"

def main():
    try:
        name, age, gender = main_info()
        age_category = categorize_age(age)
        gender_str = "남자" if gender else "여자"
        
        print(f"이름: {name}, 나이: {age}, 성별: {gender_str}, 나이 범주: {age_category}")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()