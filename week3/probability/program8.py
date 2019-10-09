"""In a communication system each data packet consists of 1000 bits. Due to the noise, each bit may be received in
error with probability 0.1. It is assumed bit errors occur independently. Find the probability that there are more
than 120 errors in a certain data packet.
"""


import math
def Calculation(X):
    n=1000 #number of bits in each packet
    EXi =0.1  # Mean Value of each bit
    Var=EXi*(1-EXi)
    Sigma=math.sqrt(Var)
    Z = ((X - (n * EXi)) / (Sigma * math.sqrt(n)))  # Calculating the value of Z
    return Z

Z=Calculation(120)
print('The Value of Z is-',round(Z,2))

print('Hence P(x>120) = P(x>2.11) = 1 - [area to the left of 2.11]=',round((1-0.9826),4))
#if we check for 2.11 in positive Z table
#It will give us the area to the left of 2.11 and since Z>2.11 we want area to its right
#hence we subtract the total area that is 1 -area to the left of 2.11 i.e 0.9826 =0.0174