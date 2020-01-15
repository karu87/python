fruit = ['사과','배','딸기','포도']

fruit.append('귤')

print(fruit)

a = input("과일을 입력하세요")

if a in fruit:
    print(a, "가 있습니다")
else:
    print(a, "없어요")