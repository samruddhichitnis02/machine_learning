"""Write a Python program to get the difference between the two lists. """



x=[ ]
y=[ ]
z=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
m=int(input('Enter the number of elements-'))
for i in range(m):
    b=input('Enter the elements-')
    y.append(b)

for i in x:
    if i not in y:
        z.append(i)

for i in y:
   if i not in x:
       z.append(i)
       
print(z)