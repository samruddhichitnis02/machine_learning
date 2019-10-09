""" A bank teller serves customers standing in the queue one by one. Suppose that the service time XiXi for customer
ii has mean EXi=2 (minutes) and Var(Xi)=1. We assume that service times for different bank customers are independent.
Let YY be the total time the bank teller spends serving 50 customers. Write a program to find P(90<Y<110)
"""



import math
def Calculation(X):
    n=50 #number of samples
    EXi=2 #Mean Value
    Var=1 #Variance Value
    Sigma=math.sqrt(Var)
    Z = ((X - (n*EXi)) / (Sigma*math.sqrt(n)))  # Calculating the value of Z
    return Z

Z=round(Calculation(90),2)
print('The Value of Z is-',Z)

Z=round(Calculation(110),2)
print('The Value of Z is-',Z)

print('Hence P(90 < x < 110) = P(-1.41 < z < 1.41) = [area to the left of z = 1.41] - [area to the left of -1.41]=',round((0.9207-0.0793),4))
#Z<1.41 corresponds to Bigger area in the normal curve & -1.41<Z corresponds to Smaller area in the normal curve
#For  Z=-1.41 the corresponding area in the z table is 0.0793
#For Z=1.41 the corresponding area in the z table is 0.9207
#Bigger area i.e. 0.9207 - smaller area i.e= 0.0793