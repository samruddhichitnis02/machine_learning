"""A radar unit is used to measure speeds of cars on a motorway. The speeds are normally distributed with a mean
of 90 km/hr and a standard deviation of 10 km/hr. Write a program to find the probability that a car picked at
random is travelling at more than 100 km/hr?"""


def calculation_of_Z(X):
    Mu=90 #value of mean from the statement
    Sigma=10 #value of standard deviation from the statement
    Z=((X-Mu)/Sigma) #calculation of Z
    return Z

Z=calculation_of_Z(100)
print('The Value of Z is-',Z)
print('P(Z>100)=P(Z>1)=1-area to the left of 1=',round((1-0.8413),4))
#if we check for 1 in positive Z table
#It will give us the area to the left of 1 and since Z>1 we want area to its right
#hence we subtract the total area that is 1 - area to the left of 1 i.e 0.8413 =0.1587