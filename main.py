#Import from moduls
from art import logo, vs
from game_data import data
from random import randint
from replit import clear

#     []     {}
#First A
a = data[randint(0, len(data) - 1)]
a_print = f"{a['name']}, a {a['description']}, from {a['country']}."
a_value = a['follower_count']
a_all = (a, a_print, a_value)

#First B
b = data[randint(0, len(data) - 1)]
b_print = f"{b['name']}, a {b['description']}, from {b['country']}."
b_value = b['follower_count']
b_all = (b, b_print, b_value)

#First Score
score = 0

#Print Logo
print(logo)

#Fuction for game
def game(a_all, b_all):
    a, a_print, a_value = a_all
    b, b_print, b_value = b_all
    #show logo and answers
    print(f"Compare A: {a_print}")
    print(vs)
    print(f"Against B: {b_print}")

    quest = input("Who has more followers? Type 'A' or 'B': ").upper()
    max_value = max(a_value, b_value)
    
    if quest == "A":
        quest = a_value
    elif quest == "B":
        quest = b_value
    global score
    if quest == max_value:
        score += 1
        
        a_all = b_all

        b = data[randint(0, len(data) - 1)]
        b_print = f"{b['name']}, a {b['description']}, from {b['country']}."
        b_value = b['follower_count']
        b_all = (b, b_print, b_value)

        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        game(a_all, b_all)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return False

game(a_all, b_all)