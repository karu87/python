#print('\u2605')

#for문을 이용해서

a = '\u2605'

for i in range(1,10):
    if i < 6:
        for k in range(1, 6-i):
            print("  ", end="")
        for k in range(1, 2*i):
            print(a,end="")
        print()
    elif i > 5:
        for k in range(1, i-4):
            print("  ", end="")
        for k in range(0, (9-i)*2+1):
            print(a,end="")
        print()

