"""Write a Python program to count the number of strings where the string length is 2 or more and the first and last
character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""


x=[ ]
y=[ ]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)
count=0
for i in x:
    if(len(i)>1 and i[0]==i[-1]):
        count=count+1
print(count)


