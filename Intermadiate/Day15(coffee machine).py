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
