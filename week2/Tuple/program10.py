""" Write a Python program to reverse a tuple."""


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
y=tuple(x)
print(y)
print('The reversed tuple is-',y[::-1])