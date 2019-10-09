""" Write a Python program to get the smallest number from a list"""


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=int(input('Enter the elements-'))
    x.append(a)
print(x)
min=x[0]
for i in range(len(x)):
    if(x[i]<min):
        min=x[i]
print('the smallest number of the list is-',min)