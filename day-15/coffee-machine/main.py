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
    "vending_money": 10
}

def print_resources(water, milk, coffee, vending_money):
    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Vending Money: ${vending_money}')

def check_resource(coffee, resources):
    for key, value in resources.items():
        if value == 0:
            if key == "vending_money":
                return f"Sorry there isn't enough change in the machine. Money refunded"
            return f'Sorry there is not enough {key}'

    print(f'Enjoy your {coffee}') 

def total_coins(quarters, dimes, nickels, pennies):
    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

def check_change(total_coins, cost_of_drink, vending_money):
    if total_coins > cost_of_drink:
        change = round(total_coins - cost_of_drink, 2)
        if vending_money > change:
            print(f'Here is ${change} in change')
    else:
        print("Sorry there isn't enough change in the machine. Money refunded")


choice = input('What would you like? (espresso/latte/cappuccino): ')

if(choice == 'report'): 
    print_resources(resources["water"], resources["milk"], resources["coffee"], resources["vending_money"])
elif(choice == 'espresso' or choice == 'latte' or choice == 'cappuccino'):
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    total_coins = total_coins(quarters, dimes, nickels, pennies)
    cost_of_drink = MENU[choice]["cost"]
    check_change(total_coins, cost_of_drink, resources["vending_money"])