aa = [85,100,90,70,95,90]

# 1.리스트의 갯수를 출력
print(len(aa))
# 2. 리스트의 데이터를 바꾸지 않으면서 정렬해서 출력
print("%s"% sorted(aa))
# 3. 90 데이터의 위치를 출력
# aa.index(값[, 시작번호[, 끝번호]])
print("%d" % aa.index(90))
# 4. 마지막 데이터를 꺼내면서 제거해 보세요
print("%s" % aa.pop())
# 5. bb라는 리스트에 동일한 데이터를 가지도록 처리해 보세요
bb=aa.copy()
print(bb)
# 6. aa 리스트에서 값이 100인 데이터를 지운다
aa.remove(100)
print("%s" % aa)
# 7. aa 리스트 전체 내용을 지운다
print("%s" % aa.clear())