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
