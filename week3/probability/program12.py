"""Write a program to find the probability of getting a random number from the interval [2, 7]"""


import random
x=[ ]
random_number=random.randrange(50)
print('The random number generated is-',random_number)
if random_number in range(2,8):
    P=round((1/6),2)
    print('the probability of getting that number in the interval  [2, 7] is',P)
else:
    print('the probability of getting that number in the interval [2, 7] is-',0)