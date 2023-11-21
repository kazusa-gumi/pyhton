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