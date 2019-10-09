"""Write a Python program to create an array of 5 integers and display the array items. Access individual element
through indexes. """


from array import *
a=array('i',[ ])
n=int(input('Enter the number of elements-'))
for i in range(n):
    x=int(input('Enter the elements-'))
    a.append(x)
print(a)
index=int(input('Enter the index no of which you want to access the element-'))
if(index<=n):
    print(a[index])
else:
    print('Invalid index number!')