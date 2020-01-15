# 별개의 새로운 리스트를 만든다. 예전에 데이터를 그대로 사용
oldlist = ['짜장면']
newlist = oldlist

print("newlist : ", newlist)
print("oldlist : ", oldlist)

oldlist.append('탕수육')

print("oldlist : ", oldlist)
print("newlist : ", newlist)


newlist.append('군만두')

print("oldlist : ", oldlist)
print("newlist : ", newlist)

#별개로 동작 데이터 복사
newlist = oldlist[:]

oldlist.append('짬뽕')

print("oldlist : ", oldlist)
print("newlist : ", newlist)

newlist = oldlist.copy()

oldlist.append('울면')

print("oldlist : ", oldlist)
print("newlist : ", newlist)

newlist = []
for data in oldlist:
    newlist.append(data)

oldlist.remove('탕수육')

print("oldlist : ", oldlist)
print("newlist : ", newlist)






