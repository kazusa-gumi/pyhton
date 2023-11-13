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
# index 1から３つずつ要素飛ばしで10,11,12を代入している
nos[1::3] = [10, 11, 12]
print(nos)

# index 1から4つずつ要素飛ばしで10,11,12を代入している
nos[1::4] = [10, 11, 12]
print(nos)