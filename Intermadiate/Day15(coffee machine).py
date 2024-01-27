########## The code I wrote. ##########
def input_money():
    print("Please insert coins.")
    quarters=float(input("How many quarters?"))
    dimes=float(input("How many dimes?"))
    nickles=float(input("How many nickles?"))
    pennies=float(input("How many pennies?"))
    total_input = float(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies )
    print(f"Here is ${total_input} in change.")
    return total_input


def check():
    if action == "report":
        water=resource["Water"]
        milk = resource["Milk"]
        coffee = resource["Coffee"]
        money = resource["Money"]
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")
    if action == "espresso": 
        
        rest_water = int(resource["Water"])
        rest_milk = int(resource["Milk"])
        rest_coffee = int(resource["Coffee"])
        if rest_water < 50 :
            print("Sorry there is not enough water.")
            coffee_machine = False
        elif rest_coffee < 18:
            print("Sorry there is not enough coffee.")
            coffee_machine = False
        elif total_input < 1.5:
            print("Sorry there is not enough money. Please refunded.")
            coffee_machine = False
        else:
            print("Here is your espresso. Enjoy!")
    if action == "latte" : 
        rest_water = int(resource["Water"])
        rest_milk = int(resource["Milk"])
        rest_coffee = int(resource["Coffee"])
        if rest_water < 200 :
            print("Sorry there is not enough water.")
            coffee_machine = False
        elif rest_milk < 150: 
            print("Sorry there is not enough milk.")
            coffee_machine = False
        elif rest_coffee < 24:
            print("Sorry there is not enough coffee.")
            coffee_machine = False
        elif total_input < 2.5:
            print("Sorry there is not enough money. Please refunded.")
            coffee_machine = False
        else:
            print("Here is your latte. Enjoy!")
    if action == "cappuccino": 
        rest_water = int(resource["Water"])
        rest_milk = int(resource["Milk"])
        rest_coffee = int(resource["Coffee"])
        
        if rest_water < 250 :
            print("Sorry there is not enough water.")
            coffee_machine = False
        elif rest_milk < 100: 
            print("Sorry there is not enough milk.")
            coffee_machine = False
        elif rest_coffee < 24:
            print("Sorry there is not enough coffee.")
            coffee_machine = False
        elif total_input < 3:
            print("Sorry there is not enough money. Please refunded.")
            coffee_machine = False
        else:
            print("Here is your cappuccino. Enjoy!")


def minus_resource():
    global resource
    global action
    if action == "espresso":
        resource["Water"]-= 50
        resource["Coffee"]-= 18
        resource["Money"]+= 1.5

    elif action == "latte" :
        resource["Water"] -= 200
        resource["Coffee"] -= 24
        resource["Milk"] = -150
        resource["Money"]+=2.5

    elif action == "cappuccino":
        resource["Water"]-=250
        resource["Coffee"]-=24
        resource["Milk"]-=100
        resource["Money"]+=3

    return resource


coffee_machine = True


while coffee_machine==True: 
    resource={"Water":300, "Milk":200, "Coffee":100, "Money":0}
    action = str(input("What would you like? (espresso/latte/cappuccino)"))
    total_input = input_money()
    check()
    resource = minus_resource()


########## The standard code ##########
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""              ### add explaination after the function()
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False                                                                           ### A function can just return a true or false 
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





