from Day11_Blackjack_Art import logo
import random
import os

def clear():
    os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    rand_card = cards[random.randint(0, len(cards)-1)]
    return rand_card

def calculate_score(player_list):
    total = sum(player_list)
    if 11 in player_list and total > 21:
        for i, card in enumerate(player_list):
            if card == 11:
                player_list[i] == 1
    if total == 21:
        return 0
    else:
        return total

def play_game():
    user_cards = []
    computer_cards = []
    for x in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    cont_game = True
    while cont_game:
        print(logo)
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        if calculate_score(computer_cards) == 0:
            print("You lose, computer has blackjack!")
            cont_game = False
        elif calculate_score(user_cards) == 0:
            print("You win, you have blackjack!")
            cont_game = False
        add_card_cont = True
        while add_card_cont:
            add_card = input("Type 'y' to get another card, type 'n' to pass:")
            if add_card == 'y':
                user_cards.append(deal_card())
                if calculate_score(user_cards) > 21:
                    add_card_cont = False
            if add_card == 'n':
                add_card_cont = False
        while calculate_score(computer_cards) <= 17:
            computer_cards.append(deal_card())
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")
        if calculate_score(computer_cards) == 21:
            print("You lose!")
        elif calculate_score(computer_cards) > 21:
            print("You win, computer busts!")
        elif calculate_score(user_cards) > 21:
            print("You lose, you busted!")
        elif calculate_score(user_cards) > calculate_score(computer_cards):
            print("You win!")
        elif calculate_score(user_cards) < calculate_score(computer_cards):
            print("You lose!")
        elif calculate_score(user_cards) == calculate_score(computer_cards):
            print("push")
        else:
            print("error")
        cont_game = False


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    clear()
    play_game()
