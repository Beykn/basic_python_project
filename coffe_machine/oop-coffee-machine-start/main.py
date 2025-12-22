from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

decision = input("What would you like? (espresso/latte/cappuccino): ")
menu_decision = Menu()
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True

while is_on:

    if decision == "report":
        coffeMaker.report()
        moneyMachine.report()
    elif decision == "off":
        exit()
    else:
        drink = menu_decision.find_drink(decision)
        if coffeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeMaker.make_coffee(drink)

