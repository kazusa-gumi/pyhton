#cars = []
#print(cars)

# 0 1 2
# -3 -2 -1 (negative index)
# you reference from the end, and it starts -1
cars = ['Saab', 'Volvo', 'BMW']
print(cars)

print(cars[2])
print(cars[-3])

fruits = ["apple", "banana", "peach", "oranges", "grapes"]
print(fruits)


# range(5) = [0,1,2,3,4]
# for i in range(len(fruits) ): # could use 5 instead
#     print(fruits[i])

# while loop
# i= 0
# # ini
# while i < len(fruits): # test
#     print(fruits[i])
# i += 1


# length method
fruits = ["apple", "banana", "peach", "oranges", "grapes"]
print(len(fruits))

# append method
fruits.append('apple')
print(fruits)

# insert method
fruits.insert(3, 'apple2')
print(fruits)