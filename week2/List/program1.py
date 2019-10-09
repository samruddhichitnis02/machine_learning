"""Write a Python program to sum all the items in a list"""
x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=int(input('Enter the elements-'))
    x.append(a)
print(x)
sum=0
for i in range(len(x)):
    sum=sum+x[i]
print('The sum of all the elements in the list is-',sum)