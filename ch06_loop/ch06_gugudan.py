# 구구단 처리를 하는 시작 단수와 마지막 단수를 입력 받아서
# 시작단수 부터 마지막 단수 사이의 모든 단수를 출력한다
# 단 한줄에

# range(시작, 끝+1, 증감)
for i in range(1,11,2):
    print(i)

num1 = int(input("시작구구단:"))
num2 = int(input("끝구구단:"))
for i in range(1,10):
    for e in range(num1,num2+1):
        print("%d X %d = %2d" % (e, i, i * e), end="  ")
    print()




