#1~10까지 출려
'''
i=1
while i< 11:
    print(i)
    i += 1
'''
#1부터 숫자를 계속 더해서 더한 숫자가 100보다 커지면 빠져나가서 출력
'''
i=1
sum = 0
while True:
    sum += i
    i += 1
    if sum>100:

        break
print(sum)
'''

#1부터 10까지 출력 홀수만 출력
#1부터 시작하면서 2씩 증가 -> 1번째 방법
#짝수인 경우 출력하지 않고 반복처리를 계속 할 수 있도록 한다
e = 0
while e in range(0,10):
    e += 1
    if e%2 == 0:
        continue
    else:
        print(e)
'''
i=1
while i<11:
    #만약에 짝수면 출력하지 않는다.
    if i%2==0:
        i+=1
        continue
    print(i)
'''

i=1
while i < 11:
    print(i)
    i += 2
