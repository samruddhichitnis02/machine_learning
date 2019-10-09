"""Write a program to find the probability of drawing an ace after drawing an ace on the first draw"""

total_no_of_aces=4
total_cards=52

total_aces_after_first_draw=total_no_of_aces-1
total_cards_after_first_draw=total_cards-1

probability_of_drawing_an_ace=(total_aces_after_first_draw/total_cards_after_first_draw)
print(probability_of_drawing_an_ace)