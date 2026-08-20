# 1. 상품 정보 저장
product_name = "파이썬 기초"
price = 28000
discount_rate = 0.15
is_on_sale = True
stock = 12

# 3. type()으로 검증
print(type(product_name))
print(type(price))
print(type(discount_rate))
print(type(is_on_sale))
print(type(stock))

# 4. 형 변환
price_text = str(price)
print(type(price_text))

# 5. 오류 실험
age = str("스무살")

# MISSION 01 - 구매 금액 계산 프로그램
price = 18000
quantity = 3
shipping_fee = 3000

product_total = price * quantity
final_total = product_total + shipping_fee
print("상품 금액:", product_total)
print("배송비:", shipping_fee)
print("최종 금액:", final_total)

# MISSION 02 - 시간을 시간과 분으로 바꾸기
total_minutes = 250
hours = total_minutes // 60
minutes = total_minutes % 60

print(hours, "시간")
print(minutes, "분")

# 과제 - 나의 생활 계산기 만들기
# 과제 A. 카페 주문 금액
coffee_price = 4500
coffee_quantity = 3
cake_price = 6500
cake_quantity = 2

total_price = coffee_price * coffee_quantity + cake_price * coffee_quantity

print ("총 금액:", total_price)

# 과제 B. 학습 시간 변환
total_minute = 385
hour = total_minutes // 60
minutes = total_minutes % 60

print (hour, "시간")
print (minutes, "분")

# 과제 C. 직사각형 계산
width = 12
height = 8

area = width * height

print("넓이:", area)

result = area > 100
print("넓이가 100보다 큰가?:", result)

width += 3

new_area = width * height
print("새로운 넓이:", new_area)
print("넓이가 100보다 큰가?:", result)