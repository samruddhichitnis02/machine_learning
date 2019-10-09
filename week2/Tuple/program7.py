"""Write a Python program to convert a list to a tuple"""


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)
print(tuple(x))