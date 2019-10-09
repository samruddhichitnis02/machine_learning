"""Write a Python program to remove the first occurrence of a specified element from an array."""

x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)
b=input('Enter the element to remove-')
for i in x:
    if(i==b):
        x.remove(i)
        break
    if(b not in x):
        print('Element not present in original array!')
        break
print(x)