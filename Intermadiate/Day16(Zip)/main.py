from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



#is_on = True
coffee_maker = CoffeeMaker()

menu = Menu()
moneymachine = MoneyMachine()



#while is_on: 
    
choice = input("​What would you like? (espresso/latte/cappuccino): ")

options = menu.get_items()

if choice in options: 
    drink = menu.find_drink(choice)
    print(drink)