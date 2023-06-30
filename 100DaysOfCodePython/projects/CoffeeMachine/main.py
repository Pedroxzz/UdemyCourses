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
    "milk": 0,
    "coffee": 100,
}


def report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(order, money):
    resources_sufficient = True
    ingredients = MENU[order]["ingredients"]

    if 'water' in ingredients:
        qtd_water = ingredients["water"]
    else:
        return 0
    if 'milk' in ingredients:
        qtd_milk = ingredients["milk"]
    else:
        return 0
    if 'coffee' in ingredients:
        qtd_coffee = ingredients["coffee"]
    else:
        return 0


def process_coins():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def new_order(order, money):
    if order.lower() == "espresso":
        check_resources(order.lower(), money)
    elif order.lower() == "latte":
        check_resources(order.lower(), money)
    elif order.lower() == "cappuccino":
        check_resources(order.lower(), money)
    elif order.lower() == "report":
        report(money)


def machine():
    money = 0.00
    is_on = True
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            is_on = False
        else:
            new_order(order, money)

# TODO: Falta terminar tudo
machine()
