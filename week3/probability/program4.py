"""You toss a fair coin three times write a program to find following:
What is the probability of three heads, HHH?
What is the probability that you observe exactly one heads?
Given that you have observed at least one heads, what is the probability that you observe at least two heads?"""



outcomes_of_3_heads=1
total_outcomes=8

a=(outcomes_of_3_heads/total_outcomes)
print('probability of  three heads, HHH-',a)

outcomes_of_exactly_1_head=3

b=(outcomes_of_exactly_1_head/total_outcomes)
print('probability of getting exactly one heads-',b)


outcomes_of_atleast_1_heads=7
outcomes_of_atleast_2_heads=4
c=(outcomes_of_atleast_2_heads/outcomes_of_atleast_1_heads)

print('given that you observe atleast one heads the probability that you observe at least two heads-',c)