"""Write a Python program to reverse the order of the items in the array. """

x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)
x.reverse()
print(x)