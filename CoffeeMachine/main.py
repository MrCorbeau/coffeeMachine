from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def clear():
    return print(end="\033c")

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machineRun = True
machineCont = True

while machineRun:
    options = menu.get_items()
    user = input("What would you like? (espresso/latte/cappuccino/) : ").lower()
    if user == "off":
        machineRun = False
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


