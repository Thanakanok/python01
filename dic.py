motorcycle={
    "model":"wave125",
    "brand":"Honda",
    "year":2012
}
profile={
    'name':"Thanakanok",
    'age':17
}
print(motorcycle["brand"])
print(profile["name"])
print(motorcycle)
#การเพิ่มคีย์ในdic
motorcycle['color'] = "blue"
print(motorcycle)
#การแก้ไขคำในdic
motorcycle['color']='red'
print(motorcycle)
motorcycle.pop('color')
print(motorcycle)
#การใช้list+dic
person=[{'name':'Tuu','age':18,'favor':'buffalo'},
        {'name':'pom','age':5,'favor':'aligator'},
        {'name':'justin','age':19,'favor':'pop music'}
        ]
print(person[0],['favor'])
#การใช้dicในdic
personDic={'Child':{'name':'Tuu','age':18,
'favor':'buffalo'},'child2':{'name':'pom','age':5,
'favor':'aligator'},'child3':{'name:'justin,
'age':19,'favor':'pop music'}}
print(personDic['child2']['favor'])
#Thanakanok Kitnukul M.6/11 No.38