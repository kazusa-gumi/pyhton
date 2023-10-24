# while statements

'''
n = 5
while n > 0 :
    n = n-1
    print(n)
'''

'''
n = 4
while n > 0 :
    n = n-1
    print(n)
    print('Loop ended')


#Break Statement
n = 5
while n > 0:
    n = n-1
    if n == 2:
        break
    print(n)
    print("While Loop ended")

#Continue Statement
n = 6
while n > 0:
    n = n-1
    if n == 2:
        continue
    print(n)
    print("While Loop ended")


# run forever
while True:
    print('Hello')


# nested while
score =0
wicket=10
while score < 10:
    print('less than 10')
    score += 1 #score = score +1 
    while wicket >= 10:
        print('wicket')
        wicket += -1


# definite loops
# for loop
for x in [4,2,7,8,1]:
    print(x)
print('Definite loop')


for n in (0,1,2,3,4):
    print(n)

#range function
for n in range(5):
    print('Hello welcome to python')
print(n)


for x in range(10):
    print(x)

print('********************************')

for x in range(2,10):
    print(x)

print('********************************')

for x in range(2,10,2):
    print(x)
print('********************************')

for x in range(5):
    if(x == 2):
        #the loop is completed 2が来たら終わり
        break
    print(x)

print('********************************')

for x in range(5):
    if(x == 2):
        #２以外は続ける
        continue
    print(x)


x = 0
while x <=5:
    print(x)
    x+=1
else: 
    print('finished')


n=1
while n < 10:
    print(n,'\t', n**2)
    n +=1

'''

for i in range(1,11):
    for j in range(i):
        print(i, end =' ')
    print(' ')

