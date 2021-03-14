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

money = 0

def print_resources(water, milk, coffee, money):
    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: ${money}')

def check_resource(coffee, resources):
    for key, value in resources.items():
        if value == 0:
            return f'Sorry there is not enough {key}'
    return f'Enjoy your {coffee}'


choice = input('What would you like? (espresso/latte/cappuccino): ')

if(choice == 'report'): 
    print_resources(resources["water"], resources["milk"], resources["coffee"], money)
elif(choice == 'espresso' or choice == 'latte' or choice == 'cappuccino'):
    print(check_resource(choice, resources))
