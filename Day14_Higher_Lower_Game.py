from Day14_Higher_Lower_Game_Art import logo, vs
from Day14_Higher_Lower_Game_Data import data
import random
import os

def celeb_info(number, info_type):
    '''
    type can be "name", "follower_count", "description", or "country"
    '''
    df = data[number][info_type]
    return df

def rand_int():
    num = random.randint(0, len(data)-1)
    return num

# Need formula to check answer
def check_answer(guess, a, b):
    if guess == 'a':
        if a > b:
            return 'correct'
        else:
            return 'incorrect'
    else:
        if b > a:
            return 'correct'
        else:
            return 'incorrect'

def clear():
    '''
    clears the terminal
    '''
    os.system('cls')


rand_int_b = rand_int()
score_correct = 0
correct = True
print(logo)
while correct:
    rand_int_a = rand_int_b
    print(f"Compare A: {celeb_info(number=rand_int_a, info_type='name')}, a {celeb_info(number=rand_int_a, info_type='description')} from {celeb_info(number=rand_int_a, info_type='country')}")
    print(vs)
    rand_int_b = rand_int()
    if rand_int_a == rand_int_b:
        if rand_int_b == 49:
            rand_int_b == 0
        else:
            rand_int_b +=1

    print(f"Against B: {celeb_info(number=rand_int_b, info_type='name')}, a {celeb_info(number=rand_int_b, info_type='description')} from {celeb_info(number=rand_int_b, info_type='country')}")
    guess = input("Who has the most followers? Type 'A' or 'B': ").lower()
    c_or_i = check_answer(guess, celeb_info(number=rand_int_a, info_type='follower_count'), celeb_info(number=rand_int_b, info_type='follower_count'))  
    if c_or_i == 'correct':
        score_correct += 1
        clear()
        print(logo)
        print(f"You're right! Current score is {score_correct}.")
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score is {score_correct}")
        correct = False

