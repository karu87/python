# list는 데이터 변경이 가능[], tuple은 데이터 변경이 불가능()
tt = (10,20,30)

print(tt , type(tt))

print(tt[2])

print(tt[0:2])
#수정 불가
#tt[2] = 300
#tt.append(40)

tt1 = tt

print(tt1 + tt)

print(tt *3)

# tuple->(10,20,30) -> (10,200,30)
# tuple -> list -> 수정 -> tuple
list = list(tt)
#list[1] = 200
list[list.index(20)] = 200
#print(list)
tt = tuple(list)
print(tt)
