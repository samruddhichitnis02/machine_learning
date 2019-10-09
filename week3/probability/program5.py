"""In my town, it's rainy one third of the days. Given that it is rainy, there will be heavy traffic with probability 12,
and given that it is not rainy, there will be heavy traffic with probability 14.
If it's rainy and there is heavy traffic, I arrive late for work with probability 12. On the other hand, the probability
of being late is reduced to 18 if it is not rainy and there is no heavy traffic. In other situations (rainy and no traffic, not rainy and traffic)
the probability of being late is 0.25. You pick a random day.
Write a program to find following
a.What is the probability that it's not raining and there is heavy traffic and I am not late?
b.What is the probability that I am late?
c.Given that I arrived late at work, what is the probability that it rained that day?
"""




 #R event that it's raining   Rc event that it's not raining
 #T event of heavy traffic    Tc event of no traffic
 #L event that I am late      Lc event that I am not late

R=(1/3)
Rc=1-R

RcT=(1/4) #Probability of Event that there is no rain but heavy traffic
RcTL=(1/4)

PRcTL=(Rc*RcT*RcTL)# probability of Event that there is no rain but heavy traffic and I am late


RcTLc=(1-RcTL)#Event that there is no rain but heavy traffic and I am not late
PRcTLc=(Rc*RcT*RcTLc)#probability of Event that there is no rain but heavy traffic and I am not late

P_of_T_intersection_Rc=(PRcTL+PRcTLc)

P_of_Lc_intersection_Rc_intersection_T=PRcTLc

Event_A=(Rc)*(P_of_T_intersection_Rc/Rc)*(P_of_Lc_intersection_Rc_intersection_T/P_of_T_intersection_Rc)
print("the probability that it's not raining and there is heavy traffic and I am not late-",Event_A)#Probability that it's not raining & there is heavy traffic & I am not Late

RT=(1/2)#Probability of Event that it's raining & there is heavy traffic
RTL=(1/2)
PRTL=(R*RT*RTL)#Probability of Event that it's raining & there is heavy traffic & I am late

RTc=1-(RT)#Probability of Event that it's raining and there is no traffic
RTcL=(1/4)
PRTcL=(R*RTc*RTcL)#Probability of event that its Raining & there is no traffic & I am Late

RcTc=(1-RcT)#Probability of event that it's not raining & there is no traffic
RcTcL=(1/8)
PRcTcL=(Rc*RcTc*RcTcL)#Probability of event that it's not Raining & there is no traffic & I am late

Event_B=(PRTL+PRTcL+PRcTL+PRcTcL)
print("the probability that I am late-",Event_B)#Probability that I am late

P_R_by_L=((PRTL+PRTcL)/Event_B)
Event_C=P_R_by_L
print("Given that I arrived late at work,probability that it rained that day",Event_C)
