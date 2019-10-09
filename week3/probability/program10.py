"""X is a normally normally distributed variable with mean μ = 30 and standard deviation σ = 4. Write a program to find
a. P(x < 40)
b. P(x > 21)
c. P(30 < x < 35)"""



def calculation_of_Z(X):
    Mu=30 #Mean Value
    Sigma=4 #Standard Deviation Value
    Z = ((X - Mu) / Sigma)  # Calculating the value of Z
    return Z



Z=calculation_of_Z(40)
print('The Value of Z is-',Z)
print('P(X<40)=P(Z<2.5)= area to the left of 2.5=',0.9938) #The value 0.9938 is calculated from the negative Z table with area to the left


Z=calculation_of_Z(21)
print('The Value of Z is-',Z)
print('P(X>40)=P(Z>-2.25)= 1-area to the left of -2.25=',(1-0.0122))
#if we check for -2.25 in negative Z table
#It will give us the area to the left of -2.25 and since Z>-2.25 we want area to its right
#hence we subtract the total area that is 1 -area to the left of -2.25 i.e 0.0122 =0.9878

#For P(30<X<35)
Z=calculation_of_Z(30)
print('The Value of Z is-',Z)


Z=calculation_of_Z(35)
print('The Value of Z is-',Z)
print('Hence P(30 < x < 35) = P(0 < z < 1.25) = [area to the left of z = 1.25] - [area to the left of 0]=',(0.8944-0.5))
#Z<1.25 corresponds to Bigger area in the normal curve & 0<Z corresponds to Smaller area in the normal curve
#For  Z=0 the corresponding area in the z table is 0.5
#For Z=1.25 the corresponding area in the z table is 0.8944
#Bigger area i.e. 0.8944 - smaller area i.e= 0.5