"""Write a Python function that takes two lists and returns True if they have at least one common member."""


x=[ ]
y=[ ]
n=int(input('Enter the number of elements-'))
for  i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)
m=int(input('Enter the number of elements-'))
for i in range(m):
    b=input('Enter the elements-')
    y.append(b)

count=0
for i in range(len(x)):
    for j in range(len(y)):
        if(x[i]==y[j]):
            count=count+1
if(count>0):
    print(True)
else:
    print(False)