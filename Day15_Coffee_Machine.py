MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    

def money_required(cof_type):
    cost = MENU[cof_type]['cost']
    return cost

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def coin_comparison(total_given, total_cost):
    total_given = round(total_given, 2)
    total_cost = round(total_cost, 2)
    if total_given > total_cost:
        dif_amount = round(total_given - total_cost,2)
        print(f"You paid ${total_given} and the cost was ${total_cost}. Here is the ${dif_amount} in change")
        return True
    elif total_cost > total_given:
        dif_amount = round(total_cost - total_given,2)
        print(f"You paid ${total_given} and the cost was ${total_cost}. You owe us ${dif_amount} more than what you provided")
        return False
    else:
        print("Thank you!")
        return True

def resource_count(cof_order):
    for item in MENU[cof_order]['ingredients']:
        if MENU[cof_order]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True 

def resource_update(cof_order):
    for item in MENU[cof_order]['ingredients']:
        resources[item] -= MENU[cof_order]['ingredients'][item]
    print(f"Here is your {cof_order}. Enjoy!")

money_sum = 0
money_req = 0
coffee_machine_on = True

while coffee_machine_on == True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino)")
    if coffee_choice == "off":
        coffee_machine_on = False
    elif coffee_choice == "report":
        resource_report()
        print(f'Money: ${money_sum}')
    else:
        if resource_count(coffee_choice) == True:
            money_given = process_coins()
            if coin_comparison(money_given, money_required(coffee_choice)) == True:
                money_req = money_required(coffee_choice)
                money_sum += money_req
                resource_update(coffee_choice)
  
