"""Write a Python program to check whether an element exists within a tuple"""


x=('10','20','30','test','40','50','60','70','80','90')
n=input('Enter the element you want to search in the tuple-')
for i in range(len(x)):
    if n in x:
        print('Element found in tuple')
        break
    if n not in x:
        print('Element not found in tuple')
        break