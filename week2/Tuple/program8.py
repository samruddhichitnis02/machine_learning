""" Write a Python program to remove an item from a tuple."""


x=(10,20,30,'test',40,50,60,70,80,90)
print('original tuple-',x)
n=3 #suppose we want to delete the object at position 3
x=x[:n]+x[n+1:]
print('Tuple after removing an element-',x)