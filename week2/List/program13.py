""" Write a Python program to append a list to the second list"""


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

for i in range(len(y)):
    x.append(y[i])

print(x)