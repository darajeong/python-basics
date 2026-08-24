fruits = ["사과", "바나나", "포도", "딸기"]

fruits.remove("바나나")

print(fruits)

removed = fruits.pop(1)

print(removed)

print(fruits)

del fruits[0]

print(fruits)


fruits = ["사과", "바나나", "사과", "포도"]
for i in range(len(fruits)):
    print(fruits[i])


#for fruit in fruits:
#    print(fruit)