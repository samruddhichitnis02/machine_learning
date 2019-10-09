"""Write a Python program to get the number of occurrences of a specified element in an array.
"""
from array import *
a=array('i',[ ])
n=int(input('Enter the number of elements-'))
for i in range(n):
    x=int(input('Enter the elements-'))
    a.append(x)
print(a)
for i in range(len(a)):
    b=int(input('Enter the element you want to get the number of occurrences of -'))
    print(a.count(b))
    break