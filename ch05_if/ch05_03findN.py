import random

# random으로 발생된 숫자 10개를 저장하는 리스트
numbers = []

# range(시작번호,끝번호+1)
for num in range(0,10):
    #print("a",num)
    # random.randrange(발생시작숫자, 발생끝숫자+1)
    numbers.append(random.randrange(0,10))


#print("생성된 리스트:", numbers)
#0-9 사이의 각각의 데이터가 있는지 확인해 보자
for num in range(0,10):
    if num in numbers:
        print("숫자 %d는 리스트에 있다" %num)
    if num not in numbers:
        print("숫자 %d는 리스트에 없다" %num)