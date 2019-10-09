"""Write a Python program to remove duplicates from a list.  """


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)

y=set(x)
x=list(y)
print(x)