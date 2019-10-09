"""Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given
list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""


x=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    tup=()
    l=list(tup)
    n1=int(input('Enter the number of elements to append it to tuple-'))
    for i in range(n1):
        a=int(input('Enter the elements-'))
        l.append(a)
    tup=tuple(l)
    x.append(tup)

def last(b):
    return b[-1]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        z=last(x[i])
        c=last(x[j])
        if(z>c):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)