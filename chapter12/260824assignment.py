# (set을 쓰지 말고) list 기능만 써서 unique_tags를 구현하시오.

# =tags를 처음부터 하나씩 확인해서, 아직 나오지 않은 값만 unique_tags에 넣으세요.
# 단, set()은 사용하지 마세요.

# 핵심은 빈 리스트를 만들고, 기존 리스트를 하나씩 확인하는 것이야.

# 힌트:
# 결과를 저장할 빈 리스트를 만든다.
# for문으로 tags의 값을 하나씩 꺼낸다.
# 꺼낸 값이 결과 리스트에 없을 때만 추가한다.
# 리스트에 값이 있는지 확인할 때는 not in을 사용한다.
# 추가할 때는 append()를 사용한다.

tags = ["Python", "AI", "Python", "Data", "AI"]

unique_tags = []
for tag in tags:
    if tag not in unique_tags:
            unique_tags.append(tag)
print(unique_tags)

# 수도코드
# 태그 목록을 준비한다

# 중복을 제거한 값을 저장할 빈 목록을 만든다

# 태그 목록에서 태그를 하나씩 꺼낸다
#     만약 꺼낸 태그가 결과 목록에 없다면
#         해당 태그 하나를 결과 목록에 추가한다

# 결과 목록을 출력한다