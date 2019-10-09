"""Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
"""


x=[ ]
n=int(input('Enter the number of lists-'))
for i in range(n):
    y=[ ]
    m=int(input('Enter the number of elements-'))
    for i in range(m):
        a=int(input('Enter the elements-'))
        y.append(a)
    x.append(y)
print(x)

for i in range(len(x)):
    y=set(x[i])
    x[i]=list(y)
print(x)