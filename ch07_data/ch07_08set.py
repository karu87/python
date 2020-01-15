# set : 중복된 데이터 배제 {v,v,v,v,v,v,v,v,v....}

mySet1 = {1,2,3,3,3,4}
print(mySet1, type(mySet1))

# list -> set -> list
salesList = ['삼각김밥','바나나','도시락','삼각김밥','삼각김밥','도시락','삼각김밥']
print(salesList)
#set(salesList)
#print(set(salesList))

# 판매된 상품과 수량을 출력하시오. 중복이 되면 안된다
print("삼각김밥 : "+ str(salesList.count('삼각김밥')))
for i in set(salesList):
    print("%s 의 판매갯수 : %d " % (i, salesList.count(i)))

mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}

# 교집합, 합집합, 차집합, 대칭차집합
print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet1 ^ mySet2)

# 1~100까지 데이터로 list를 만들어 보세요
list1 = [1,2,3,4,5]
print("list1:",list1)
list2 = []

for i in range(1,5 + 1):
    list2.append(i)
print("list2:",list2)

# 컴프리헨션으로 리스트 만들기
list3 = [num for num in range(1,5+1)]
print("list3:", list3)

#3의 배수로 리스트 만들기
list4 = [num for num in range(1, 21) if num %3 ==0]
print("list4:", list4)

#1~5사이의 데이터를 제곱으로 구해서 리스트 만들기
list5 = [num*num for num in range(1,5+1)]
print("list5:", list5)

foods = ['떡복이', '짜장면', '라면', '피자']
sides = ['오뎅', '단무지', '김치']

#for food, side in zip(foods, sides):
#    print(food, '-->', side)

for i in range(len(foods)):
    if i <= len(sides)-1:
        print("%s --> %s" % (foods[i], sides[i]))
    # foods가 더 많은 경우  빠져나가기
    else:
        break

if len(foods) > len(sides):
    cnt = len(sides)
else:
    cnt = len(foods)

for i in range(cnt):
    print(foods[i], "-->", sides[i])

# zip 함수를 이용해서 튜플 리스트, 딕셔너리 만들기
tupList = list(zip(foods, sides))
#a= len(tupList)
#print(a)
print(tupList)

dic = dict(zip(foods, sides))
print(dic)