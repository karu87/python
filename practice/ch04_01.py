'''
pay = int(input("교환할돈은?"))

a = pay//500
b = (pay-a*500)//100
c = (pay-a*500-b*100)//50
d = (pay-a*500-b*100-c*50)//10
e = pay-a*500-b*100-c*50-d*10


print("500원짜리", a,"개")
print("100원짜리", b,"개")
print("50원짜리", c,"개")
print("10원짜리", d,"개")
print("나머지", e,"원")
'''

#calcu(바꿔야할돈, 지급된돈)
def calcu(a, pay):
    print("지급금액",pay)
    # 바꿔야할 돈의 갯수
    cnt = pay // a
    print(a,"갯수:",cnt)
    # 남아있는 돈 재계산
    pay = pay % a
    return pay


pay = int(input("교환할돈은?"))
ch_pay = 500
pay=calcu(ch_pay, pay)
ch_pay = 100
pay=calcu(ch_pay, pay)
ch_pay = 50
pay=calcu(ch_pay, pay)
ch_pay = 10
pay=calcu(ch_pay, pay)
print("최종잔액:", pay)