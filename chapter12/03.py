#tags = ["Python", "AI", "Python", "Data", "AI"]

#print(type(tags))
#print(type(len(tags)))

#unique_tags = set(tags)

#print(type(unique_tags))
#print(len(unique_tags))

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
