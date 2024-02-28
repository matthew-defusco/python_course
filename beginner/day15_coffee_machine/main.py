from data import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_choice):
    """Checks the resources and returns True if there are enough and False if there aren't"""
    drink = MENU[drink_choice]
    if resources["water"] < 50 or resources["coffee"] < 18:
        print("Sorry, there's not enough resources left!")
        return False

    water = drink["water"]
    milk = drink["milk"]
    coffee = drink["coffee"]

    if resources["water"] - water < 0:
        print("Sorry! There's not enough water for that drink.")
        return False
    elif resources["milk"] - milk < 0:
        print("Sorry! There's not enough milk for that drink.")
        return False
    elif resources["coffee"] - coffee < 0:
        print("Sorry! There's not enough coffee for that drink.")
        return False
    else:
        print("There are enough resources!")
        make_drink(drink)
        return True


def make_drink(drink_choice):
    """Deducts quantities from resources."""
    resources["water"] -= drink_choice["water"]
    resources["milk"] -= drink_choice["milk"]
    resources["coffee"] -= drink_choice["coffee"]


def get_payment():
    """Returns the total amount entered."""
    quarters = int(input("How many quarters?"))
    nickels = int(input("How many nickels?"))
    dimes = int(input("How many dimes?"))
    pennies = int(input("How many pennies?"))
    return quarters * 0.25 + nickels * 0.05 + dimes * 0.1 + pennies * 0.01


on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(resources)
    else:
        enough = check_resources(choice)
        if enough:
            cost = MENU[choice]["price"]
            print(f"Great choice! Your total comes to {cost}. Please insert coins now.")
            payment = round(get_payment(), 2)
            while payment < cost:
                print(f"Sorry, that's not enough. You entered {payment}. There's still {round(cost - payment, 2)} left."
                      "Please insert more coins.")
                payment += round(get_payment(), 2)
            if payment > cost:
                print(f"Thank you! Your change is ${round(payment - cost, 2)}.")
                profit += cost
            else:
                print("Enjoy your drink!")
                profit += cost