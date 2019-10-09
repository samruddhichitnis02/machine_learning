"""Write a Python program to find common items from two lists."""



x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)

y=[ ]
m=int(input('Enter the number of elements-'))
for i in range(m):
    b=input('Enter the elements-')
    y.append(b)
print(y)

for i in x:
    if i in y:
        print(i,end=' ')