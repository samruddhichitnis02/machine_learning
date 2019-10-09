"""Write a Python program to create a tuple with different data types. """


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
y=tuple(x)
print(y)