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


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: $")


def check_resources(type):
    resources_sufficient = True
    ingredients = MENU[type]["ingredients"]

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

    while resources_sufficient > True:
        if resources["milk"] - qtd_milk >= 0:
            resources["milk"] = resources["milk"] - qtd_milk
        else:
            print("Sorry there is not enough milk")
            resources_sufficient = False


def new_order(order):
    if order.lower() == "espresso":
        check_resources(order.lower())
    elif order.lower() == "latte":
        check_resources(order.lower())
    elif order.lower() == "cappuccino":
        check_resources(order.lower())
    elif order.lower() == "report":
        report()


def machine():
    money = 0.00
    order = input("What would you like? (espresso/latte/cappuccino): ")
    new_order(order)


machine()
