import os
from Day9_Secret_Auction_Art import logo

def clear():
    os.system('cls')

print(logo)
print("Welcome to the secret auction program.")

def bidder_dict_add(dict, bid_name, bid_value):
    dict[bid_name] = bid_value
    
bid_dict = {}
other_bidder = True

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while other_bidder == True:
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))
    bidder = input("Are there any other bidders? Typer 'yes' or 'no'.").lower()
    bidder_dict_add(bid_dict, name, bid)
    if bidder == 'no':
        other_bidder = False
        highest_bidder(bid_dict)
    elif bidder == 'yes':
        clear()
