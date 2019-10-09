"""Write a Python program to multiplies all the items in a list."""


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=int(input('Enter the elements-'))
    x.append(a)
print(x)
mul=1
for i in range(len(x)):
    mul=mul*x[i]
print('The multiplication of all the elements of the list is-',mul)