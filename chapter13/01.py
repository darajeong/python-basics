#sentence = "나는 대한민국 서울 구로에서 파이썬 공부를 하고 있습니다." #단어 100개 이상
#words = sentence.split()

#print(type(words))
#print(words)

# sentence에서 3회 이상 등장하는 단어는 무엇일까요? 각 단어와 빈도수를 출력하시오.
# 1. 딕셔너리를 활용해 주세요. 지금까지 배우지 않은 기능 사용하지 말것.
# 2. 가장 간단한 방식으로 처리할 것. 

sentence = "사과 바나나 사과 포도 사과 바나나"

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

for word in word_count:
    if word_count[word] >= 3:
        print(word, word_count[word])
        print(f"3회 이상 등장하는 단어는 {word}이고, 빈도수는 {word_count[word]}입니다.")

# 문장을 공백을 기준으로 쪼개서 단어 리스트에 저장한다

# 빈 딕셔너리를 만든다

# 단어 리스트에서 단어를 하나씩 반복한다
#     만약 단어가 딕셔너리에 이미 있다면
#         해당 단어의 값을 1 증가시킨다
#     그렇지 않다면
#         해당 단어를 키로 저장하고 값을 1로 설정한다

# 딕셔너리에 있는 단어를 하나씩 반복한다
#     만약 해당 단어의 값이 3 이상이라면
#         단어와 값을 출력한다