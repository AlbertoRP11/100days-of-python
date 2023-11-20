# Day 16
# Object Oriented Programming (OOP)
# We did the same project from yesterday but now using OOP

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
items = menu.get_items()
coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()


should_continue = True

while should_continue:
    users_choice = input(f"What would you like? ({items}):")
    if users_choice == "off":
        should_continue = False
    elif users_choice == "report":
        coffe_machine.report()
        money_machine.report()
    elif users_choice == "espresso" or users_choice == "latte" or users_choice == "cappuccino":
        drink = menu.find_drink(users_choice)
        if coffe_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_machine.make_coffee(drink)
        # I had done the code below, but we can simplify it by making it like the code above:
        # enough_resources = coffe_machine.is_resource_sufficient(drink)
        # if enough_resources:
        #     enough_money = money_machine.make_payment(drink.cost)
        #     if enough_money:
        #         coffe_machine.make_coffee(drink)
