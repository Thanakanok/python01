#for จะเป็น definite Loop หรือ Loopที่มีการทำงานที่ชัดเจน
#forกับ
for i in range(1,11,1):
    print(i)
print('finish')
#for กับ list
list1 = ["apple","blueberry",'kiwi','papaya']
for element in list1:
    print(element)
#for กับ dic
dic1 ={'name':'thanakanok','age':17,'hobbies':'badminton'}
for key,value in dic1.items():
    print(key,value)
#while indefinite Loop หรือ Loopที่ทำงานไม่ชัดเจน
i =1
while i<10:
    print(i)
    i +=1
    #thanakanok kitnukul 6/11 เลขที่ 38