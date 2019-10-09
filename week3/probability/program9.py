"""In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. Overall, five percent of the
clinic’s patients are addicted to narcotics (including pain killers and illegal substances). Out of all the people
prescribed pain pills, 8% are addicts. If a patient is an addict, write a program to find the  probability that they
will be prescribed pain pills?"""



PA=(10/100)#probability of A(Hypothesis,patient prescribed with pain killers)

PB=(5/100)#probability of B(an addict,Evidence)
P_of_B_given_A=(8/100)

P_of_A_given_B=((P_of_B_given_A*PA)/PB)#Formula for Bayes Theorem
print('The Probability that an addict will be prescribed pain pills is-',P_of_A_given_B)
