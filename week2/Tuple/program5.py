"""Write a Python program to find the repeated items of a tuple"""

x=('10','20','30','40','50','60','70','90','10','10','50','50','50','60')

for i in range(len(x)):
    if(x.count(x[i])>1):
        print(x[i],end=' ')