f = open('hello.txt', 'a')
f.write("\nLine Three")
f.write("\nLine Four")
f.write("\nLine Five")
f.close()

# read method
f = open("text.txt", "r")
for line in f:
 print(line)
f.close()       

f = open("hello.txt", "r")
for line in f:
 print(line)
f.close()    

# with statement
# 最初の10文字を読む
with open ('hello.txt', 'r') as f:
    data=f.read(10)
    print(data)

# 1文字ずつprintします。
for line in data:
  words = line.split()
  print(words)