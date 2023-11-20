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
    # "profit": 0,
}
profit = 0


def get_user_choice():
    """Gets the user's choice and return it"""
    return input("What would you like? (espresso/latte/cappuccino):").lower()


def get_money():
    """Return the total amount of money the user put into the machine"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_money(money, choice):
    """Checks if the total amount of money is enough for the item that the users chose"""
    global profit
    if money >= MENU[choice]["cost"]:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        if choice != "espresso":
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        profit += MENU[choice]["cost"]
        if money > MENU[choice]["cost"]:
            print(f"Here is ${money - MENU[choice]['cost']:.2f} dollars in change.")
        print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def resources_report():
    """Prints the status of the resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(coffee_type):
    """Checks if the resources in the machine are enough for the user's order"""
    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
            print("Sorry, there's not enough water.")
        elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
            print("Sorry, there's not enough coffee.")
        elif coffee_type != "espresso" and resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
            print("Sorry, there's not enough milk.")
        else:
            return True
    elif coffee_type == "report":
        resources_report()
    elif coffee_type == "off":
        return
    else:
        print("Select a valid option!")
        get_user_choice()


def main():
    should_continue = True
    while should_continue:
        choice = get_user_choice()
        if choice == "off":
            should_continue = False
        enough_resources = check_resources(choice)
        if enough_resources:
            money = get_money()
            check_money(money, choice)


main()
