tup1 =(20,)
print(tup1)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# タプルをリストに変換
thelist = list(thistuple)
# リストの要素を変更
thelist[1] = "Orange"
# リストをタプルに戻す
thistuple = tuple(thelist)
print(thistuple)


t = ("apple", "banana", "cherry", "apple", "cherry")
for i in t: 
    print(i)

    
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Count Method
new = (1,2,3,4,5,6,7,8,9,10,5)
x = new.count(5)
print(x)

# Index Method
index = (1,2,3,4,5,6,7,8,9,10,12,13,14,15,16)
x1= index.index(3)
print(x1)