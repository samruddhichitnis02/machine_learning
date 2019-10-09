"""Given the following statistics, write a program to find the probability that a woman has cancer if she has a positive
 mammogram result?
a. One percent of women over 50 have breast cancer.
b. Ninety percent of women who have breast cancer test positive on mammograms.
c. Eight percent of women will have false positives.
"""


PA=(1/100) #Probability that a women has cancer(Hypothesis)
PNA=(1-PA)

P_of_X_given_A=(90/100)
PXNA=(8/100) #Probability of a positive result but not having cancer

P_of_A_given_X=((P_of_X_given_A*PA)/((P_of_X_given_A*PA)+(PXNA*PNA)))
print("he probability that a woman has cancer if she has a positive mammogram result is-",P_of_A_given_X)