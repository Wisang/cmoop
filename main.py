from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
mu = Menu()

turn_off = False

while not turn_off:
    order = input("What would you like? (espresso/latte/cappuccino/): ")
    if order == "off":
        turn_off = True
    elif order == "report":
        cm.report()
        mm.report()
    else:
        mi = mu.find_drink(order)
        cost = mu.find_drink(order).cost
        if cm.is_resource_sufficient(mi) and mm.make_payment(cost):
            cm.make_coffee(mi)







