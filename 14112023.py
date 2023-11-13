# COPY Method
cars =["Saab", "Volvo", "BMW"]
new_cars = list(cars)
more_cars=["Honda"]
# new_cars = list(cars)
new_cars = cars.copy()
print(new_cars)

# EXTEND Method
cars.extend(more_cars)  # more_carsの内容をcarsに追加します。(Add the contents of more_cars to CARS.)
print(cars)

# JOIN Method
even_more_cars = new_cars + more_cars
print(even_more_cars)

# String Slicing
print(cars[1:2])
newCars = cars[1:2]
print(newCars)

cars =["Saab", "Volvo", "BMW"]
print(cars[-3:-1])
print(cars[1:-1])

# print(cars[0:2]) のコードは、`cars` リストの最初の要素（インデックス0）から、
# インデックス2の要素の直前まで（つまりインデックス1まで）の要素を取得し、その結果をプリントする操作です。
print(cars[0:2])

# インデックス２番以外のものを表示
# elements, skipping two elements at a time.
print(cars[::2])

fruits = ["apple", "banana", "cherry", "orange"]

# スライスを使用して fruits のインデックス1（"banana"）からインデックス3の前までの範囲（"banana" と "cherry" を含む）
# を新しいリスト["blackcurrant", "watermelon"] に置き換えます。
fruits[1:3] = ["blackcurrant", "watermelon"]
print('fruits')
# ['apple', 'blackcurrant', 'watermelon', 'orange']が表示される。
print(fruits)

# ここで書かれたコードは実行されていませんが、もし実行されていたら、上記のリスト内のインデックス1からインデックス3の前まで
# （つまり "blackcurrant" と "watermelon"）を新しいリスト 
# ["blackcurrant", "watermelon", "cherry"] で置き換える操作になります。
# ただし、この変更は次の行で上書きされるため、結果には反映されません。最後の操作：fruits[1:3] = ["watermelon"]
# ここでは、上記リストのインデックス1からインデックス3の前までを要素 "watermelon" 一つだけを含む新しいリストで置き換えます。
# この場合、"blackcurrant" と "watermelon" が "watermelon" 1つに置き換わるため、最終的なリストは次のようになります： ["apple", "watermelon", "orange"]
fruits[1:3] = ["blackcurrant", "watermelon", "cherry"]
fruits[1:3] = ["watermelon"]
print(fruits)

nos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nos)
# index 1から３つずつ要素飛ばしで10,11,12を置き換えている。
nos[1::3] = [10, 11, 12]
print(nos)

# index 1から4つずつ要素飛ばしで10,11,12を置き換えている。
nos[1::4] = [10, 11, 12]
print(nos)

nums =[10,20,40,50,60,70,80,90]
nums[::2] =[1,1,1,1]
print(nums)

# del
# 要素0から始まり、３ずつ飛ばして要素削除
del nums[::3]
print(nums)

nums2 =[10,20,40,50,60,70,80,90]
# 1~7までの要素を2ずつ飛ばして削除する。
del nums2[1:7:2]
print(nums2)

'''
states = ["QLD", "NSW", "ACT", "VIC", "TAS", "SA", "WA", "NT"]
found = False
theState = input("Enter a state: ")
for i in states:
    if i == theState:
        found = True
        break  # ここに移動

if not found:
    print("Not a valid state")
else:
    print("Valid state entered")


states = ["QLD", "NSW", "ACT", "VIC", "TAS", "SA", "WA",
"NT"]
print("Enter a state of Australia:", end=" ")
theState = input()
num = states.count(theState)
# or isThere = theState in states
print(num)
if num == 0:
    print("Not a valid state")
else:
    print("Valid state entered")
'''

names = ["Fred", "Barney", "Wilma", "Betty"]
ages = [35, 34, 29, 30]
# 対応する要素をペアにする。（zip)
output = zip(names, ages)

#各行にして表示
for i in list(output):
    print(i)

# 一列で表示 
print(list(zip(names, ages)))