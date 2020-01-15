# dictionary -> {key:value[,key:value]} -> js : json 형식
# 같은 키를 사용한 경우 뒤에 있는 데이터로 덮어 쓰기가 된다
dic1 = {1:'a', 2:'b', 3:'c', 3: 'd'}
print(dic1, type(dic1))

# 학생 딕셔너리 생성
student = {"학번":1000, "이름": "홍길동", "학과":"파이썬학과"}
print(student, type(student))

# 학생의 이름 데이터 가져오기
print(student["이름"])
print(student.get("이름"))

# 모든 키를 출력해보자
keylist = list(student.keys())
print(keylist)

valuelist = student.values()
print(valuelist)

# 학생딕셔너리가 가지고 있는 모든 데이터 출력해 보기
for a in keylist:
    print(a, ":", student[a])


print(student.items())

studentlist = list(student.items())

print(studentlist)

studentlist.append(('연락처', '010-0000-0000'))
print(studentlist)

print(studentlist.pop())

print(studentlist)

# 딕셔너리의 데이터 추가
singer = {}

singer["이름"] = "트와이스"
singer["구성원수"] = 9
# 같은 키를 사용해서 데이터를 넣으면 수정이 된다
singer["구성원수"] = 10
singer["대표곡"] = "히든"
print(singer)

# singer 딕셔너리의 대표곡 항목을 삭제
del singer["대표곡"]
print(singer)