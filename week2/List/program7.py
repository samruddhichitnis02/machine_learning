"""Write a Python program to clone or copy a list. """
#While cloning a list if you do x=y then it's wrong
#because both x and y refer to the same object and in cloning we have to create a clone that is different object but
#the second object should have value same to that of object 1


x=[]
y=[]
z=[]
n=int(input('Enter the number of elements-'))
for i in range(n):
    a=input('Enter the elements-')
    x.append(a)
print(x)
y=x[:]
print('The cloned list is-',y)
z=x
print(id(x))
print(id(y))
print(id(z))