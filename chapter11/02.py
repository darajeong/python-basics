fruits = ["사과", "바나나"]
more_fruits = ["포도", "딸기", "키위"]

print("원래 fruits의 과일 갯수: ", len(fruits))

fruits.extend(more_fruits)

print(fruits)

print("extend 원래 fruits의 과일 갯수: ", len(fruits))