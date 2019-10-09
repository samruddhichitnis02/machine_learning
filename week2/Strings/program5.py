"""Write a Python function that takes a list of words and returns the length of the longest one."""



x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
max=len(x[0])
maxi=x[0]
for i in range(len(x)):
    if(max<len(x[i])):
        max=len(x[i])
        maxi=x[i]

print(max)
print(maxi)