# 나만의 대화형 계산 프로그램
#과제A. 과제 주문 계산기
drink = input("음료 이름: ")
price = int(input("가격: "))
quantity = int(input("수량: "))

total = price * quantity
print(f"주문상품: {drink}")
print(f"총 금액 {total}원")

#과제B. 운동 시간 계산기
name = input("이름: ")
exercise_time = int(input("하루 운동 시간: "))
exercise_day = int(input("운동 일수: "))

total - exercise_time * exercise_day
print(f"{name}님의 총 운동 시간은 {total}시간입니다.")

#과제C. 여행 경비 계산기
place = input("여행지: ")
expected_cost = int(input("1일 예상 비용: "))
duration = int(input("여행일수: "))

total = expected_cost * duration
print(f"전체 예상 비용은 {total}원 입니다.")


#나만의 조건 판단 프로그램
#과제A. 연령 안내 프로그램
age = int(input("나이: "))

if age <= 7:
    print("미취학")
elif age <=13:
    print("초등학생 연령")
elif age <=16:
    print("중학생 연령")
elif age <=19:
    print("고등학생 연령")
else:
    print("성인")

#과제B. 쇼핑 할인 프로그램
product_price = int(input("상품 금액: "))

if product_price >= 100000:
    print("10% 할인 안내")
elif product_price >=50000:
    print("5% 할인 안내")
else:
    print("할인 없음")

#과제C. 간단한 로그인 판정
saved_id = "python"
saved_password = "1234"

user_id = input("아이디: ")
user_password = input("비밀번호: ")

login_success = user_id == saved_id and user_password == saved_password

if login_success:
    print("로그인 성공")
else:
    print("아이디 또는 비밀번호를 확인하세요.")