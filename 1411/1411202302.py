'''
new_dict = {}
print(new_dict)

myCar = {
    "brand": "BMW",
    "model": "Z3",
    "year": 2022,
    "electric": False
}

print(myCar)

dict = {"Gold": 1, "Bronze": 2, "Silver": 3,"Gold": 4 } 
print(dict)

myCar["noOfCylinders"] = 4
print(myCar)

for key in myCar:
    print(key)
print("***************************")
for values in myCar:
    print(myCar[values])
print("***************************")
for k in myCar.keys():
    print(k)
print("***************************")
for key, value in myCar.items():
    print(key, value)
print("***************************")
myCar.update({"brand" : "Holden"})
print(myCar)

person = {
"name" : "Agnes",
"suburb" : "Holmesglen"
}
person["mywork_place"] = person.pop("suburb")

print(person)


purse = {"money":10,"tissues":"Kleenex","candy":"pink"}
print(purse["candy"])
print(purse.get("money"))
print(purse.get("nothing"))

bike = {"brand": "Expensive", "name": "RX2"}
if "name" in bike:
    x = bike["name"]
else:
    x = 0
print(x)

# keyとvalueを追加
x = purse.setdefault("model", "Mustang")
print("******************************:")
print(x)
print(purse)
print("******************************:")
# 第二引数に何も入れなければ、初期値はそのまま
x = purse.setdefault("money")
print("******************************:")
print(x)
print(purse)
print("******************************:")
# popメソッドでkeyとvalueを削除します
purse.pop("money")
print(purse)
print("******************************:")
print("******************************:")
teacher = {"name": "Agnes", "age": "guess!"}
newTeacher = teacher.copy() # do NOT just assign (=)
newTeacher["age"] = 35
print("teacher")
print(teacher)
print("newTeacher")
print(newTeacher)

print('dictionary')
newTeacher = dict(teacher) # dictコンストラクターを使ってteacher辞書をコピー
print(newTeacher) # 新しいnewTeacher辞書を印刷

print("******************************:")
keys = [10, 20, 30]
values = ['Ten', 'Twenty', 'Thirty']
newDict = dict(zip(keys, values))
print(newDict)
print("******************************:")

myFamily = {
"p1" : { "name" : "Peter" , "starSign": "Gemini"},
"p2" : { "name" : "Agnes", "starSign": "Pisces"},
"p3" : { "name" : "Michael", "starSign": "Aries"}
}
print(myFamily)
print(myFamily["p2"])
print(myFamily["p2"]["name"])
'''

# fromkey
l =[1,2,3]
t = 5
# 第一引数でkey を指定、第二引数でvalueを指定している。
new_dict = dict.fromkeys(l,t)
print(new_dict)

print("************************************************************")
teachers = ['Agnes', 'Akrati']
defaults = {"jobTitle": 'Teacher', "salary": 80000}
res = dict.fromkeys(teachers, defaults)
print(res) # new dictionary
print(res["Agnes"]) # individual data
