from Day16_OOP_Coffee.Day16_menu import Menu, MenuItem
from Day16_OOP_Coffee.Day16_coffee_maker import CoffeeMaker
from Day16_OOP_Coffee.Day16_money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like?({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)
