"""Write a program to find the probability of drawing an ace after drawing a king on the first draw
"""

total_no_of_aces=4
total_cards=52
total_cards_after_drawing_ace=total_cards-1

probability_of_drawing_ace=(total_no_of_aces/total_cards_after_drawing_ace)
print(probability_of_drawing_ace)